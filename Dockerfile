# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.11
# FROM python:3.10-slim
# FROM python:3.11-bullseye
FROM python:3.11-bullseye

ENV PORT 8000
EXPOSE 8000


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install build-essential libreoffice pandoc -y
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt && python -m pip install gunicorn

COPY . /app

RUN chown -R appuser /app
USER appuser

WORKDIR /app

# Collect static files
RUN python manage.py collectstatic --noinput

# get nltk data see https://github.com/Unstructured-IO/unstructured/issues/1080
ENV NLTK_DATA /home/appuser/nltk_data

RUN python -c "import nltk; nltk.download('punkt')" && \
  python -c "import nltk; nltk.download('averaged_perceptron_tagger')"

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "600","--workers", "10", "quickstartproject.wsgi"]
