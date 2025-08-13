import streamlit as st
from PIL import Image
import pytesseract
import io

# Tesseract is expected to be installed as a system dependency on the server.
# The hardcoded path is removed.

st.title("🖼️ Image to Text Converter")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load image from uploaded file
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Extracting text..."):
        # Convert image to text
        try:
            extracted_text = pytesseract.image_to_string(image)
        except pytesseract.TesseractNotFoundError:
            st.error("Tesseract is not installed or not in the system's PATH. Please ensure it's installed on the server.")
            extracted_text = ""

    if extracted_text:
        st.subheader("📄 Extracted Text")
        st.text_area("Result", extracted_text, height=300)
    else:
        st.info("No text was extracted or an error occurred.")

else:

    st.info("Please upload an image to get started.")
