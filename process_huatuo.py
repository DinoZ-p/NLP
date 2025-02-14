import json

# ✅ Load Huatuo QA data (JSONL format)
input_file = "datasets/huatuo_encyclopedia_qa/train_datasets.jsonl"
output_file = "datasets/huatuo_data.txt"

formatted_huatuo = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            entry = json.loads(line.strip())  # Read line-by-line
            question = entry.get("question", "No question available.")
            answer = entry.get("answer", "No answer available.")
            formatted_huatuo.append(f"Q: {question}\nA: {answer}")
        except json.JSONDecodeError:
            continue  # Skip lines that are not valid JSON

# ✅ Save processed data
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines("\n\n".join(formatted_huatuo))

print(f"✅ Huatuo Encyclopedia QA processed and saved as '{output_file}'")

