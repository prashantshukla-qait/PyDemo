import os
from selenium import webdriver
import urllib
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from ObjectDetection import DetectObj
from TextAnalyzer import DetectText as DT
import unittest

class supertest(unittest.TestCase):
    chromedriver = "drivers/chromedriver"
    driver=None
    detectText=DT.DetectText()
    detectFace=DetectObj.DetectObj("./HaarFiles/face.xml")
    detectPlate=DetectObj.DetectObj("./HaarFiles/NumberPlate.xml")
    detectSmile=DetectObj.DetectObj("./HaarFiles/Smile.xml")
    def setUp(self):
        os.environ["webdriver.chrome.driver"] = supertest.chromedriver
        supertest.driver = webdriver.Chrome(supertest.chromedriver)

    def tearDown(self):
         supertest.driver.quit()
