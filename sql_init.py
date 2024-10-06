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

populate_tables = """

INSERT INTO Bank (Name, Location) VALUES
	("Chase", "Provo_UT"),
    ("KeyBank", "Orem_UT");

INSERT INTO User (Name, Username, Email, BankID) values
	("Bob Jones", "bobj", "bobj@gmail.com", "1"),
    ("Kelly Smith", "kesmi", "kesm@gmail.com", "2"),
    ("Ronald McDonald", "ronaldmcdonald", "mcdon@email.com", "1"),
    ("Sarah Johnson", "sarahj", "sarah@email.com", "1"),
    ("Karen Hansen", "karenh", "kaha@gmail.com", "2"),
    ("Roberto Hernandez", "robertoh", "rohe@gmail.com", "2"),
    ("Maria Rivera", "MariaR", "mari@gmail.com", "2"),
    ("Joseph Oaks", "JoeOak", "joak@gmail.com", "1");

INSERT INTO Account (UserID, Type, Balance, BankID) VALUES
    (1, 'Checking', 26403.13, 1),
    (2, 'Savings', 57193.34, 2),
    (3, 'Savings', 1053515.44, 1),
    (4, 'Checking', 55913.12, 1),
    (5, 'Checking', 844.33, 2),
    (6, 'Savings', 40518.44, 2),
    (7, 'Checking', 1043853.22, 2),
    (8, 'Savings', 4003.50, 1);

INSERT INTO Transaction (AccountID, Type, RecipientID, Amount, Date) VALUES
	(1, 'Deposit', null, 2000.50, "2024-06-15"),
    (3, 'Transfer', 4, 5000.00, "2024-07-11"),
    (5, 'Withdrawal', null, 200.00, "2024-05-16"),
    (7, 'Transfer', 6, 1250.50, "2024-09-22"),
    (8, 'Deposit', null, 3000.00, "2024-10-4"),
    (3, 'Withdrawal', null, 50.00, "2024-10-01");
	(1, 'Withdrawal', null, 150.00, "2024-06-20"),
    (2, 'Deposit', null, 5000.00, "2024-06-25"),
    (3, 'Withdrawal', null, 200.00, "2024-06-30"),
    (4, 'Deposit', null, 1200.00, "2024-07-02"),
    (5, 'Transfer', 7, 300.00, "2024-07-15"),
    (6, 'Withdrawal', null, 1000.00, "2024-08-01"),
    (7, 'Deposit', null, 250.75, "2024-08-05"),
    (1, 'Transfer', 8, 1500.00, "2024-08-12"),
    (2, 'Withdrawal', null, 600.00, "2024-08-20"),
    (3, 'Deposit', null, 700.00, "2024-09-01"),
    (4, 'Withdrawal', null, 800.00, "2024-09-10"),
    (5, 'Deposit', null, 100.00, "2024-09-15"),
    (6, 'Transfer', 1, 2500.00, "2024-09-18"),
    (7, 'Withdrawal', null, 50.00, "2024-09-20"),
    (8, 'Deposit', null, 150.00, "2024-09-25"),
    (1, 'Transfer', 2, 750.00, "2024-09-28"),
    (3, 'Deposit', null, 3000.00, "2024-10-02"),
    (4, 'Withdrawal', null, 400.00, "2024-10-03"),
    (5, 'Transfer', 6, 300.00, "2024-10-05"),
    (2, 'Deposit', null, 4500.00, "2024-10-06"),
    (8, 'Withdrawal', null, 600.00, "2024-10-07");

"""