import qrcode
# Data to be encoded
data = "https://www.example.com"
# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction used
    box_size=10,  # Controls how many pixels each “box” of the QR code is
    border=4,  # Controls how many boxes thick the border should be
)
# Add data to the instance
qr.add_data(data)
qr.make(fit=True)
# Create an image from the QR Code instance
img = qr.make_image(fill='blue', back_color='white')
# Save the image to a file
img.save("C:/Users/Yamini Settipalli/OneDrive/Desktop/qrcode2.png")
