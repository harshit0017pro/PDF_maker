# PDF Converter App

This is a simple web application built with Streamlit that allows users to convert multiple JPG, PNG, and JPEG images into a single PDF file. The app uses the `img2pdf` library for fast and high-quality PDF conversion.

## Features
- Upload multiple images (JPG, PNG, JPEG)
- Combine all images into one PDF
- Download the generated PDF
- Simple and user-friendly interface

## How It Works
1. Users upload one or more image files using the file uploader.
2. Click the "Convert" button to process the images.
3. The app combines the images into a single PDF using `img2pdf`.
4. A download button appears to save the PDF locally.

## Requirements
- Python 3.7+
- Streamlit
- img2pdf

## Installation
1. Clone the repository or download the source code.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. Install dependencies:
   ```powershell
   pip install streamlit img2pdf
   ```

## Usage
1. Run the app:
   ```powershell
   streamlit run app.py
   ```
2. Open the provided local URL (usually http://localhost:8501) in your browser.
3. Upload images, click "Convert", and download your PDF.

## File Structure
- `app.py` : Main Streamlit application
- `README.md` : Project documentation

## License
This project is licensed under the MIT License.
