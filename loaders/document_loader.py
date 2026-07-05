from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader


def load_documents():
    """
    Load all PDF files from the requirements folder.
    """

    loader = DirectoryLoader(
        path="data/requirements",
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
   
    documents = loader.load()

    return documents