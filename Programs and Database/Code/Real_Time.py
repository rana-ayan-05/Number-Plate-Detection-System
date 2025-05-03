import cv2
import easyocr
import numpy as np
import time

# User-defined modules
import db_1, remove_space, validate_plate, fetch_plate_db

# Initialize EasyOCR reader once (GPU=False for compatibility)
reader = easyocr.Reader(['en'], gpu=False)

# Load Haar Cascade once
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Track previously detected plates with timestamps
recent_plates = {}

# Time in seconds to ignore repeat detections
DUPLICATE_TIMEOUT = 10  # 10 seconds

def preprocess_plate_region(roi):
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    filtered = cv2.bilateralFilter(gray, 11, 17, 17)
    return filtered

def detect_and_recognize_number_plate(frame):
    global recent_plates
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 30))

    current_time = time.time()

    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        plate_region = frame[y:y + h, x:x + w]
        processed_plate = preprocess_plate_region(plate_region)

        result = reader.readtext(processed_plate)

        if result:
            plate_text = result[0][1]
            plate_text = remove_space.clean_number_plate(plate_text)

            if validate_plate.is_valid_indian_number_plate(plate_text):
                # Skip recently detected plates
                if plate_text in recent_plates and current_time - recent_plates[plate_text] < DUPLICATE_TIMEOUT:
                    continue  # Already detected recently

                print(f"Detected: {plate_text}")
                cv2.putText(frame, plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

                # Mark as recently detected
                recent_plates[plate_text] = current_time

                db_1.insert_Data_from_image(plate_text)
                fetch_plate_db.fetch_data_from_db(plate_text)
            else:
                print(f"Invalid format: {plate_text}")
        else:
            print("No text detected")

    # Clean up old entries
    recent_plates = {
        plate: ts for plate, ts in recent_plates.items() if current_time - ts < DUPLICATE_TIMEOUT
    }

    return frame

def real_time_detection():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open webcam.")
        return

    print("Press 'Q' to exit...\n")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        result_frame = detect_and_recognize_number_plate(frame)
        cv2.imshow('Real-Time Number Plate Detection', result_frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    real_time_detection()
