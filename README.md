# Natural Language SQL Project

The purpose of this project is to assess the effectiveness of gpt-4o-mini when it comes to generating SQL queries with the zero-shot method and how the single-domain double shot method differs. The SQL database we will use for this purpose models a basic bank database that has User, Account, Transaction, and Bank tables. The database will not model other complexities in the field of online banking for the sake of simplicity. The following is a schema representing our bank database:

<img src=schema.png>

For the next section of the report, we will highlight a sucessful and unsucessful query example.
## Successful Query Example
**Question**: Which user withdrew the most money overall?

**gpt-4o-mini response:**
```sql
SELECT u.Name, SUM(t.Amount) AS TotalWithdrawn
FROM Transaction t
JOIN Account a ON t.AccountID = a.AccountID
JOIN User u ON a.UserID = u.UserID
WHERE t.Type = 'Withdrawal'
GROUP BY u.UserID
ORDER BY TotalWithdrawn DESC
LIMIT 1;"
```
**Friendly Response**: The result shows that Sarah Johnson is the user who withdrew the most money, totaling $1,200.00.

As can be seen, gpt-4o-mini handled this question well and successfully joined the tables together, beforing finding the user with the highest total withdrawal sum. 


## Unsuccessful Query Example
**Question:** Which user has the most transactions of every type?

**gpt-4o-mini response:**
```sql
SELECT UserID, COUNT(*) AS TransactionCount
FROM Transaction
GROUP BY UserID
ORDER BY TransactionCount DESC
LIMIT 1;
```
**Friendly Response**: The result shows that Karen Hansen has the lowest account balance, which is $844.33.

MySQL gave us an error response from this query stating "Unknown column 'UserID' in 'field list" because the Transaction table doesn't have a column called userID. Despite this, the select still returned a result, but gpt-4o-mini incorrectly intrepreted our result as meaning that we wanted to find the user with the lowest account balance rather than the user that made the most transactions.

With a more clearly worded question, perhaps gpt would've returned the answer we were looking for. However, the largest issue that gpt-4o-mini made is that it didn't refer to the correct columns in the Transaction table, and asking the question differently may have still resulted in a similar error.
## Multi-shot Queries
Now, we will analyze the previously failed response with a multi-shot approach. Here are the results:

**Question:** Which user has the most transactions of every type?

**gpt-4o-mini response:**
```sql
SELECT u.Name, COUNT(t.TransactionID) AS TransactionCount
FROM Transaction t
JOIN Account a ON t.AccountID = a.AccountID
JOIN User u ON a.UserID = u.UserI
GROUP BY u.UserID
ORDER BY TransactionCount DESC
LIMIT 1;
```
**Friendly Response**: The user with the most transactions of every type is Ronald McDonald, and he has completed a total of 5 transactions.

Clearly, this response is significantly improved from our last example. gpt-4o-mini successfully utilized a join in order to access the name column from the User table, and it used the Account table to access the UsedID from the AccountID found in the Transaction table. 

It appears that already demonstrating a correct query  allows it to have a better idea how to join the different tables together with their respective columns.

## Conclusion:
From our results, gpt-4o-mini was mostly accurate. However, it had enough inaccuracies that non-programmers couldn't effectively interface with it and have reliable information because they would have no way of knowing if the results are accurate without being able to understand the code. On a different note, the multi-shot approach does appear to increase accuracy in gpt-4o-mini's responses by providing more context on the database.

## More examples:
<a href="zero_shot_response.json">Additional zero shot response results</a>

<a href="single_domain_double_shot_response.json">Additional multi shot response results</a>