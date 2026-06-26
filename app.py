import streamlit as st

from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_text
from utils.rag_pipeline import create_vector_store
from utils.retriever import search_documents
from utils.llm import get_answer

st.set_page_config(page_title="Enterprise Document Analytics Pipeline")

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

    # Create vector store
    vector_store = create_vector_store(chunks)

    st.success("Vector Store Created Successfully!")

    # Ask question
    query = st.text_input("Ask a question about the document")

    if query:

        docs = search_documents(
            vector_store,
            query
        )

        st.subheader("Retrieved Chunks")

        for i, doc in enumerate(docs, start=1):
            st.write(f"Chunk {i}")
            st.write(doc.page_content)
            st.write("---")

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        answer = get_answer(
            context,
            query
        )

        st.subheader("Answer")
        st.write(answer)

    st.subheader("Extracted Text")
    st.text_area(
        "PDF Content",
        text,
        height=300
    )

    st.subheader("Number of Chunks")
    st.write(len(chunks))

    if chunks:
        st.subheader("First Chunk")
        st.write(chunks[0])