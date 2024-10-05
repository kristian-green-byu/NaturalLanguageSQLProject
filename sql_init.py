create_tables = """
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Account;
DROP TABLE IF EXISTS Transaction;
DROP TABLE IF EXISTS Beneficiary;

CREATE TABLE User (
    ID int unsigned NOT NULL AUTO_INCREMENT,
    Name VARCHAR(40) NOT NULL,
    Username VARCHAR(30) NOT NULL,
    Email VARCHAR(30),
    PRIMARY KEY(ID)
);



"""