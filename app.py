import streamlit as st
import qrcode
import io

# Function to generate the QR code
def generate_qr(new_url):
    """
    Generates a QR code image based on the provided URL.

    Args:
        new_url (str): The URL to encode in the QR code.

    Returns:
        None

    Generates the QR code and stores it in the `st.session_state`
    dictionary with the keys `qr_image` and `qr_url`.
    """
    if new_url:
        # Create the QR code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=40,
            border=4,
        )
        qr.add_data(new_url)  # Add the URL data
        qr.make(fit=True)  # Make the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert PIL Image to bytes for display
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()

        # Store the image and URL in `st.session_state`
        st.session_state['qr_image'] = img_bytes
        st.session_state['qr_url'] = new_url

# App title and description
st.title("QR Code Generator")
st.write("Generate a QR code for any website URL.")

# Input field for URL
input_URL = st.text_input("Enter URL...", placeholder="https://your-website.com")

# calling the qrcode generator with the dynamic input
generate_qr(input_URL)

e = st.empty()

# Container for QR code display and clearing
with e.container():
    if "qr_image" in st.session_state:
        # Display QR code and URL
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.image(st.session_state['qr_image'], width=250)

        st.write(f"Encoded URL: {st.session_state['qr_url']}")

        # Clear button with conditional clearing
        if st.button("Clear"):
            st.session_state.clear()
            e.empty()  # Clear the container

