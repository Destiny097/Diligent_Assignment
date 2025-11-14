#!/usr/bin/env python3

import sqlite3
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).parent
DATA_DIR = ROOT_DIR / "data"
DB_PATH = ROOT_DIR / "ecom.db"

SCHEMAS = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            signup_date TEXT,
            city TEXT,
            loyalty_tier TEXT
        )
    """,
    "product": """
        CREATE TABLE IF NOT EXISTS product (
            product_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            price REAL,
            cost REAL,
            stock_qty INTEGER,
            is_active INTEGER
        )
    """,
    "orders": """
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            order_date TEXT,
            status TEXT,
            shipping_method TEXT,
            shipping_cost REAL,
            discount REAL,
            total_amount REAL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """,
    "order_item": """
        CREATE TABLE IF NOT EXISTS order_item (
            order_item_id TEXT PRIMARY KEY,
            order_id TEXT NOT NULL,
            product_id TEXT NOT NULL,
            quantity INTEGER,
            unit_price REAL,
            line_total REAL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES product(product_id)
        )
    """,
    "payments": """
        CREATE TABLE IF NOT EXISTS payments (
            payment_id TEXT PRIMARY KEY,
            order_id TEXT NOT NULL,
            payment_date TEXT,
            amount REAL,
            payment_method TEXT,
            provider TEXT,
            status TEXT,
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    """,
}

CSV_SOURCES = {
    "users": DATA_DIR / "users.csv",
    "product": DATA_DIR / "products.csv",
    "orders": DATA_DIR / "orders.csv",
    "order_item": DATA_DIR / "order_items.csv",
    "payments": DATA_DIR / "payments.csv",
}


def ensure_data_files_exist() -> None:
    missing = [path for path in CSV_SOURCES.values() if not path.exists()]
    if missing:
        missing_str = ", ".join(str(path) for path in missing)
        raise FileNotFoundError(f"Missing CSV files: {missing_str}")


def seed_database() -> None:
    ensure_data_files_exist()
    DB_PATH.unlink(missing_ok=True)  # start fresh each run

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")

        for ddl in SCHEMAS.values():
            conn.execute(ddl)

        for table, csv_path in CSV_SOURCES.items():
            df = pd.read_csv(csv_path)
            conn.execute(f"DELETE FROM {table};")
            df.to_sql(table, conn, if_exists="append", index=False)

        conn.commit()


if __name__ == "__main__":
    seed_database()

