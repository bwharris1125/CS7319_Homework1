# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /src

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8000 for the API
EXPOSE 5000

# Start the API
CMD ["python3", "src/simple_api.py"]