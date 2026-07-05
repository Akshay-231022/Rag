"""
rag_chain.py

Creates the complete RAG pipeline.
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def create_rag_chain(retriever, prompt, llm):
    """
    Create the complete Retrieval-Augmented Generation chain.
    """

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain