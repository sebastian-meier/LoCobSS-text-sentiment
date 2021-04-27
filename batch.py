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
textfile = open(textfile_path, "r")
textlines = [line for line in textfile.readlines()]
textfile.close()

results = []
resultsfile_path = sys.argv[2]

for text in textlines:
  out = []
  
  lines_list = tokenize.sent_tokenize(text)
  for sentence in lines_list:
    ss = sid.polarity_scores(sentence)
    out.append(ss)

  results.append(json.dumps(out))

  out = []

# export as json-nd
with open(resultsfile_path, "w") as outfile:
  outfile.write("\n".join(results))
