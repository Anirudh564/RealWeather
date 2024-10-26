# Use a base image with Python installed
FROM python:3.9-slim

# Set the working directory at the root of the app
WORKDIR /app

# Copy all application files into the container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Initialize the database
RUN python app/setup_database.py

# Run the application
CMD ["python", "main.py"]
