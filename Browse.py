import os
from selenium import webdriver
import urllib
import DetectObj
import DetectText as DT
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.runscope.com/customers/human-api")
img=driver.find_element_by_xpath('//*[@class="resize www-customer-pic customer"]')
src = img.get_attribute('src')
DT=DT.DetectText()
alttext = img.get_attribute('alt')
print(alttext)
DT.detectText(alttext)
#downloading the image
# urllib.urlretrieve(src, "Image.png")
#
# detectFace=DetectObj.DetectObj()
#
# faces=detectFace.detect("Image.png","face.xml")

driver.quit()
