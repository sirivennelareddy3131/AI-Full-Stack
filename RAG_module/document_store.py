from sentence_transformers import SentenceTransformer
import chromadb
with open("fest_info.txt","r",encoding="utf-8") as f:
    text=f.read()
print(f"Your file has {len(text)} characters.")
print()
print("Sample Text:",text[:300])
def chunk_text(text,chunk_size=270,overlap=40):
    chunks=[]
    start=0
    while start<len(text):
        chunks.append(text[start:start+chunk_size])
        start+=chunk_size-overlap
    return chunks
print() 
chunks=chunk_text(text)

model=SentenceTransformer('all-MiniLM-L6-V2')
embeddings=model.encode(chunks)

client=chromadb.PersistentClient(path="chroma_db")
collection=client.get_or_create_collection(name="fest_docs")

collection.upsert(
    ids=[f"chunk_{i}"for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings
)

# results=collection.query(question_embedding= q_embeddings ,n_results=2)
# print()
# print("Result 1:",results["documents"][0])
# print("Result 2:",results["documents"])

print(f"Total {collection.count()} number of document stored in db named fest_docs")

# for i in range(len(embeddings)):
#     print(f"Chunk_{i+1}: chunks[i]")
#     print(f"emb+{i+1}:{embeddings[i][:5]}")
#     print()
#     print("---------------------")

# print(f"Total {len(embeddings)} embeddings created.Shape of embeddings:{embeddings.shape}")
# embeddings:{embeddings.shape}
# print()

# for i in range(len(chunks)):
#     print(f"chunk+{i+1}:{chunks[i][:5]}")
#     print()
#     print("---------------------")