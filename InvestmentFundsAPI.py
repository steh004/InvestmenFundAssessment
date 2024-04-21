from flask import Flask, request, jsonify
import sqlite3
import InvestmentFunds

app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('investmentfunds.db')
c = conn.cursor()

# Create funds table if not exists
c.execute(InvestmentFunds.CREATE_TABLE_QUERY)
conn.commit()

# Endpoint to retrieve a list of all funds
@app.route('/funds', methods=['GET'])
def get_funds():
    c.execute(InvestmentFunds.SELECT_ALL_FUNDS_QUERY)
    funds = [{'fund_id': row[0], 'fund_name': row[1], 'fund_manager_name': row[2],
              'fund_description': row[3], 'fund_nav': row[4], 'creation_date': row[5], 'performance': row[6]}
             for row in c.fetchall()]
    return jsonify(funds)

# Endpoint to create a new fund
@app.route('/funds', methods=['POST'])
def create_fund():
    new_fund = InvestmentFunds.from_dict(request.json)
    c.execute(InvestmentFunds.NEW_FUND_QUERY,
              (new_fund.fund_id, new_fund.fund_name, new_fund.fund_manager_name, new_fund.fund_description, new_fund.fund_nav, new_fund.creation_date, new_fund.performance))
    conn.commit()
    return jsonify(new_fund), 201

# Endpoint to retrieve details of a specific fund using its ID
@app.route('/funds/<string:fund_id>', methods=['GET'])
def get_fund(fund_id):
    c.execute(InvestmentFunds.GET_FUND_QUERY, (fund_id,))
    fund = c.fetchone()
    if fund:
        return jsonify({'fund_id': fund[0], 'fund_name': fund[1], 'fund_manager_name': fund[2],
                        'fund_description': fund[3], 'fund_nav': fund[4], 'creation_date': fund[5], 'performance': fund[6]})
    return jsonify({'message': 'Fund not found'}), 404

# Endpoint to update the performance of a fund using its ID
@app.route('/funds/<string:fund_id>', methods=['PUT'])
def update_performance(fund_id):
    fund_updates = InvestmentFunds.from_dict(request.json)
    c.execute(InvestmentFunds.UPDATE_FUND_QUERY, (fund_updates.performance, fund_id))
    conn.commit()
    return jsonify({'message': 'Performance updated'}), 200


# Endpoint to delete a fund using its ID
@app.route('/funds/<string:fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    c.execute(InvestmentFunds.DELETE_FUND_QUERY, (fund_id,))
    conn.commit()
    return jsonify({'message': 'Fund deleted'})

if __name__ == '__main__':
    app.run(debug=True)




# # Sample data - replace with a database in a real application
# funds = [
#     {
#         'fund_id': '1',
#         'fund_name': 'Fund 1',
#         'fund_manager_name': 'Manager 1',
#         'fund_description': 'Description 1',
#         'fund_nav': 1000000,
#         'creation_date': '2024-04-21',
#         'performance': 10.5
#     },
#     {
#         'fund_id': '2',
#         'fund_name': 'Fund 2',
#         'fund_manager_name': 'Manager 2',
#         'fund_description': 'Description 2',
#         'fund_nav': 2000000,
#         'creation_date': '2024-04-22',
#         'performance': 8.5
#     }
# ]