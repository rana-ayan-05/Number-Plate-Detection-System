import cv2
import easyocr
import numpy as np
import matplotlib.pyplot as plt
import sys

#user defined
import db_1, remove_space, validate_plate, fetch_plate_db


# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to detect and recognize number plate
def detect_and_recognize_number_plate(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use OpenCV's Haar Cascade for detecting plates (you may need to tune this path)
    # plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'indian_license_plate.xml')
    plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
    # D:\Python\Python312\Lib\site-packages\cv2\data

    # Detect number plates in the image
    plates = plate_cascade.detectMultiScale(gray, 1.1, 10)

    for (x, y, w, h) in plates:
        # Draw a rectangle around the plate
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Extract the number plate region
        plate_region = image[y:y + h, x:x + w]
        
        # Use EasyOCR to recognize text from the plate region
        result = reader.readtext(plate_region)
        
        # If OCR successfully detects text
        if result:
            plate_text = result[0][1]
            #remove space 
            plate_text = remove_space.clean_number_plate(plate_text)
            
            if validate_plate.is_valid_indian_number_plate(plate_text):
                print(f"Detected Number Plate: {plate_text}")
                cv2.putText(image, plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # database storage...
                db_1.insert_Data_from_image(plate_text)
                
                # fetch all details of number plate
                print("Fetching data from database...")   
                fetch_plate_db.fetch_data_from_db(plate_text) 
                
            else:
                print("Invalid number plate format.")

            
        else:
            print("No text detected")
    
    return image


# Function to display image using matplotlib
def show_image(image):
    # Convert color from BGR (OpenCV default) to RGB (matplotlib default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')  # Turn off axis
    plt.show()

# Function to process an image file
def process_image(image_path):
    image = cv2.imread(image_path)
    result_image = detect_and_recognize_number_plate(image)
    show_image(result_image)


# Main program
if __name__ == "__main__":
    # # Example of processing an image
    # process_image(r"Images\Vehicle Images\car-image-1.jpg")

    if len(sys.argv) < 2:
        print("Usage: python Image-main.py <image_path>")
    else:
        process_image(sys.argv[1])