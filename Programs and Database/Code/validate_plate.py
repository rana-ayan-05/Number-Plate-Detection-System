import re

def is_valid_indian_number_plate(plate):
    # Standard Indian number plate format: e.g., KA01AB1234
    pattern = r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$'
    return re.match(pattern, plate.upper()) is not None

# # Take input from user
# user_input = input("Enter the vehicle number plate (e.g., MH12AB1234): ").strip()

# # Validate and display result
# if is_valid_indian_number_plate(user_input):
#     print("Valid Indian number plate.")
# else:
#     print("Invalid number plate format.")
