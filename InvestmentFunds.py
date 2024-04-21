class InvestmentFunds:

    CREATE_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS funds
             (fund_id TEXT PRIMARY KEY, fund_name TEXT, fund_manager_name TEXT, fund_description TEXT,
              fund_nav REAL, creation_date TEXT, performance REAL)'''

    SELECT_ALL_FUNDS_QUERY = 'SELECT * FROM funds'
    NEW_FUND_QUERY = 'INSERT INTO funds (fund_id, fund_name, fund_manager_name, fund_description, fund_nav, creation_date, performance) VALUES (?, ?, ?, ?, ?, ?, ?)'
    GET_FUND_QUERY = 'SELECT * FROM funds WHERE fund_id = ?'
    UPDATE_FUND_QUERY = 'UPDATE funds SET performance = ? WHERE fund_id = ?'
    DELETE_FUND_QUERY = 'DELETE FROM funds WHERE fund_id = ?'



    def __init__(self, fund_id, fund_name, fund_manager_name, fund_description, fund_nav, creation_date, performance):
        self.fund_id = fund_id
        self.fund_name = fund_name
        self.fund_manager_name = fund_manager_name
        self.fund_description = fund_description
        self.fund_nav = fund_nav
        self.creation_date = creation_date
        self.performance = performance

    @classmethod
    def from_dict(cls, data):
        return cls(
            fund_id=data['fund_id'],
            fund_name=data['fund_name'],
            fund_manager_name=data['fund_manager_name'],
            fund_description=data['fund_description'],
            fund_nav=data['fund_nav'],
            creation_date=data['creation_date'],
            performance=data['performance']
        )
    
    def __str__(self):
        return f"Fund ID: {self.fund_id}\nFund Name: {self.fund_name}\nFund Manager: {self.fund_manager_name}\nDescription: {self.fund_description}\nNAV: {self.fund_nav}\nCreation Date: {self.creation_date}\nPerformance: {self.performance}%"


if __name__ == "__main__":
    # Example usage
    data = {
        'fund_id': '123',
        'fund_name': 'My Fund',
        'fund_manager_name': 'John Doe',
        'fund_description': 'This is a description of my fund.',
        'fund_nav': 1000000,
        'creation_date': '2024-04-21',
        'performance': 10.5
    }

    fund = InvestmentFunds.from_dict(data)
    print(fund.fund_id)


# # Example usage
# fund = InvestmentFunds(
#     fund_id='123',
#     fund_name='My Fund',
#     fund_manager_name='John Doe',
#     fund_description='This is a description of my fund.',
#     fund_nav=1000000,
#     creation_date='2024-04-21',
#     performance=10.5
# )

# print(fund)
