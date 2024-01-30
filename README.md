# QR Code Generator

## Overview

This simple Python app, built with Streamlit, allows you to quickly generate QR codes for any website URL. It's a convenient way to create shareable QR codes for various purposes.

## Features

User-friendly interface: Intuitive input field for entering the URL.
Dynamic QR code generation: Generates the QR code as soon as you enter a URL.
Clear display: Presents the QR code image and encoded URL prominently.
Easy clearing: The "Clear" button removes the generated QR code and resets the app.
GitHub link: Provides access to the code for exploration and modification.
## Getting Started

Prerequisites:

Python 3.6 or later
Streamlit
qrcode
Pillow (PIL Fork)


Install missing libraries using pip:

Bash
pip install streamlit qrcode Pillow


Run the app:

Bash
streamlit run your_app_file.py

(Replace your_app_file.py with the actual filename.)

## Usage

Enter the desired website URL in the input field.
The QR code and encoded URL will be generated automatically.
Click the "Clear" button to remove the QR code and start over.


## Additional Notes

If you encounter issues with the "Clear" button not clearing the container properly, try the following:
Clear your browser cache.
Double-check for any nested containers or elements within the cleared container.
Ensure unique keys for containers are consistent throughout the code.
Experiment with st.experimental_remove_widget to clear cached values.
Feel free to explore the code and customize it to your preferences!


## Contributing

I welcome contributions and feedback to improve this app! Please create issues or pull requests on the GitHub repository.


## License

MIT License: https://choosealicense.com/licenses/mit/