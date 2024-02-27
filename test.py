
import pytest
import os
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from pathlib import Path
import tensorflow as tf
import shutil
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig



def test_download_zipfile():
    """Test the download of the zip file"""
    STAGE_NAME = "Data Ingestion"
    config = DataIngestionConfig(
        source_URL='https://drive.google.com/file/d/1s2a0KK6nCC3sDZLtC3r7Y8RoW3jqmSsE/view?usp=drive_link',
        local_data_file="artifacts/data_ingestion/data.zip",
        unzip_dir="artifacts/data_ingestion",
        root_dir="artifacts/data_ingestion"   
    )
    data_ingestion = DataIngestion(config=config)
    try:
        logger.info(f"Starting {STAGE_NAME} dowload...")
        data_ingestion.download_file()
        assert os.path.exists(config.local_data_file), "File was not downloaded to the expected location."
        logger.info(f"Completed {STAGE_NAME} dowload...")

    except Exception as e:
        pytest.fail(e)
        

def test_extract_zipfile():
    STAGE_NAME = "Data Ingestion"
    config = DataIngestionConfig(
        source_URL='https://drive.google.com/file/d/1s2a0KK6nCC3sDZLtC3r7Y8RoW3jqmSsE/view?usp=drive_link',
        local_data_file="artifacts/data_ingestion/data.zip",
        unzip_dir="artifacts/data_ingestion",
        root_dir="artifacts/data_ingestion"   
    )
    data_ingestion = DataIngestion(config=config)
    data_ingestion.download_file()
    try:
        logger.info(f"Starting {STAGE_NAME} extract...")
        data_ingestion.extract_zip_file()
        assert os.path.isdir(config.unzip_dir), "The unzip directory was not created."
        logger.info(f"Completed {STAGE_NAME} extract...")
    except Exception as e:
        pytest.fail(e)

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
    # Verify the base model has been saved correctly
    
            
