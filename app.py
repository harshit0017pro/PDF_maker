# Simple pdf maker 
# Import necessary libraries
import streamlit as st
import img2pdf  # Library for converting images to PDF

# Set the title and instructions 
st.title("Welcome to PDF converter")
st.text("To start upload an image below")

# File uploader widget for multiple images
images = st.file_uploader(
    "Upload an image then click on convert to convert the image in PDF:",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)
st.caption("Tip: You can drag and drop images here!")

# Button for conversion
convert_btn = st.button("Convert")

# If images are uploaded and the convert button is clicked
if images and convert_btn:
    # Read each uploaded image file 
    pix_list = [img.read() for img in images]
    # Convert the list of images to a single PDF
    pdf_c = img2pdf.convert(pix_list)
    # Provide a download button for the generated PDF
    st.success("your pdf is ready")
    st.download_button(
        label="Download PDF",
        data=pdf_c,
        file_name="your PDF.pdf",
        mime="application/pdf"
    )


# Sidebar 
st.sidebar.title("PDF Converter Options")
st.sidebar.markdown("Upload images and convert them to a PDF file easily.")
st.sidebar.info("1. Upload images\n2. Click Convert\n3. Download your PDF")

