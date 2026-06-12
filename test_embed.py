from utils.embeddings import get_embedding_model

print("Loading model...")

embeddings = get_embedding_model()

print("Generating embedding...")

result = embeddings.embed_query("Hello world")

print("Success!")
print("Embedding length:", len(result))