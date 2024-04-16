import argparse
from transformers import BertTokenizer, BertForSequenceClassification
import torch


def classification_news(news):
  # Load the model and tokenizer
  #model_path = "./bert-output/checkpoint-2500" #USED FOR LOCAL EXECUTION
  #model_path = "./checkpoint-2500"
  model_path = '/content/drive/MyDrive/bert-output/checkpoint-2500' # YOU MUST CHANGE THE PATH TO YOUR MODEL PATH

  model = BertForSequenceClassification.from_pretrained(model_path, num_labels=3)

  tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
  #model = BertForSequenceClassification.from_pretrained(model_path)

  model.eval() # Put the model in evaluation mode



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
"""
EXAMPLE OF USE  
classification = classification_news("Your news must go here")

print(f'The news is classified as: {classification}')"""