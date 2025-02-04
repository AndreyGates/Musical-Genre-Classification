# Get the Fast API image with Python version 3.9
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Create the directory for the container
WORKDIR /app

# Copy the dependencies list
COPY requirements.txt ./requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Specially for Librosa
RUN apt-get -y update && apt install -y libsndfile1
RUN apt-get -y update && apt install -y ffmpeg

# Copy scripts, templates, static and test to make app.py work
COPY scripts ./scripts
COPY templates ./templates
COPY static ./static
COPY test ./test

# Copy FastAPI root
COPY app.py ./

# Copy the classification model
COPY model/CnnModel.pt ./model/CnnModel.pt

# Run by specifying the host and port
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]