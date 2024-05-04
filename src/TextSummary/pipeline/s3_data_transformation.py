from TextSummary.config.configuration import ConfigManager
from TextSummary.components.data_transformation import Data_transformation
from TextSummary.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = Data_transformation(config=data_transformation_config)
        data_transformation.convert()