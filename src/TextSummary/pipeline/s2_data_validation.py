from TextSummary.config.configuration import ConfigManager
from TextSummary.components.data_validation import Data_validation
from TextSummary.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = Data_validation(config=data_validation_config)
        data_validation.validate_all_files_exists()


