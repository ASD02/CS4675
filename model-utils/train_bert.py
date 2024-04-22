import torch
import pandas as pd
import numpy as np
from matplotlib import text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from transformers import TrainingArguments, Trainer
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import EarlyStoppingCallback
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from sklearn.model_selection import train_test_split


path_fake = "./Fake.csv"
path_true = "./True.csv"
path_opinions = "./extracted_texts.csv"

fake_news = pd.read_csv(path_fake).drop('date', axis=1)
true_news = pd.read_csv(path_true).drop('date', axis=1)
opinions = pd.read_csv(path_opinions)
fake_news = fake_news[['text']]
true_news = true_news[['text']]
opinions = opinions[['text']]

fake_news.dropna(axis=0, how="any", subset = None, inplace=True)
true_news.dropna(axis=0, how="any", subset = None, inplace=True)
opinions.dropna(axis=0, how="any", subset = None, inplace=True)

fake_news["label"] = 1
opinions["label"] = 0
true_news["label"] = 2


full_news = pd.concat([fake_news, true_news, opinions])

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
train, test  = train_test_split(full_news, test_size=0.3 , shuffle = True , random_state= 42)
train = pd.DataFrame(train)
test = pd.DataFrame(test)


train = pd.DataFrame(train)
test = pd.DataFrame(test)

train_text = list(train['text'])
test_text = list(test['text'])
tokenize_train = tokenizer(train_text, padding=True, truncation=True, max_length=512)
tokenize_test = tokenizer(test_text, padding=True, truncation=True, max_length=512)

train_labels = list(train['label'])
test_labels = list(test['label'])

class Dataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels=None):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        if self.labels:
            item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.encodings["input_ids"])


train_dataset = Dataset(tokenize_train, train_labels)
test_dataset = Dataset(tokenize_test, test_labels)

bert_model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", return_dict=True, num_labels =3)
freeze_layer_count = 11
if freeze_layer_count:
	      # We freeze here the embeddings of the model
        for param in bert_model.bert.embeddings.parameters():
            param.requires_grad = False

        if freeze_layer_count != -1:
	          # if freeze_layer_count == -1, we only freeze the embedding layer
	          # otherwise we freeze the first `freeze_layer_count` encoder layers
            for layer in bert_model.bert.encoder.layer[:11]:
                for param in layer.parameters():
                    param.requires_grad = False
            for layer in bert_model.bert.encoder.layer[11:12]:
                for param in layer.parameters():
                    param.requires_grad = True


args = TrainingArguments(
    output_dir="./bert-output",
    evaluation_strategy="steps",
    eval_steps=500,
    per_device_train_batch_size=10,
    per_device_eval_batch_size=10,
    num_train_epochs=5,
    seed=0,
    load_best_model_at_end=True,
)

def compute_metrics(p):
    pred, labels = p
    pred = np.argmax(pred, axis=1)

    accuracy = accuracy_score(y_true=labels, y_pred=pred)
    recall = recall_score(y_true=labels, y_pred=pred, average="weighted")
    precision = precision_score(y_true=labels, y_pred=pred, average="weighted")
    f1 = f1_score(y_true=labels, y_pred=pred, average="weighted")

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}

trainer = Trainer(
    model=bert_model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)])

#trainer.train()

# Load trained model
model_path = "./bert-output/checkpoint-2000"
model = BertForSequenceClassification.from_pretrained(model_path, num_labels=3)

# Define test trainer
test_trainer = Trainer(model)

# Make prediction
raw_pred, _, _ = test_trainer.predict(test_dataset)

y_pred = np.argmax(raw_pred, axis=1)
c = pd.DataFrame(y_pred)
c.to_csv("./results/result.txt", index= False, encoding='UTF-8')

accuracy = accuracy_score(y_true=test['label'], y_pred=y_pred)
recall = recall_score(y_true=test['label'], y_pred=y_pred, average="weighted")
precision = precision_score(y_true=test['label'], y_pred=y_pred, average="weighted")
f1 = f1_score(y_true=test['label'], y_pred=y_pred, average="weighted")
print("accuracy =",accuracy*100)
print("recall =", recall*100)
print("precision =", precision*100)
print("F1 score =", f1*100)
1
