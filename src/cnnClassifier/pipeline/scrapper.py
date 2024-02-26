from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_scraping import DataScraping
from cnnClassifier import logger

STAGE_NAME = "Data Scraping"

class ScrapperPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_scraping_config = config.get_data_scraping_config()
        data_scraping = DataScraping(config=data_scraping_config)
        real = data_scraping.scrape_reals()
        fake = data_scraping.scrape_fakes()
        data_scraping.refresh_data(real, fake)
        logger.info(f"Completed {STAGE_NAME}...")

if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}...")
        pipeline = ScrapperPipeline()
        pipeline.main()
        logger.info(f"Completed {STAGE_NAME}...")
    except Exception as e:
        logger.exception(f"Failed to run {STAGE_NAME} because of {str(e)}")
        raise e