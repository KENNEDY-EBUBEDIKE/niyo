FROM ubuntu:22.04
RUN apt update && apt-get install -y tzdata && apt install -y python3.10 python3-pip
RUN apt install -y python3-dev libpq-dev postgresql-client

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose ports for Gunicorn and Daphne
EXPOSE 8000
EXPOSE 8001

# Create an entrypoint script to run both servers
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh


# Set the entrypoint script as the container's entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
