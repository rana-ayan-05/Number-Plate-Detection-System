# this code for fetching data from database and display into new pop box   
    
import tkinter as tk
from tkinter import messagebox
import mysql.connector

def fetch_data_from_db(plate_text='GJ16DJ3301'):
    def fetch_vehicle_info(plate_text):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="npds"
            )
            cursor = conn.cursor()
            query = "SELECT * FROM vehicles WHERE plate_number = %s"
            cursor.execute(query, (plate_text,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            if result:
                display_result(result)
                return True
            else:
                messagebox.showinfo("Not Found", f"Number plate '{plate_text}' not found.")
                return False
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))
            return False

    def display_result(data):
        id, plate_number, make, model, year, color, owner = data
        result_text = (
            f"Vehicle ID: {id}\n"
            f"Number Plate: {plate_number}\n"
            f"Owner Name: {owner}\n"
            f"Vehicle Model: {model}\n"
            f"Manufacture: {make}\n"
            f"Color: {color}\n"
            f"Registration Year: {year}\n"
        )
        text_output.config(state=tk.NORMAL)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, result_text)
        text_output.config(state=tk.DISABLED)

    def run_check():
        plate = plate_text.replace(" ", "").upper()
        root.result = fetch_vehicle_info(plate)

    def quit_on_q(event):
        root.destroy()

    # GUI setup
    root = tk.Tk()
    root.title("Vehicle Number Plate Checker")
    root.geometry("400x300")

    tk.Label(root, text="Vehicle Info Lookup (Press Q to Quit)", font=("Arial", 12)).pack(pady=10)
    text_output = tk.Text(root, height=10, width=50, state=tk.DISABLED, font=("Arial", 10))
    text_output.pack(pady=10)

    root.result = False
    root.after(100, run_check)

    # Bind 'q' or 'Q' key to quit
    root.bind('<q>', quit_on_q)
    root.bind('<Q>', quit_on_q)

    root.mainloop()

    return root.result

# Example usage
if __name__ == "__main__":
    found = fetch_data_from_db()
    print("Plate Found:", found)
