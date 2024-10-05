create_tables = """
    DROP TABLE IF EXISTS Transaction;
    DROP TABLE IF EXISTS Account;
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Bank;

    CREATE TABLE Bank (
        BankID INT UNSIGNED NOT NULL AUTO_INCREMENT,
        Name VARCHAR(30) NOT NULL,
        Location VARCHAR(40) NOT NULL,
        PRIMARY KEY (BankID)
    );

    CREATE TABLE User (
        UserID INT UNSIGNED NOT NULL AUTO_INCREMENT,
        Name VARCHAR(40) NOT NULL,
        Username VARCHAR(30) NOT NULL,
        Email VARCHAR(30),
        BankID INT UNSIGNED NOT NULL,
        PRIMARY KEY(UserID),
        FOREIGN KEY(BankID) REFERENCES Bank(BankID)
    );

    CREATE TABLE Account (
        AccountID INT UNSIGNED NOT NULL AUTO_INCREMENT,
        UserID INT UNSIGNED NOT NULL, 
        Type VARCHAR(30) NOT NULL,
        Balance DECIMAL(19,2) NOT NULL,
        BankID INT UNSIGNED NOT NULL,
        PRIMARY KEY(AccountID),
        FOREIGN KEY(BankID) REFERENCES Bank(BankID),
        FOREIGN KEY(UserID) REFERENCES User(UserID)
    );

    CREATE TABLE Transaction (
        TransactionID INT UNSIGNED NOT NULL AUTO_INCREMENT,
        AccountID INT UNSIGNED NOT NULL,
        Type ENUM('Deposit', 'Withdrawal', 'Transfer') NOT NULL,
        RecipientID INT UNSIGNED,
        Amount DECIMAL(19,2) NOT NULL,
        Date DATE NOT NULL,
        PRIMARY KEY(TransactionID),
        FOREIGN KEY(AccountID) REFERENCES Account(AccountID),
        FOREIGN KEY(RecipientID) REFERENCES Account(AccountID)
    );
"""