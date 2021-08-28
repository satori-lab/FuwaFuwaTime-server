from fastapi import FastAPI
from detoxify import Detoxify
from pydantic import BaseModel

class DetectText(BaseModel):
    text: str

app = FastAPI()

model = Detoxify('multilingual')
@app.post("/")
def detect_toxic(detect_text: DetectText):
    results = model.predict(detect_text.text)
    print(results)
    return {"toxicity": float(results["toxicity"])}
