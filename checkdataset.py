from datasets import load_from_disk
from collections import Counter

# Load dataset
dataset = load_from_disk("datasets/processed_with_labels")

# Count class distribution
labels = [x["labels"] for x in dataset]
class_counts = dict(Counter(labels))

# Print distribution
print(f"\n📊 Class Distribution: {class_counts}")

