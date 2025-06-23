FROM python:3.10-slim

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy app files
COPY . .

# Install Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 10000

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
