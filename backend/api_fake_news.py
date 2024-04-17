import sys
from transformers import BertTokenizer, BertForSequenceClassification
import torch


def classification_news(news, model_path):
    # Load the model and tokenizer
    model = BertForSequenceClassification.from_pretrained(model_path, num_labels=3)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    model.eval()  # Put the model in evaluation mode

    inputs = tokenizer(news, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    print("The outputs are: " + str(logits) + "\n")
    if predictions[0] == 2:
        classification = 'True'
    elif predictions[0] == 1:
        classification = 'Fake'
    else:
        classification = 'Opinion'
    return classification


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <model_path> <news>")
        sys.exit(1)

    model_path = sys.argv[1]
    news = sys.argv[2]

    classification = classification_news(news, model_path)
    print(f'{classification}')
