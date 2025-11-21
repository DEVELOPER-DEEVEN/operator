from google.cloud import firestore
import json

class VectorStore:
    def __init__(self):
        try:
            self.db = firestore.Client()
            self.available = True
        except:
            self.available = False
            print("Firestore not available for VectorStore")

    def store_experience(self, prompt, action, result):
        if not self.available:
            return

        # In a real implementation, we would generate an embedding for the prompt here
        # embedding = generate_embedding(prompt)
        
        doc_data = {
            "prompt": prompt,
            "action": action,
            "result": result,
            # "embedding": embedding # Vector field
        }
        
        try:
            self.db.collection("experiences").add(doc_data)
        except Exception as e:
            print(f"Failed to store experience: {e}")

    def find_similar(self, prompt, limit=3):
        if not self.available:
            return []

        # In a real implementation, this would be a vector similarity search
        # query = self.db.collection("experiences").find_nearest(
        #    vector_field="embedding",
        #    query_vector=generate_embedding(prompt),
        #    distance_measure=firestore.DistanceMeasure.COSINE,
        #    limit=limit
        # )
        
        # Fallback: Simple text match or recent items for demo
        try:
            docs = self.db.collection("experiences").limit(limit).stream()
            return [doc.to_dict() for doc in docs]
        except Exception as e:
            print(f"Failed to retrieve experiences: {e}")
            return []
