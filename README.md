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
                       Document Loader
                             |
                             ▼
                  Text Extraction
                             |
                             ▼
                  Text Chunking
                             |
                             ▼
                  Embedding Model
                             |
                             ▼
                  Vector Database
                (Chroma/FAISS)
                             ▲
                             |
                Stored Embeddings
------------------------------------------------------------

                Runtime (User Query)

                    User Question
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
                    Prompt Template
                    (Context + Question)
                        |
                        ▼
                    LLM
                        |
                        ▼
                    Structured Response
