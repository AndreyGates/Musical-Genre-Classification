# Load the libraries
import shutil
from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from scripts.music_dealer import MusicDealer # Docker cannot process librosa library
from scripts.models import CnnModel
from scripts.Paras import ParaSetting

# Initialize an instance of FastAPI
app = FastAPI()

# Define templating for a web app
templates = Jinja2Templates(directory='templates/')

# Define the default route 
@app.get("/")
def root():
    return {"message": "Welcome to Your Music Genre Classification FastAPI"}

# Define the initial submission form route
@app.get("/form", response_class=HTMLResponse)
def form_post(request: Request):
    result = "Send a track"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# Define the route to the music genre classifier
@app.post("/form", response_class=HTMLResponse)
async def form_post(request: Request, file: UploadFile = File(...)):
    if(not(file)):
        raise HTTPException(status_code=400, 
                            detail = "Please provide an MP3 audiofile")

    with open('test/test.mp3', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    #audio_path = file.filename
    audio_path = 'test/test.mp3'

    # load the model
    dealer = MusicDealer("model/CnnModel.pt", CnnModel())
    genre_scores = dealer.get_genre(audio_path)
        
    result = {
                "audio_file": audio_path, 
                "music_genre": ParaSetting().dictionary[genre_scores[0]]
             }

    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})