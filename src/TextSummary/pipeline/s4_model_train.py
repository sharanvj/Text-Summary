from TextSummary.config.configuration import ConfigManager
from TextSummary.components.model_train import ModelTrainer
from TextSummary.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        model_training_config = config.get_model_trainer_config()
        model_training = ModelTrainer(config=model_training_config)
        model_training.train()