""" import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess

def run_image_detection():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:  # If user selects a file
        subprocess.run(['python', 'Image_main.py', file_path])
    else:
        messagebox.showwarning("No File Selected", "Please select an image to proceed.")

def run_camera_detection():
    subprocess.run(['python', "Real_Time.py"])
    # subprocess.run(['python', "1-Real_Time-old-main.py"])
    # subprocess.run(['python', "2-Real_Time-old-main.py"])

def show_options():
    for widget in main_window.winfo_children():
        widget.destroy()
    
    title_label = tk.Label(main_window, text="OPTIONS", font=("Arial", 24, "underline"), fg="brown", bg='lightgray')
    title_label.pack(pady=20)
    
    img_icon = Image.open("Images/GUI Images/image1.jpg").resize((100, 100))
    img_icon = ImageTk.PhotoImage(img_icon)
    cam_icon = Image.open("Images/GUI Images/image3.jpg").resize((100, 100))
    cam_icon = ImageTk.PhotoImage(cam_icon)
    
    main_window.img_icon = img_icon
    main_window.cam_icon = cam_icon
    
    img_label = tk.Label(main_window, image=img_icon, bg='lightgray')
    img_label.place(x=200, y=130)
    img_button = tk.Button(main_window, text="UPLOAD IMAGE & DETECT ➡", font=("Arial", 14, "bold"), fg="blue", bg="lightgreen", width=30, height=2, command=run_image_detection)
    img_button.place(x=350, y=150)
    
    cam_label = tk.Label(main_window, image=cam_icon, bg='lightgray')
    cam_label.place(x=200, y=280)
    cam_button = tk.Button(main_window, text="DETECT FROM CAMERA ➡", font=("Arial", 14, "bold"), fg="blue", bg="lightgreen", width=30, height=2, command=run_camera_detection)
    cam_button.place(x=350, y=300)
    
    exit_button = tk.Button(main_window, text="↩ BACK", font=("Arial", 14, "bold"), fg="blue", bg="red", width=15, height=2, command=setup_main_screen)
    exit_button.place(x=400, y=480)

def setup_main_screen():
    for widget in main_window.winfo_children():
        widget.destroy()
    
    main_window.configure(bg='lightgray')
    title_label = tk.Label(main_window, text="REAL-TIME NUMBER PLATE DETECTION", font=("Arial", 24, "underline"), fg="magenta", bg='lightgray')
    title_label.pack(pady=20)
    
    placeholder1_img = Image.open("Images/GUI Images/front1.png").resize((200, 150))
    placeholder1 = ImageTk.PhotoImage(placeholder1_img)
    main_window.placeholder1 = placeholder1
    
    placeholder2_img = Image.open("Images/GUI Images/front2.png").resize((150, 150))
    placeholder2 = ImageTk.PhotoImage(placeholder2_img)
    main_window.placeholder2 = placeholder2
    
    img_label1 = tk.Label(main_window, image=placeholder1, bg='lightgray')
    img_label1.image = placeholder1
    img_label1.place(x=250, y=200)
    
    img_label2 = tk.Label(main_window, image=placeholder2, bg='lightgray')
    img_label2.image = placeholder2
    img_label2.place(x=600, y=200)
    
    start_button = tk.Button(main_window, text="▶ START", font=("Arial", 14, "bold"), fg="blue", bg="orange", width=15, height=2, command=show_options)
    start_button.place(x=250, y=400)
    
    exit_button = tk.Button(main_window, text="✖ EXIT", font=("Arial", 14, "bold"), fg="blue", bg="red", width=15, height=2, command=main_window.quit)
    exit_button.place(x=600, y=400)

main_window = tk.Tk()
main_window.title("Real-Time Number Plate Detection")
main_window.geometry('1000x700')
setup_main_screen()
main_window.mainloop()
 """

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess

# Function to upload image and run detection script
def run_image_detection():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        subprocess.run(['python', 'Image_main.py', file_path])
    else:
        messagebox.showwarning("No File Selected", "Please select an image to proceed.")

# Function to open real-time detection
def run_camera_detection():
    subprocess.run(['python', "Real_Time.py"])

# Function to insert VEHICLE details into database
def submit_details():
    details = [entries[field].get() for field in ["Plate Number", "Manufacture", "Model", "Registration Year", "Vehicle Color", "Owner Name"]]
    if all(details):
        try:
            result = subprocess.run(['python', 'add_vehicle_details.py'] + details, capture_output=True, text=True)
            if "Inserted Successfully" in result.stdout:
                messagebox.showinfo("Success", "Vehicle details submitted successfully!")
                setup_main_screen()
            else:
                messagebox.showerror("Database Error", result.stdout + result.stderr)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Incomplete", "Please fill in all fields before submitting.")

