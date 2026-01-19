import mysql.connector

def load_data(df):
    conn = mysql.connector.connect(
        host="localhost",
        database="sales_db",
        user="root",
        password="password"
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT IGNORE INTO sales 
            (order_id, order_date, customer_id, product, quantity, price, total_amount)
            VALUES (%s,%s,%s,%s,%s,%s,%s);
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()
import mysql.connector

def load_data(df):
    conn = mysql.connector.connect(
        host="localhost",
        database="sales_db",
        user="root",
        password="password"
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT IGNORE INTO sales 
            (order_id, order_date, customer_id, product, quantity, price, total_amount)
            VALUES (%s,%s,%s,%s,%s,%s,%s);
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()
