from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY


def get_embedding_model():
    """
    Create and return the OpenAI embedding model.
    """

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY
    )

    return embeddings