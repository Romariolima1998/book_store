# Use a Python base image
FROM python:3.8.15-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Prepend venv to PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Set working directory
WORKDIR $PYSETUP_PATH

# Install dependencies
RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# Change to the application's directory
WORKDIR /app

# Copy the application code
COPY . /app/

# Expose the port if your application needs it
EXPOSE 8000

# Define the command to run on container start using Gunicorn
CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000"]