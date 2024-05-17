# Importing necessary libraries
import pyqrcode
import png
from pyqrcode import QRCode
import tkinter

# Function to generate and display QR Codes
def generate_qr_codes():
    # Enter the link/text to store in the QR Code
    qr_str = "https://www.linkedin.com/in/arush-karnatak-894bb52a1/"

    # Parameters for QR Code generation
    # version specifies size and data capacity
    # error_correction levels: L, M, Q, H (H has highest error correction, smallest data capacity)
    # Other parameters: box_size, border, image_factory, mask_pattern, fit, and mode

    # Generating QR Code with specific parameters
    big_code = pyqrcode.create(qr_str, error='L', version=5, mode='binary') # mode='binary' to store any kind of data

    # Generating QR Codes for different data types

    # Numeric data: Best for encoding numeric data, can store up to 7089 digits
    num = pyqrcode.create('123456789')
    num2 = pyqrcode.create(123456789)

    # Alphanumeric data: Limited to certain ASCII characters, encodes uppercase letters, digits 0-9, space, and eight punctuation characters
    # $ % * + - . / :

    # Rendering QR Codes

    # Text-based rendering: renders QR Code in 0's and 1's format
    print(num2.text())

    # Terminal rendering: directly renders the QR Code in terminal
    print(num.terminal(module_color='blue', background='white'))

# Execute the function
generate_qr_codes()
