# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Use separate step for dependencies to cache them
COPY requirements.txt requirements.txt

# Increase timeout and cache dependencies
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy application code after dependencies are installed
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
