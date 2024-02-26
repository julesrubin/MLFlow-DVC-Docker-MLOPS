from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import shutil
import zipfile
from cnnClassifier.entity.config_entity import DataScrapingConfig


class DataScraping:
    def __init__(self, config: DataScrapingConfig): # DataScrapingConfig is a dataclass that contains the source_fake_URL and source_real_URL as attributes
        self.config = config

    def scrape_fakes(self) -> list:
        '''
        Scrapes data from the url
        '''
        try:
            # Set up the Chrome webdriver
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)

            # Open the website
            driver.get(self.config.source_fake_URL)

            # Wait for the page to load
            driver.implicitly_wait(10)

            # Find all image elements
            images = driver.find_elements(By.TAG_NAME, 'img')

            # Extract src attribute from each image
            image_srcs = [image.get_attribute('src') for image in images]

            #drop images with no "freepic" in the src
            image_srcs = [src for src in image_srcs if "img.freepik.com" in src]

            # Print the image srcs
            fake = []
            for src in image_srcs:
                # print(src)
                fake.append(src)

            # Close the browser
            driver.quit()
            return fake
        except Exception as e:
            raise e

    def scrape_reals(self) -> list:
        '''
        Scrapes data from the url
        '''
        try:
            # Set up the Chrome webdriver
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)

            # Open the website
            driver.get(self.config.source_real_URL)
            # Wait for the page to load
            driver.implicitly_wait(10)

            # Find all image elements
            images = driver.find_elements(By.TAG_NAME, 'img')

            # Extract src attribute from each image
            image_srcs = [image.get_attribute('src') for image in images]

            #drop images with "freepic" in the src
            image_srcs = [src for src in image_srcs if "img.freepik.com" not in src]

            # Print the image srcs
            real = []
            for src in image_srcs:
                # print(src)
                real.append(src)

            # Close the browser
            driver.quit()
            return real
        except Exception as e:
            raise e
    

    def refresh_data(self, real, fake):
        '''
        Refreshes the data
        '''
        try:
            prefix = 0

            #find the biggest prefix in the images prefix_0.jpg, prefix_1.jpg, ...
            # if the images doesn't contain any prefix, the prefix is 0 , doesn't contain "_"
            for file in os.listdir("artifacts/data_ingestion/temp/FAKE"):
                if "_" in file:
                    prefix = max(prefix, int(file.split("_")[0]))
                else:
                    prefix = max(prefix, 0)


            #increment the prefix
            prefix += 1

            # download the images to the correct directories
            import requests
            # download the images
            for i, url in enumerate(fake):
                response = requests.get(url)
                file = open(f"artifacts/data_ingestion/temp/FAKE/{prefix}_{i}.jpg", "wb")
                file.write(response.content)
                file.close()
            for i, url in enumerate(real):
                response = requests.get(url)
                file = open(f"artifacts/data_ingestion/temp/REAL/{prefix}_{i}.jpg", "wb")
                file.write(response.content)
                file.close()

        except Exception as e:
            raise e


        