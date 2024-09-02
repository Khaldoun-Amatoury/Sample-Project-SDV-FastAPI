
# from dotenv import load_dotenv
# load_dotenv()
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd
from io import StringIO
from sdv_handler import SDVHandler
import os
import uvicorn

# port = os.getenv('PORT')


app = FastAPI()

class GenerateDataRequest(BaseModel):
    num_rows: int
    model_type: str

class EvaluationResult(BaseModel):
    evaluation_score: float
    generated_data: list  


@app.post("/generate_synthetic_data/", response_model=EvaluationResult)
async def generate_synthetic_data(request: GenerateDataRequest):
    sdv_handler = SDVHandler()
    num_rows = request.num_rows
    model_type = request.model_type
    generated_data = sdv_handler.generate_data(num_rows, model_type)
    evaluation_score = sdv_handler.generate_quality_report(generated_data)
    return {
        "evaluation_score": evaluation_score,
        "generated_data": generated_data.to_dict(orient="records")
    }

@app.post("/upload_data/")
async def upload_data(file: UploadFile = File(...)):
    data_path = os.path.join(os.getcwd(), "..",  "data", "uploaded_data.csv")
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode("utf-8")))
    df.to_csv(data_path, index=False)
    return {"status": "Data uploaded successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6000)
    # uvicorn.run(app, host="0.0.0.0", port=port)