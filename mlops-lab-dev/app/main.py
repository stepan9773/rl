from fastapi import FastAPI

from app.config import settings
from app.models import RLInput, RLOutput
from app.rl import HuggingFaceModel

app = FastAPI(title=settings.APP_NAME)

model = HuggingFaceModel(
    model_name=settings.MODEL_NAME,
    repo_id=settings.HUGGINGFACE_REPO_ID,
    model_filename=settings.HUGGINGFACE_MODEL_FILENAME,
)


@app.post("/api/inference")
async def inference(input: RLInput) -> RLOutput:
    return {"action": model.predict(input)}
