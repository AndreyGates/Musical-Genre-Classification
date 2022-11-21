# Get the Fast API image with Python version 3.9
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Create the directory for the container
WORKDIR /app
COPY requirements.txt ./requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install -Iv pywin32==305

# Copy scripts to make app.py work
COPY scripts ./scripts

# Copy FastAPI root
COPY app.py ./

# Copy the classification model
COPY model/CnnModel.pt ./model/CnnModel.pt

# Run by specifying the host and port
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]