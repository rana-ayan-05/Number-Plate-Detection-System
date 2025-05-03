# This program is used to insert plate number to database while detected in real time along with 
# from image with time

import mysql.connector

def insert_Data_from_image(number_plate_pass):
    # Database connection
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='npds'
    )

    cursor = db_connection.cursor()

    number_plate = number_plate_pass # take from Image_main file

    if number_plate:
        cursor.execute(
            "INSERT INTO vehicle_entries (number_plate) VALUES (%s)",(number_plate,)
        )
        db_connection.commit()
        print(f"Inserted {number_plate} from Image_main.py")

    # Close the database connection
    cursor.close()
    db_connection.close()
