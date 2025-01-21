# SQL Crash course
from: [SQL crash course for data analyst](https://www.youtube.com/watch?v=FtkwIi0LofA)   
using SQL test website: [SQL Tryit editor](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_where)  

## Display commands
* `SELECT`
if database is [Customers]:
```
SELECT * FROM [Customers]
```
will display all fields and all entries from the Customers database

```
SELECT CustomerID,CustomerName FROM [Customers] 
```
will display all entries from Customers database, but only the CustomerID and CustomerName fields for each entry  
 
* `WHERE`
to get only entries with a certain value for a field, include a WHERE statement:
```
SELECT * FROM [Customers]
WHERE Country = 'Germany'
```

* `LIKE`
instead of using = in `WHERE` statements, `LIKE` can be used instead. Like allows you to use incomplete search terms, such as:
```
WHERE Country like 'A%'
```
where the % sign means the search term is A followed by anything else. This returns entries with countries that start with A, such as Argentina and Austria.   
% sign can be used at the beginning, at the end, or in the middle. The search term can be multiple characters.

* `ORDER BY`
to sort the data, use term `ORDER BY `:
```
SELECT * FROM [Customers]
ORDER BY CustomerID
```
this will sort the database by ID in increasing order. to reverse the sort, include `desc` at the end of the query:
`ORDER BY CustomerName desc`  

## Aggregation
* `SUM()`  
The sum of numerical value can be found for the entire table with the sum command, ex:
```
SELECT SUM(CustomerID) [Customers]
```
will return the value of all customerIDs summed (For the entire table).   

* `AS`  
To rename the column with a aggregated source, use AS keyword. ex. `SELECT sum(Quantity) as TotalQty FROM [OrderDetails]`.  
Technically, you don't actually need AS in this context:  
`SELECT sum(Quantity) TotalQty FROM [OrderDetails]` will do the same thing.   

* `OTHER AGGREGATION KEYWORDS`:
```
AVG()
MAX()
MIN()
```

### combining aggregate search terms
the OrderIDs from OrderDetails are not unique. If you wanted to see the total quantity of items for each order ID, you could do something like: 
```
SELECT OrderID,sum(Quantity) as TotalQty FROM [OrderDetails]
GROUP BY OrderID
```
This selects OrderID and creates a new column called TotalQty for the sum of the quantities. The GROUP BY OrderID line specifies that the sums should be grouped by unique order ID. this will display two columns. 

## if conditions
works with both `and` and `or`
```
SELECT *,
CASE WHEN Quantity >=50 THEN 'Large'
WHEN Quantity <50 AND Quantity >=20 THEN 'Medium'
WHEN Quantity <20 THEN 'Small'
END AS OrderSize
FROM [OrderDetails]
```
SQL reads sequentially, so this can be simplified: (including `else`)
```
SELECT *,
CASE
WHEN Quantity >=50 THEN 'Large'
WHEN Quantity >=20 THEN 'Medium'
ELSE 'Small'
END AS OrderSize
FROM [OrderDetails]
```

## joining databases: R/L
Tacking on new COLUMNS to the existing table  

ex joining the [Products] database and the [OrderDetails] database. Each has ProductID as a field. OrderDetails has OrderDetailID, OrderID, and Quantity, and we want Price and ProductName from Products. To join them, use the following code:
```
SELECT t1.*, t2.ProductName, t2.Price as PricePerUnit
FROM [OrderDetails] t1
left join 
[Products] t2
on t1.ProductID = t2.ProductID
```
here we name OrderDetails as t1 and Products as t2. We take all fields from t1 and only Price and ProductName from t2, renaming Price as PricePerUnit. We then left join the tables when the ProductIDs match.  

### join types
- __left join__: all entries existing in table 1 will be kept, and only matching entries in t2 will be included. if an entry exists in t2 but not in t1, it will be ommited.   
- __right join__: opposite from left, only entries in t1 that match an entry in t2 will be included  
- __inner join__: only entries that have matches in BOTH tables will be kept (like an AND operation). if there is an entry in either table that does not have a match, it will be ommited  

## unionizing tables: T/B
Tacking on new ROWS to the existing table  

Unionizing the [Suppliers] table and the [Customers] table. We want the IDs, names, and countries of both, but we want to see them all in three columns. We also want to add a type column to specify whether the entry is a customer or supplier. 
```
SELECT SupplierID as ID,SupplierName as Name,Country, 'Supplier' as Type FROM [Suppliers]
union
SELECT CustomerID as ID,CustomerName as Name,Country, 'Customer' as Type FROM [Customers]
```
Here we are selecting the IDs, names, and countries from each table. These are renamed for each to common names of ID, Name, and Country. Then a new column Type is added, with a specified entry for the whole of each table. Union is the keyword to put them together. They are autosorted by ID. 
