import json

input_file = "datasets/cleaned_merged_data.jsonl"
output_file = "datasets/fixed_cleaned_data.jsonl"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)  # This will load the entire JSON array

# Convert it into JSONL format
with open(output_file, "w", encoding="utf-8") as f:
    for entry in data:
        f.write(json.dumps(entry) + "\n")  # Write each object in JSONL format

print(f"✅ Fixed JSONL format saved to {output_file}")

