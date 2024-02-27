import pytest
import os
from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.utils.common import get_size
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

def test_get_base_model():

    STAGE_NAME = "Prepare Base Model"
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)    


    try:
        logger.info(f"Starting {STAGE_NAME} ...")
        prepare_base_model.get_base_model()
        assert prepare_base_model_config.base_model_path.exists(), "Base model was not saved correctly."
        logger.info(f"Completed {STAGE_NAME}...")

    except Exception as e:
        pytest.fail(e)
    
def test_update_base_model():

    STAGE_NAME = "Prepare Base Model"
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)    


    try:
        logger.info(f"Starting {STAGE_NAME} update...")
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        assert prepare_base_model_config.updated_base_model_path.exists(), "Base model was not saved correctly."
        logger.info(f"Completed {STAGE_NAME} update...")

    except Exception as e:
        pytest.fail(e) 
