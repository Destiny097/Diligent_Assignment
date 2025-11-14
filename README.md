## Diligent Assignment

### Task 1 – Repository Setup
- Created a new GitHub repository and connected Cursor IDE to it.
- Cloned the provided starter repo inside Cursor and pushed an initial empty project structure to GitHub.

### Task 2 – Synthetic E-commerce Data
- Prompted Cursor to generate five CSV datasets (`users.csv`, `products.csv`, `orders.csv`, `order_items.csv`, `payments.csv`) containing 20–50 synthetic rows each.
- Stored the files inside the `data/` subfolder as requested.

### Task 3 – SQLite Seeding Script
- Asked Cursor to build `seed_data.py`, which reads the CSVs with pandas and seeds an `ecom.db` SQLite database.
- Script creates the tables (`users`, `product`, `orders`, `order_item`, `payments`) with explicit schemas and loads each CSV into its table.
- Used the SQLite Viewer extension to inspect the resulting database and verify the tables.

### Task 4 – Reporting Query
- Prompted Cursor to write `query.sql`, which joins the five tables, returns `user_name`, `product_title`, `order_date`, `quantity`, `price`, `amount_paid`, and `payment_method`, sorts by `order_date`, and materializes the results into a `final_output` table inside `ecom.db`.
- The `final_output` table can be viewed with the SQLite Viewer (or via `sqlite3` CLI).

### Task 5 – Repo Update
- Committed and pushed all generated CSV files, scripts, the SQLite database, and SQL query back to the GitHub repository to complete the assignment deliverables.

