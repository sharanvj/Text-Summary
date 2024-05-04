from TextSummary.pipeline.s1_data_ingestion import DataIngestionTrainingPipeline
from TextSummary.pipeline.s2_data_validation import DataValidationTrainingPipeline
from TextSummary.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"------> Stage {STAGE_NAME} started <-------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"------> Stage {STAGE_NAME} completed <------\n\n <------------>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"------> Stage {STAGE_NAME} started <-------")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"------> Stage {STAGE_NAME} completed <------\n\n <------------>")
except Exception as e:
    logger.exception(e)
    raise e