import sys
import mysql.connector

def insert_to_db(data):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='npds'
        )
        cursor = conn.cursor()
        query = """
            INSERT INTO vehicles (plate_number, make, model, year, color, owner)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, data)
        conn.commit()
        print("Data Inserted Successfully")
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 7:
        insert_to_db(tuple(sys.argv[1:]))
    else:
        print("Invalid number of arguments")
