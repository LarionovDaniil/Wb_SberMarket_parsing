import numpy as np
import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment', return_dict=True)

@torch.no_grad()
def predict(text):
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.sigmoid(outputs.logits)
    predicted = torch.argmax(predicted, dim=1).numpy()
    return predicted


def rating(reviews):
    predictions = predict(reviews)
    positive = np.where(predictions == 1)[0]
    negative = np.where(predictions == 2)[0]
    neutral = np.where(predictions == 0)[0]
    length = predictions.size

    return positive, negative, neutral, length

