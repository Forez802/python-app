import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "sumdb")
    )

def insert_result(a, b, result):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (a, b, result) VALUES (%s, %s, %s)", (a, b, result))
    conn.commit()
    conn.close()

def get_all_results():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM results")
    results = cursor.fetchall()
    conn.close()
    return results
