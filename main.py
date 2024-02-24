from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"Completed {STAGE_NAME}...")
except Exception as e:
    logger.exception(f"Failed to run {STAGE_NAME} because of {str(e)}")
    raise e