from langchain_community.vectorstores import Chroma

from config import CHROMA_DB_PATH


def create_vector_store(chunks, embedding_model):
    """
    Create a Chroma vector database
    and store document embeddings.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_PATH
    )

    return vector_store