# Use Python 3.11 slim image
FROM python:3.12-slim

# Make Python output immediately visible (unbuffered)
ENV PYTHONUNBUFFERED 1

# Set working directory inside container
WORKDIR /app

# Install system dependencies needed for Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libpq-dev \
       libssl-dev \
       libffi-dev \
       libjpeg-dev \
       zlib1g-dev \
       curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project code
COPY . /app/

RUN python manage.py collectstatic --noinput

# Expose the port Django will run on
EXPOSE 8000

# Default command to run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]