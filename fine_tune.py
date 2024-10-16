import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import torch

# Load and preprocess data
def load_data(file_path):
    df = pd.read_csv(file_path)
    texts = df['text'].tolist()
    labels = df['sentiment'].tolist()
    return texts, labels

# Tokenize data
def tokenize_data(texts, tokenizer):
    return tokenizer(texts, padding=True, truncation=True, max_length=512)

# Prepare dataset
class SentimentDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Fine-tune model
def fine_tune_model(train_dataset, val_dataset, model_name, output_dir):
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
    
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        evaluation_strategy="epoch",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )

    trainer.train()
    trainer.save_model(output_dir)

def main():
    # Load data
    texts, labels = load_data('data/all_financial_sentiment_data.csv')

    # Split data
    train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2)

    # Tokenize data
    tokenizer = AutoTokenizer.from_pretrained("llama3.2:3b")
    train_encodings = tokenize_data(train_texts, tokenizer)
    val_encodings = tokenize_data(val_texts, tokenizer)

    # Create datasets
    train_dataset = SentimentDataset(train_encodings, train_labels)
    val_dataset = SentimentDataset(val_encodings, val_labels)

    # Fine-tune model
    fine_tune_model(train_dataset, val_dataset, "llama3.2:3b", "./fine_tuned_model")

if __name__ == "__main__":
    main()
