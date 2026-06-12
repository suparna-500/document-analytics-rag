import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_text

st.title("Enterprise Document Analytics Pipeline")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    # Extract text from PDF
    text = extract_text_from_pdf(uploaded_file)

    # Split text into chunks
    chunks = split_text(text)

    # Show extracted text
    st.subheader("Extracted Text")
    st.text_area(
        "PDF Content",
        text,
        height=300
    )

    # Show chunk information
    st.subheader("Number of Chunks")
    st.write(len(chunks))

    # Show first chunk
    st.subheader("First Chunk")
    st.write(chunks[0])