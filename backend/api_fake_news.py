from transformers import BertTokenizer, BertForSequenceClassification
import torch

MODEL_PATH = 'bert-model'
# Load the model and tokenizer
model = BertForSequenceClassification.from_pretrained(MODEL_PATH, num_labels=3)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model.eval()  # Put the model in evaluation mode


def classify_text(news: str) -> int:
    inputs = tokenizer(news, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    classification = 0
    if predictions[0] == 2:
        classification = 1              # 'True'
    elif predictions[0] == 1:
        classification = -1              # 'Fake'
    else:
        classification = 0              # 'Opinion'
    return classification
