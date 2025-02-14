import os
import torch
import transformers
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForLanguageModeling

# ✅ Paths optimized for saving space
MODEL_PATH = "/root/NLP/models/opt-1.3b"
DATA_PATH = "/root/autodl-tmp/datasets/opt_train.jsonl"
DS_CONFIG_PATH = "/root/NLP/zero2.json"

# ✅ Storage paths to avoid system disk issues
OUTPUT_DIR = "/root/autodl-tmp/NLP_output"
LOG_DIR = "/root/autodl-tmp/NLP_logs"

# ✅ Ensure directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# ✅ Load Dataset
dataset = load_dataset("json", data_files={"train": DATA_PATH}, split="train")

# ✅ Load Tokenizer & Model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

# ✅ Data Collator (Ensures Proper Batching)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# ✅ Training Arguments (Fixed to Match DeepSpeed Config)
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=3e-5,  # 🔥 Matches DeepSpeed (auto)
    weight_decay=0.01,   # 🔥 Matches DeepSpeed (auto)
    save_strategy="epoch",
    save_total_limit=2,
    fp16=False,
    bf16=True,
    deepspeed=DS_CONFIG_PATH,  # ✅ Ensures consistency with DeepSpeed
    logging_dir=LOG_DIR,
    logging_steps=100,
    report_to="none",
    run_name="opt-1.3b-training",
    evaluation_strategy="no",
)

# ✅ Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# ✅ Start Training
trainer.train()

