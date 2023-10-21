FROM python:3.10-alpine

# Install curl in the Alpine
RUN apk add --no-cache curl

# Create a user to run the app
RUN adduser -D user_app
USER user_app

# Set environment variables
ENV APP_PATH=/app \
    PATH=$PATH:/home/user_app/.local/bin \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONPATH="${PYTHONPATH}:${APP_PATH}"

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy pyproject.toml and poetry.lock files
WORKDIR /temp
COPY pyproject.toml poetry.lock ./

# Install dependencies using poetry
USER root
RUN poetry install --no-dev

# Copy the app
USER user_app
WORKDIR $APP_PATH
COPY . .
