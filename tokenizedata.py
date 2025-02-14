import json
from transformers import AutoTokenizer

# ✅ Load the tokenizer (update path if needed)
model_path = "models/opt-1.3b"
tokenizer = AutoTokenizer.from_pretrained(model_path)

# ✅ Load the formatted dataset (Updated to use the correct input file)
input_file = "datasets/cleaned_merged_data.jsonl"
output_file = "datasets/opt_tokenized.jsonl"

tokenized_data = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line.strip())  # Ensure each line is correctly parsed
            if "input" not in data:
                continue  # Skip entries that don't have an "input" field

            # ✅ Tokenize the "input" text
            tokenized = tokenizer(
                data["input"],
                padding="max_length",
                truncation=True,
                max_length=512,
                return_tensors="pt"
            )

            # ✅ Convert tokenized data to a serializable format
            tokenized_entry = {
                "input_ids": tokenized["input_ids"].tolist()[0],  # Convert tensor to list
                "attention_mask": tokenized["attention_mask"].tolist()[0],  # Convert tensor to list
                "context": data.get("context", ""),
                "source": data.get("source", ""),
            }
            tokenized_data.append(tokenized_entry)
        except json.JSONDecodeError as e:
            print(f"Skipping malformed line: {e}")

# ✅ Save tokenized data
with open(output_file, "w", encoding="utf-8") as f:
    for item in tokenized_data:
        json.dump(item, f)
        f.write("\n")

print(f"✅ Tokenized dataset saved: {output_file}")

