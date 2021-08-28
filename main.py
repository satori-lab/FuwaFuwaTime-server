from fastapi import FastAPI, File, UploadFile
from detoxify import Detoxify
from pydantic import BaseModel

from recognize import convert_speech_to_text

class DetectText(BaseModel):
    text: str

app = FastAPI()

# model = Detoxify('multilingual')
@app.post("/")
def root(file: UploadFile = File(...)):
    print(file)
    print(file.filename)
    print(file.file)
    google_res = convert_speech_to_text(file.file)
    if google_res:
        return google_res
        # return _detect_toxic(google_res)
    else:
        return 500

@app.get("/health")
def health():
    return {"status": "ok"}

# def _detect_toxic(detect_text: DetectText):
#     results = model.predict(detect_text.text)
#     print(results)
#     return {"toxicity": float(results["toxicity"])}
