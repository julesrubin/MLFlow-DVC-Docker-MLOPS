from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}...")
except Exception as e:
    logger.exception(f"Failed to run {STAGE_NAME} because of {str(e)}")
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}...")
except Exception as e:
    logger.exception(f"Failed to run {STAGE_NAME} because of {str(e)}")
    raise e