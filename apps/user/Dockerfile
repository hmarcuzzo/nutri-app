FROM python:3.10-alpine

# Create a user to run the app
RUN adduser -D user_app
USER user_app

# Set environment variables
ENV APP_PATH=/app

ENV PATH=$PATH:/home/user_app/.local/bin \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="${PYTHONPATH}:${APP_PATH}"

# Install dependencies from pipenv
COPY Pipfile* /tmp/
RUN pip install pipenv && \
    cd /tmp && \
    pipenv install --system --deploy

# Copy the app
WORKDIR $APP_PATH
COPY . $APP_PATH
