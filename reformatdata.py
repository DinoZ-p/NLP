import json

input_file = "datasets/merged_data.jsonl"
output_file = "datasets/cleaned_merged_data.jsonl"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        try:
            entry = json.loads(line)  # Parse JSON line
            json.dump(entry, outfile, ensure_ascii=False)  # Write cleaned JSON
            outfile.write("\n")  # Ensure newline separation
        except json.JSONDecodeError as e:
            print(f"❌ Skipping malformed JSON line: {line} (Error: {e})")  # Debugging

print(f"✅ Cleaned JSONL format saved to {output_file}")

