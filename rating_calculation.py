# from dostoevsky.tokenization import RegexTokenizer
# from dostoevsky.models import FastTextSocialNetworkModel

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

# rate = {0:'NEUTRAL', 1:'POSITIVE', 2:'NEGATIVE'}
# print(reviews_kirill_only)

def rating(reviews):
    predictions = predict(reviews)
    positive = np.count_nonzero(predictions == 1)
    negative = np.count_nonzero(predictions == 2)
    neutral = np.count_nonzero(predictions == 0)
    length = predictions.size

    return positive,negative,neutral,length

# 44 с
