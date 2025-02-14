import os
import json
import xml.etree.ElementTree as ET

# Paths
pubmed_path = "datasets/"
huatuo_path = "datasets/huatuo_data.txt"
output_file = "datasets/merged_data.jsonl"

# ✅ Load Huatuo data
with open(huatuo_path, "r", encoding="utf-8") as f:
    huatuo_data = f.readlines()

formatted_data = []

# ✅ Process PubMed XML files
for file in sorted(os.listdir(pubmed_path)):
    if file.endswith(".xml"):
        file_path = os.path.join(pubmed_path, file)
        tree = ET.parse(file_path)
        root = tree.getroot()

        for article in root.findall(".//PubmedArticle"):
            abstract = article.find(".//AbstractText")
            title = article.find(".//ArticleTitle")

            if abstract is not None and title is not None:
                formatted_data.append({
                    "input": f"Title: {title.text}\nAbstract: {abstract.text}",
                    "context": "PubMed",
                    "source": file
                })

# ✅ Process Huatuo Q&A
for entry in huatuo_data:
    formatted_data.append({
        "input": entry.strip(),
        "context": "Huatuo",
        "source": "huatuo_encyclopedia"
    })

# ✅ Save merged data
with open(output_file, "w", encoding="utf-8") as f:
    for item in formatted_data:
        json.dump(item, f)
        f.write("\n")

print(f"✅ Merged dataset saved to: {output_file}")

