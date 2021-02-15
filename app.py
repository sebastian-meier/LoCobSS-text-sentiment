import logging
logging.basicConfig()
logging.root.setLevel(logging.ERROR)

import json

from flask import Flask
from flask_restful import Api, Resource, reqparse

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

import os
from dotenv import load_dotenv
load_dotenv()

sid = SentimentIntensityAnalyzer()

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/')
def root():
  return 'Hello', 200

@app.route('/predict', methods=['POST'])
def predict():
  parser = reqparse.RequestParser()
  parser.add_argument('text')
  args = parser.parse_args()

  text = args["text"]

  if text == None or len(text) <= 0:
    return "Text parameter missing.", 400

  lines_list = tokenize.sent_tokenize(text)

  out = []

  for sentence in lines_list:
    ss = sid.polarity_scores(sentence)
    out.append(ss)

  return json.dumps(out), 200

if __name__ == "__main__":
  # use 0.0.0.0 to use it in container
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))