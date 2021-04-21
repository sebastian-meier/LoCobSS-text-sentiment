import logging
logging.basicConfig()
logging.root.setLevel(logging.ERROR)

import json

import sys

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sid = SentimentIntensityAnalyzer()

# load text file
textfile_path = sys.argv[1]
textfile = json.load(open(textfile_path, "r"))

results_question = []
results_description = []
resultsfile_path = sys.argv[2]

for text in textfile:
  out = []
  
  lines_list = tokenize.sent_tokenize(text['question_en'][0])
  for sentence in lines_list:
    ss = sid.polarity_scores(sentence)
    out.append(ss)

  results_question.append(json.dumps(out))

  out = []

  description = ''
  if 'description_en' in text:
    description = text['description_en'][0]
  if 'description_alt_en' in text:
    description = text['description_alt_en'][0]
  
  if description != '':
    lines_list = tokenize.sent_tokenize(description)
    for sentence in lines_list:
      ss = sid.polarity_scores(sentence)
      out.append(ss)

    results_description.append(json.dumps(out))
  else:
    results_description.append(json.dumps([]))

# export as json-nd
with open(resultsfile_path + '/questions-sentiment.json-nd', "w") as outfile:
  outfile.write("\n".join(results_question))

with open(resultsfile_path + '/descriptions-sentiment.json-nd', "w") as outfile:
  outfile.write("\n".join(results_description))

