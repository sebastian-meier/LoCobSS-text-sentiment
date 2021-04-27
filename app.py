import logging
logging.basicConfig()
logging.root.setLevel(logging.ERROR)

import json

from flask import Flask
from flask_restful import Api, Resource, reqparse
from flasgger import Swagger

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

import os
from dotenv import load_dotenv
load_dotenv()

sid = SentimentIntensityAnalyzer()

app = Flask(__name__)
app.config['DEBUG'] = False

swagger = Swagger(app)

@app.route('/')
def root():
  """Default endpoint for testing
    ---
    produces:
      - text/plain
    responses:
      200:
        description: Service is alive
        examples:
          text/plain: Hello
  """
  return 'Hello', 200

@app.route('/predict', methods=['POST'])
def predict():
  """Endpoint for generating sentiment predictions for a text.
    ---
    parameters:
      - name: text
        type: string
        required: true
    definitions:
      Sentiment:
        type: object
        properties:
          neg: 
            type: float
          neu: 
            type: float
          pos: 
            type: float
          compund: 
            type: float
      Sentiments:
        type: array
        items:
          $ref: '#/definitions/Sentiment'
    responses:
      400:
        description: Text parameter missing
      200:
        description: List of sentiments
        schema:
          $ref: '#/definitions/Sentiments'
        examples: 
          application/json: [{'neg': 0.54, 'neu': 0.46, 'pos': 0.0, 'compound': -0.69}]
  """

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