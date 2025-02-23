FROM python:3.9-slim

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app

# Expose port for Django
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]