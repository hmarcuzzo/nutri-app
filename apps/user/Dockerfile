FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Install dependencies from pipenv
COPY Pipfile* /tmp/
RUN pip install pipenv
RUN cd /tmp && pipenv install --system --deploy

# Copy the app
WORKDIR /app
COPY . /app
