import numpy as np
from huggingface_sb3 import load_from_hub
from stable_baselines3 import PPO

from app.enums import RLModels
from app.models import RLInput


class HuggingFaceModel:
    rl_models = {RLModels.PPO: PPO}

    def __init__(self, model_name: str, repo_id: str, model_filename: str) -> None:
        self.repo_id = repo_id
        self.model_filename = model_filename
        self.model = self.load_model(model_name)

    def get_model(self, model_name: str):
        return self.rl_models[model_name]

    def load_model(self, model_name: str):
        self.model = self.get_model(model_name)
        # When the model was trained on Python 3.8 the pickle protocol is 5
        # But Python 3.6, 3.7 use protocol 4
        # In order to get compatibility we need to:
        # 1. Install pickle5 (we done it at the beginning of the colab)
        # 2. Create a custom empty object we pass as parameter to PPO.load()
        placeholder_pickle_sucks = {
            "learning_rate": 0.0,
            "lr_schedule": lambda _: 0.0,
            "clip_range": lambda _: 0.0,
        }
        checkpoint = load_from_hub(self.repo_id, self.model_filename)
        return self.model.load(
            checkpoint, custom_objects=placeholder_pickle_sucks, print_system_info=True
        )

    def predict(self, observation: RLInput) -> int:
        observation = np.array(list(observation.model_dump().values()))
        action, _ = self.model.predict(observation)
        return action
