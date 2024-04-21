CREATE TABLE IF NOT EXISTS funds (
    fund_id TEXT PRIMARY KEY,
    fund_name TEXT NOT NULL,
    fund_manager_name TEXT NOT NULL,
    fund_description TEXT,
    fund_nav REAL NOT NULL,
    creation_date TEXT NOT NULL,
    performance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    fund_id TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    transaction_date TEXT NOT NULL,
    FOREIGN KEY (fund_id) REFERENCES funds (fund_id)
);