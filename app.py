# Load the libraries
import shutil
from fastapi import FastAPI, HTTPException, UploadFile, File
from scripts.music_dealer import MusicDealer # Docker cannot process librosa library
from scripts.models import CnnModel
from scripts.Paras import ParaSetting

# Initialize an instance of FastAPI
app = FastAPI()

# Define the default route 
@app.get("/")
def root():
    return {"message": "Welcome to Your Music Genre Classification FastAPI"}

# Define the route to the music genre classifier
@app.post("/predict_genre")
async def predict_genre(audio_file: UploadFile = File(...)):
    if(not(audio_file)):
        raise HTTPException(status_code=400, 
                            detail = "Please provide an MP3 audiofile")

    with open('test/test.mp3', 'wb') as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    #audio_path = audio_file.filename
    audio_path = 'test/test.mp3'

    # load the model
    dealer = MusicDealer("model/CnnModel.pt", CnnModel())
    genre_scores = dealer.get_genre(audio_path)
        
    return {
            "audio_file": audio_path, 
            "music_genre": ParaSetting().dictionary[genre_scores[0]]
           }