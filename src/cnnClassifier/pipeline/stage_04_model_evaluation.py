from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger
import os

os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/Pernam75/MLFlow-DVC-Docker-MLOPS.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'Pernam75'
os.environ['MLFLOW_TRACKING_PASSWORD'] = '1e699d26f03e9c945b5485e741b464a017b391ad'

STAGE_NAME = "Model Evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}...")
        pipeline = EvaluationPipeline()
        pipeline.main()
        logger.info(f"Completed {STAGE_NAME}...")
    except Exception as e:
        logger.exception(f"Failed to run {STAGE_NAME} because of {str(e)}")
        raise e