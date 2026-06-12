from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embedding_model

def create_vector_store(chunks):

    embeddings = get_embedding_model()

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store