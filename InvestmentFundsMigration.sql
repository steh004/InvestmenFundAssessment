.mode csv
.output funds.csv
SELECT * FROM funds;

LOAD DATA INFILE 'path_to_funds.csv' INTO TABLE funds
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM funds;
SELECT * FROM transactions;