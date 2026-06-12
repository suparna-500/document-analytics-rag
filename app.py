import streamlit as st

from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_text
from utils.rag_pipeline import create_vector_store
from utils.retriever import search_documents
from utils.llm import get_answer

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

    # Create FAISS vector store
    vector_store = create_vector_store(chunks)

    query = st.text_input(
    "Ask a question about the document"
)

if query:

    docs = search_documents(
        vector_store,
        query
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    answer = get_answer(
        context,
        query
    )

    st.subheader("Answer")

    st.write(answer)
    st.success("Vector Store Created Successfully!")

    # Display extracted text
    st.subheader("Extracted Text")

    st.text_area(
        "PDF Content",
        text,
        height=300
    )

    # Display chunk information
    st.subheader("Number of Chunks")
    st.write(len(chunks))

    # Display first chunk
    st.subheader("First Chunk")
    st.write(chunks[0])