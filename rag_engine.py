import os
import numpy as np
from sentence_transformers import SentenceTransformer


# ---------------------------------------------------
# Load an embedding model
# This model converts text into numerical vectors
# so we can compare similarity between texts.
# ---------------------------------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")


# ---------------------------------------------------
# STEP 1: Load all knowledge documents
# This reads all .txt files inside the knowledge_base
# folder and stores them as a list of documents.
# ---------------------------------------------------
def load_documents():

    documents = []

    folder_path = "knowledge_base"

    # FIX: prevent crash if folder does not exist
    if not os.path.exists(folder_path):
        return ["No knowledge base available."]

    for file in os.listdir(folder_path):

        if file.endswith(".txt"):

            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:

                documents.append(f.read())

    return documents


# ---------------------------------------------------
# Load the documents once when the system starts
# ---------------------------------------------------
documents = load_documents()


# ---------------------------------------------------
# STEP 2: Convert documents into embeddings
# Embeddings are vectors that represent the meaning
# of each document.
# ---------------------------------------------------
doc_embeddings = model.encode(documents, normalize_embeddings=True)


# ---------------------------------------------------
# STEP 3: Retrieve the most relevant knowledge
# based on the user's question.
# ---------------------------------------------------
def retrieve_relevant_chunks(question, top_k=3):

    # Convert the question into an embedding
    query_embedding = model.encode([question], normalize_embeddings=True)[0]

    # Compute cosine similarity between question
    # and all knowledge documents
    similarities = np.dot(doc_embeddings, query_embedding) / (
        np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(query_embedding)
    )

    # Get indices of the top_k most similar documents
    top_indices = np.argsort(similarities)[-top_k:][::-1]

    # Return the corresponding documents
    relevant_docs = [documents[i] for i in top_indices]

    return "\n\n".join(relevant_docs)