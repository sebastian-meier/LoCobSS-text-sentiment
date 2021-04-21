# LoCobSS-text-sentiment
Setup tested and deployed on Google Cloud Run

## Local Setup
.env file
```
GOOGLE_APPLICATION_CREDENTIALS=
```
see: https://cloud.google.com/docs/authentication/production

Install requirements using `requirements.txt`.

## Deployment
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/BUILD_NAME
gcloud run deploy --image gcr.io/YOUR_PROJECT/BUILD_NAME --platform managed
```

## Running local batch
If you already have a lot of text and you want to process it, before setting up the cloud service. The `batch.py` file allows you to process a text file. Each text-snippet should be line-sepparated. The output is a json-nd file with corresponding line-separated output. Call it like this:

```bash
python batch.py YOUR_TEXTFILE.txt OUTPUT_FILE.json-nd
```