# Function to create the vehicle detail entry page
def enter_car_details():
    global entries
    entries = {}
    for widget in main_window.winfo_children():
        widget.destroy()

    main_window.configure(bg='lightblue')
    tk.Label(main_window, text="Enter Vehicle Details", font=("Arial", 22, "bold"), bg='lightblue').pack(pady=20)

    labels = ["Plate Number", "Manufacture", "Model", "Registration Year", "Vehicle Color", "Owner Name"]
    for label_text in labels:
        frame = tk.Frame(main_window, bg='lightblue')
        frame.pack(pady=5)
        tk.Label(frame, text=label_text + ":", font=("Arial", 14), bg='lightblue', width=18, anchor='w').pack(side=tk.LEFT, padx=5)
        entry = tk.Entry(frame, font=("Arial", 14), width=30)
        entry.pack(side=tk.LEFT, padx=5)
        entries[label_text] = entry

    tk.Button(main_window, text="✅ Submit", font=("Arial", 14, "bold"), bg="green", fg="white", width=15, height=2, command=submit_details).pack(pady=30)
    tk.Button(main_window, text="↩ BACK", font=("Arial", 14, "bold"), bg="red", fg="white", width=15, height=2, command=show_options).pack()

# Function to show main options
def show_options():
    for widget in main_window.winfo_children():
        widget.destroy()

    title_label = tk.Label(main_window, text="OPTIONS", font=("Arial", 24, "underline"), fg="brown", bg='lightgray')
    title_label.pack(pady=20)

    img_icon = Image.open("Images/GUI Images/image1.jpg").resize((100, 100))
    img_icon = ImageTk.PhotoImage(img_icon)
    cam_icon = Image.open("Images/GUI Images/image3.jpg").resize((100, 100))
    cam_icon = ImageTk.PhotoImage(cam_icon)

    main_window.img_icon = img_icon
    main_window.cam_icon = cam_icon

    tk.Label(main_window, image=img_icon, bg='lightgray').place(x=200, y=130)
    tk.Button(main_window, text="UPLOAD IMAGE & DETECT ➡", font=("Arial", 14, "bold"), fg="blue", bg="lightgreen", width=30, height=2, command=run_image_detection).place(x=350, y=150)

    tk.Label(main_window, image=cam_icon, bg='lightgray').place(x=200, y=280)
    tk.Button(main_window, text="DETECT FROM CAMERA ➡", font=("Arial", 14, "bold"), fg="blue", bg="lightgreen", width=30, height=2, command=run_camera_detection).place(x=350, y=300)

    tk.Button(main_window, text="✍ ENTER VEHICLE DETAILS", font=("Arial", 14, "bold"), fg="blue", bg="yellow", width=30, height=2, command=enter_car_details).place(x=350, y=400)
    tk.Button(main_window, text="↩ BACK", font=("Arial", 14, "bold"), fg="blue", bg="red", width=15, height=2, command=setup_main_screen).place(x=400, y=500)

# Setup initial home screen
def setup_main_screen():
    for widget in main_window.winfo_children():
        widget.destroy()

    main_window.configure(bg='lightgray')
    title_label = tk.Label(main_window, text="REAL-TIME NUMBER PLATE DETECTION", font=("Arial", 24, "underline"), fg="magenta", bg='lightgray')
    title_label.pack(pady=20)

    placeholder1_img = Image.open("Images/GUI Images/front1.png").resize((200, 150))
    placeholder1 = ImageTk.PhotoImage(placeholder1_img)
    main_window.placeholder1 = placeholder1

    placeholder2_img = Image.open("Images/GUI Images/front2.png").resize((150, 150))
    placeholder2 = ImageTk.PhotoImage(placeholder2_img)
    main_window.placeholder2 = placeholder2

    tk.Label(main_window, image=placeholder1, bg='lightgray').place(x=250, y=200)
    tk.Label(main_window, image=placeholder2, bg='lightgray').place(x=600, y=200)

    tk.Button(main_window, text="▶ START", font=("Arial", 14, "bold"), fg="blue", bg="orange", width=15, height=2, command=show_options).place(x=250, y=400)
    tk.Button(main_window, text="✖ EXIT", font=("Arial", 14, "bold"), fg="blue", bg="red", width=15, height=2, command=main_window.quit).place(x=600, y=400)

# Main window setup
main_window = tk.Tk()
main_window.title("Real-Time Number Plate Detection")
main_window.geometry('1000x700')
setup_main_screen()
main_window.mainloop()
