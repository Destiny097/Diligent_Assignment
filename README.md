## Diligent Assignment

### Task 1 – Repository Setup
- Created a new GitHub repository and connected Cursor IDE to it.
- Cloned the provided starter repo inside Cursor and pushed an initial empty project structure to GitHub.
- "Hi cursor , i have an assignment coming up , i need your help in completing it , i want you to create / generate synthetic ecom data in csv format for 5 files , namely users,product,orders,order_item,payments , i want these files to be put in a sub folder called 'data' , i think 20 - 50 rows of data should suffice "
-Cursor generated 5 .csv files in a sub folder called '/data' in the root directory .

### Task 2 – Synthetic E-commerce Data
- Prompted Cursor to generate five CSV datasets (`users.csv`, `products.csv`, `orders.csv`, `order_items.csv`, `payments.csv`) containing 20–50 synthetic rows each.
- Stored the files inside the `data/` subfolder as requested.
- Prompt - "Hi cursor , i have an assignment coming up , i need your help in completing it , i want you to create / generate synthetic ecom data in csv format for 5 files , namely users,product,orders,order_item,payments , i want these files to be put in a sub folder called 'data' , i think 20 - 50 rows of data should suffice "
-Cursor generated 5 .csv files in a sub folder called '/data' in the root directory .

### Task 3 – SQLite Seeding Script
- Asked Cursor to build `seed_data.py`, which reads the CSVs with pandas and seeds an `ecom.db` SQLite database.
- Script creates the tables (`users`, `product`, `orders`, `order_item`, `payments`) with explicit schemas and loads each CSV into its table.
- Prompt - "you did the previous task accurately , i want you to use the previosly generated data in the csv files stored in "data" subfolder , and seed an sqlite database , so write a script using sqlite3 and pandas to create a sqlite database named "ecom.db" , create tables for users ,product ,orders ,order_item , payments .
load the csv files into respective tables  and save the script as 'seed_data' in  the root folder "

-then to view the database and tables created , I used SQLite viewer extension .
- Used the SQLite Viewer extension to inspect the resulting database and verify the tables.

### Task 4 – Reporting Query
- Prompted Cursor to write `query.sql`, which joins the five tables, returns `user_name`, `product_title`, `order_date`, `quantity`, `price`, `amount_paid`, and `payment_method`, sorts by `order_date`, and materializes the results into a `final_output` table inside `ecom.db`.
- Prompt - "now that its done , i want you to write a SQl query on ecom.db that joins the following tables users ,product ,orders ,order_item ,payments and return the follwing fields user_name , product_title , order_date, quantity, price, amount_paid, payment_method and could you sort it by order_date , save this query as query.sql "
- The `final_output` table can be viewed with the SQLite Viewer (or via `sqlite3` CLI).

### Task 5 – Repo Update
- Committed and pushed all generated CSV files, scripts, the SQLite database, and SQL query back to the GitHub repository to complete the assignment deliverables.

