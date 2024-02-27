from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline
from cnnClassifier.pipeline.scrapper import ScrapperPipeline
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#import time

BASE_URL = "http://localhost:4000"

def test_home_page():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

    # add silenium
    
    # button = driver.find_element(By.ID, 'send')
    # button.click()

    # button = driver.find_element(By.ID, 'uload')
    # button.click()
    

def test_train_route():

    response_get = requests.get(f"{BASE_URL}/train")
    assert response_get.status_code == 200
    assert response_get.text == "Training done successfully!"

    response_post = requests.post(f"{BASE_URL}/train")
    assert response_post.status_code == 200
    assert response_post.text == "Training done successfully!"

def test_predict_route():
    # Example: Test predict route with a dummy image data
    dummy_image_data = {"image": "base64encodeddummydata"}
    response = requests.post(f"{BASE_URL}/predict", json=dummy_image_data)
    assert response.status_code == 200
   

def test_fetch_new_data():
    response = requests.get(f"{BASE_URL}/fetch_new_data")
    assert response.status_code == 200
    

if __name__ == "__main__":
    test_home_page()
    test_train_route()
    test_predict_route()
    test_fetch_new_data()