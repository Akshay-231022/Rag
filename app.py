from loaders.document_loader import load_documents
from splitter.text_splitter import split_documents

documents = load_documents()
chunks = split_documents(documents)

print("=" * 70)
print(f"Documents Loaded : {len(documents)}")
print(f"Chunks Created   : {len(chunks)}")
print("=" * 70)

for i, chunk in enumerate(chunks[:3]):  # Show only first 3 chunks
    print(f"\nChunk {i + 1}")
    print("-" * 70)
    print(f"Source : {chunk.metadata.get('source')}")
    print(f"Page   : {chunk.metadata.get('page')}")
    print("\nContent:")
    print(chunk.page_content)