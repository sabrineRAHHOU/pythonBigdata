from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn
import sklearn


#définir FastAPI
app = FastAPI()
model = joblib.load("finalResult.pkl")

#on fait une classe de modéle pour faciliter les appels des objets
class Tweet(BaseModel):
    tweet = str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/dataTweet/{tweet}")
def get_offensive_language(tweet): 
    if (tweet) :
        Y_pred = model.predict_proba([tweet])[0]

        if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
            return("hate_speech")
        elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2]:
            return("offensive_language")
        else :
            return("neither")

