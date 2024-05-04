from TextSummary.config.configuration import ConfigManager
from TextSummary.components.model_eval import ModelEval
from TextSummary.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        model_eval_config = config.get_model_eval_config()
        model_eval = ModelEval(config=model_eval_config)
        model_eval.evaluate()