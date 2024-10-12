import qrcode

def generate_qr_code(data, filename):
    """
    Generate a QR code from the given data and save it to a file.

    Args:
        data (str): The data to encode in the QR code
        filename (str): The filename to save the QR code to
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
data = "https://www.example.com"  # Replace with your desired data
filename = "qrcode.png"
generate_qr_code(data, filename)
