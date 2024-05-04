from TextSummary.pipeline.s1_data_ingestion import DataIngestionTrainingPipeline
from TextSummary.pipeline.s2_data_validation import DataValidationTrainingPipeline
from TextSummary.pipeline.s3_data_transformation import DataTransformationTrainingPipeline
from TextSummary.pipeline.s4_model_train import ModelTrainingPipeline
from TextSummary.pipeline.s5_model_eval import ModelEvaluationPipeline
from TextSummary.logging import logger
'''
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

STAGE_NAME = "Data Tranforamtion Stage"

try:
    logger.info(f"------> Stage {STAGE_NAME} started <-------")
    data_tranformation = DataTransformationTrainingPipeline()
    data_tranformation.main()
    logger.info(f"------> Stage {STAGE_NAME} completed <------\n\n <------------>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"------> Stage {STAGE_NAME} started <-------")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f"------> Stage {STAGE_NAME} completed <------\n\n <------------>")
except Exception as e:
    logger.exception(e)
    raise e
'''
STAGE_NAME = "Model Evaluating Stage"

try:
    logger.info(f"------> Stage {STAGE_NAME} started <-------")
    model_eval = ModelEvaluationPipeline()
    model_eval.main()
    logger.info(f"------> Stage {STAGE_NAME} completed <------\n\n <------------>")
except Exception as e:
    logger.exception(e)
    raise e