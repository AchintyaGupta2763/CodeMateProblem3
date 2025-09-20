# config.py
MONGODB_URI = "mongodb://localhost:27017"
DB_NAME = "deep_researcher"
VECTOR_COLLECTION = "embeddings"
EMBEDDING_DIM = 768  # adjust according to your embedding model
TTL_SECONDS = 3600  # auto-delete after 1 hour
