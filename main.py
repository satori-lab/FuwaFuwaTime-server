from fastapi import FastAPI
from detoxify import Detoxify
from pydantic import BaseModel

from recognize import convert_speech_to_text

class DetectText(BaseModel):
    text: str

app = FastAPI()

# model = Detoxify('multilingual')
@app.post("/")
def root(wav_path: str):
    google_res = convert_speech_to_text(wav_path)
    if google_res:
        return google_res
        # return _detect_toxic(google_res)
    else:
        return 500

@app.get("/helth")
def root():
    return 'OK'

@app.get("/")
def root():
    return 'OK'

# def _detect_toxic(detect_text: DetectText):
#     results = model.predict(detect_text.text)
#     print(results)
#     return {"toxicity": float(results["toxicity"])}
