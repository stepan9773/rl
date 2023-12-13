from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "MLOps Homework API contract"
    MODEL_NAME: str = "PPO"
    HUGGINGFACE_REPO_ID: str = "Stepan9773/ppo-LunarLander-v2"
    HUGGINGFACE_MODEL_FILENAME: str = "ppo-LunarLander-v2-lab.zip"


settings = Settings()
