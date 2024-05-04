from TextSummary.pipeline.s1_data_ingestion import DataIngestionTrainingPipeline
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
