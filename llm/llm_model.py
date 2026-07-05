"""
llm_model.py

This module initializes the OpenAI Chat Model.
"""

from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY
from config import MODEL_NAME


def get_llm():
    """
    Returns a configured OpenAI Chat Model.
    """

    llm = ChatOpenAI(
        model=MODEL_NAME,
        api_key=OPENAI_API_KEY,
        temperature=0
    )

    return llm