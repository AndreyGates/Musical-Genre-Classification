# Load the libraries
import shutil
import os
from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from scripts.music_dealer import MusicDealer # Docker cannot process librosa library
from scripts.models import CnnModel
from scripts.Paras import ParaSetting

# Initialize an instance of FastAPI
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

# Define the default route 
#@app.get("/")
#def root():
    #return {"message": "Welcome to Your Music Genre Classification FastAPI"}

# Define the initial submission form route
@app.get("/", response_class=HTMLResponse)
def form_post(request: Request):
    result = "-"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# Define the route to the music genre classifier
@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, file: UploadFile = File(...)):
    if(not(file)):
        raise HTTPException(status_code=400, 
                            detail = "Please provide an MP3 audiofile")

    with open('test/test.mp3', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    cmd_str = f"ffmpeg -i {'test/test.mp3'} -ac 1 -ar {ParaSetting().sample_rate} {'test/test_resampled.mp3'}"
    print(cmd_str)
    os.system(cmd_str)

    audio_path = 'test/test_resampled.mp3'

    # load the model
    dealer = MusicDealer("model/CnnModel.pt", CnnModel())
    genre_scores = dealer.get_genre(audio_path)

    os.remove('test/test.mp3')
    os.remove('test/test_resampled.mp3')
        
    '''result = {
                "audio_file": audio_path, 
                "music_genre": ParaSetting().dictionary[genre_scores[0]]
             }'''
    result = ParaSetting().dictionary[genre_scores[0]]

    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})