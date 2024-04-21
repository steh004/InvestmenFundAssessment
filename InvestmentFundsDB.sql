CREATE TABLE IF NOT EXISTS investmentfunds (
    fund_id TEXT PRIMARY KEY,
    fund_name TEXT,
    fund_manager_name TEXT,
    fund_description TEXT,
    fund_nav REAL,
    creation_date TEXT
);

CREATE TABLE IF NOT EXISTS fund_performances (
    performance_id TEXT PRIMARY KEY,
    fund_id TEXT,
    performance_date TEXT,
    performance REAL NOT NULL,
    FOREIGN KEY (fund_id) REFERENCES investmentfunds(fund_id)
);