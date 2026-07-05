# Rag
Complete RAG for Enterprise QA 

                    +----------------+
                    | Requirement PDFs|
                    | BRDs            |
                    | User Stories    |
                    | Jira Export     |
                    +--------+--------+
                             |
                             |
                       Document Loader      //from langchain_community.document_loaders import DirectoryLoader
                             |          
                             ▼
                  Text Extraction         // //from langchain_community.document_loaders import PyPDFLoader
                             |
                             ▼
                  Text Chunking           //from langchain.text_splitter import RecursiveCharacterTextSplitter
                             |
                             ▼
                  Embedding Model         //from langchain_openai import OpenAIEmbeddings
                             |
                             ▼
                  Vector Database         //from langchain_community.vectorstores 
                (Chroma/FAISS)            //import Chroma from config import CHROMA_DB_PATH
                             ▲
                             |
                Stored Embeddings        //from langchain_openai import OpenAIEmbeddings
------------------------------------------------------------

                Runtime (User Query)

                    User Question     //we can gradio or devlop some UI Interface with UI/UX angular along with fastAPI
                        |
                        ▼
                    Embedding Model
                        |
                        ▼
                    Vector Similarity Search
                        |
                        ▼
                    Top-K Relevant Chunks    
                        |
                        ▼
                    Prompt Template            ///from langchain.prompts import PromptTemplate
                    (Context + Question)
                        |
                        ▼
                       LLM                          //from langchain_openai import ChatOpenAI
                        |
                        ▼
                    Structured Response
-------------------------------------------------------------------
                            How LangChain Works

                            Retriever

                            +

                            Prompt

                            +

                            LLM

                            ↓

                            Chain
-------------------------------------------------------------------
requirement-testcase-rag
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── data
│   └── requirements
│       ├── Login.pdf
│       ├── Dashboard.pdf
│       ├── Counterparty.pdf
│       └── RiskLimit.pdf
│
├── loaders
│   └── document_loader.py
│
├── splitter
│   └── text_splitter.py
│
├── embeddings
│   └── embedding_model.py
│
├── vectordb
│   └── chroma_store.py
│
├── retriever
│   └── retriever.py
│
├── prompts
│   └── prompt_template.py
│
├── llm
│   └── llm_model.py
│
├── chains
│   └── rag_chain.py
│
├── output
│   └── generated_testcases.txt
│
└── utils
    └── helper.py