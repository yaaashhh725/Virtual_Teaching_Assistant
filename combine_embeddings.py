import numpy as np

# Load the two files
cc = np.load("teaching_assistant_embeddings.npz", allow_pickle=True)
df = np.load("discourse.npz", allow_pickle=True)

# Concatenate arrays
chunks = np.concatenate([cc['chunks'], df['chunks']])
embeddings = np.concatenate([cc['embeddings'], df['embeddings']])
metadata = np.concatenate([cc['metadata'], df['metadata']])

# Save combined
np.savez_compressed(
    "final_embeddings.npz",
    chunks=chunks,
    embeddings=embeddings,
    metadata=metadata
)

print(f"Combined {len(chunks)} chunks into final_embeddings.npz")