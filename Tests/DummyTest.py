from SuperTest import supertest
import unittest
import urllib.request as urllib
from Compare import compare
class VerifyAccessibilityGuidlines(supertest):

    def test_Images(self):
         self.driver.get("https://www.runscope.com/customers/human-api")
         imgs=self.driver.find_elements_by_xpath('//img[@class="resize www-customer-pic customer"]')
         for img in imgs:
              src = img.get_attribute('src')
              try:
                urllib.urlretrieve(src, "Images/Image.png")
                print('downloading an image')
              except:
                pass
              classlist=[]
              if self.detectFace.detect("Images/Image.png")==True:
                   classlist.append("person")
              text = img.get_attribute('alt')
              src = img.get_attribute('src')
              # print(src)
              if text==None:
                 imgcaption=img.find_element_by_xpath("../figcaption")
                 text=imgcaption.text
              # print(text)
              classfromText=self.detectText.detectTextIn(text)
              # print(classfromText)
              self.assertTrue(compare.compare(classfromText, classlist))

    def test_Images_via_API(self):
         self.driver.get("https://www.runscope.com/customers/human-api")
         imgs=self.driver.find_elements_by_xpath('//img[@alt="Image of baby foot with sores"]')
         for img in imgs:
              classlist=[]
              src = img.get_attribute('src')
              response = self.model.predict_by_url(url=src)
              concepts = response['outputs'][0]['data']['concepts']
              for concept in concepts:
                # print(concept['name'], concept['value'])
                if(concept['value']*100>90.00): 
                  classlist.append(concept['name'])
              text = img.get_attribute('alt') 
              # print(src)
              if text==None:
                 imgcaption=img.find_element_by_xpath("../figcaption")
                 text=imgcaption.text
              # print(text)
              classfromText=self.detectText.detectTextIn(text)
              self.assertTrue(compare.compare(classfromText, classlist))

    def test_face_Image_via_API(self):
         self.driver.get("https://www.runscope.com/customers/human-api")
         imgs=self.driver.find_elements_by_xpath('//img[@class="resize www-customer-pic customer"]')
         for img in imgs:
              classlist=[]
              src = img.get_attribute('src')
              response = self.model.predict_by_url(url=src)
              concepts = response['outputs'][0]['data']['concepts']
              for concept in concepts:
                print(concept['name'], concept['value'])
                if(concept['value']*100>90.00): 
                  classlist.append(concept['name'])
              text = img.get_attribute('alt') 
              print(src)
              if text==None:
                 imgcaption=img.find_element_by_xpath("../figcaption")
                 text=imgcaption.text
              print(text)
              classfromText=self.detectText.detectTextIn(text)
              self.assertTrue(compare.compare(classfromText, classlist))
    def test_Animals_Image_via_API(self):
         self.driver.get("http://www.animalplanet.com/wild-animals/")
         imgs=self.driver.find_elements_by_xpath('//img[contains(@src,"zebra")]')
         for img in imgs:
              classlist=[]
              src = img.get_attribute('src')
              response = self.model.predict_by_url(url=src)
              concepts = response['outputs'][0]['data']['concepts']
              for concept in concepts:
                # print(concept['name'], concept['value'])
                if(concept['value']*100>90.00): 
                  classlist.append(concept['name'])
              text = img.get_attribute('alt') 
              # print(src)
              if text==None:
                 imgcaption=img.find_element_by_xpath("../figcaption")
                 text=imgcaption.text
              print(text)
              classfromText=self.detectText.detectTextIn(text)
              self.assertTrue(compare.compare(classfromText, classlist))

if __name__ == '__main__':
    unittest.main()
