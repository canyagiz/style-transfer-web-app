import uuid
import cv2
import numpy as np
from PIL import Image
import uvicorn
from fastapi import File, FastAPI, UploadFile

import config
import inference


app = FastAPI()


@app.get("/")
def read_root():
    return{"message":"Welcome from the API"}

@app.post("/{style}")
async def get_image(style:str, file:UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    model = config.STYLES[style]
    output, resized = inference.inference(model=model, image=image)
    name = f"/storage/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(name, output)

    return {"name": name}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)