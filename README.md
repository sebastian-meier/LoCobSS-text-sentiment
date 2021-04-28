This repo is part of the LoCobSS research project. More details about the project and dependencies to other repos can be found [here](https://github.com/sebastian-meier/LoCobSS-documentation).

# LoCobSS-text-sentiment
Setup tested and deployed on Google Cloud Run

## Functionality
This service takes a string (param *text*) peforms tokenization to split it into sequences. For each sequence the *polarity_scores* from NLTK's [nltk.sentiment.vader](https://www.nltk.org/api/nltk.sentiment.html?highlight=vader#module-nltk.sentiment.vader)'s SentimentIntensityAnalyzer is being generated and returned as an array.

## Local Setup
.env file
```
GOOGLE_APPLICATION_CREDENTIALS=
```
see: https://cloud.google.com/docs/authentication/production

Install requirements using `requirements.txt`.

Execute on port 5050:
```bash
gunicorn --bind :5050 --workers 1 --threads 8 --timeout 0 app:app
```

If you want to quickly check if the system is running:
```bash
python test.py
```

## API Documentation
The API is documented using flasgger/swagger. When running the API, simply go to localhost:5050/apidocs

## Deployment
This repo already contains a folder nltk_data, which contains the required models for the sentiment analysis. This makes sure that the stateless container does not need to load that data upon initialisation and, therefore, be more responsive and faster.

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/BUILD_NAME
gcloud run deploy --image gcr.io/YOUR_PROJECT/BUILD_NAME --platform managed
```

## Running local batch
If you already have a lot of text and you want to process it, before setting up the cloud service. The `batch.py` file allows you to process a text file. Each text-snippet should be line-sepparated. The output is a json-nd file with corresponding line-separated output. Call it like this:

```bash
python batch.py YOUR_TEXTFILE.txt OUTPUT_FILE.json-nd
```
