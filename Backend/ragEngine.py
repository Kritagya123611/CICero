import cohere
import os
import faiss
import numpy as np
import json
from dotenv import load_dotenv

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

# Create a vector index (Cohere uses 1024 dimensions)
index = faiss.IndexFlatL2(1024)
metadata = []

def embed_text(text):
    response = co.embed(
        texts=[text],
        model="embed-english-v3.0",
        input_type="search_document"  # <-- this fixes the error
    )
    return np.array(response.embeddings[0]).astype("float32")

def add_log_example(log_text, fix_text):
    vector = embed_text(log_text)
    index.add(np.array([vector]))
    metadata.append({"log": log_text, "fix": fix_text})

def search_similar(log_text, top_k=3):
    query_vec = embed_text(log_text)
    _, indices = index.search(np.array([query_vec]), top_k)
    return [metadata[i] for i in indices[0] if i < len(metadata)]

def load_rag_dataset(path="SampleLog/ragDataset.json"):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            add_log_example(item["log"], item["fix"])

# Load when file is run
load_rag_dataset()
