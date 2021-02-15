FROM python:3.6-slim-buster

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

ENV NLTK_DATA ./nltk_data

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader vader_lexicon -d nltk_data
RUN python -m nltk.downloader punkt -d nltk_data

# CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:$PORT", "app:app"]
# EXPOSE $PORT

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app