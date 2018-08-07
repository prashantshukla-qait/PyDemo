from SuperTest import supertest
import unittest
import urllib
class VerifyAccessibilityGuidlines(supertest):

    def test_Images(self):
        # self.driver.get("https://html.com/tags/figcaption/")
        # imgs=self.driver.find_elements_by_xpath('//img')
        # for img in imgs:
        #      src = img.get_attribute('src')
        #      urllib.urlretrieve(src, "Images/Image.png")
        #      classlist=[]
        #      if self.detectFace.detect("Images/Image.png")==True:
        #           classlist.append("face")
        #      text = img.get_attribute('alt')
        #      src = img.get_attribute('src')
        #      print(src)
        #      if text==None:
        #         imgcaption=img.find_element_by_xpath("../figcaption")
        #         text=imgcaption.text
        #      print(text)
             classfromText=self.detectText.detectTextIn("Hello Jaspal")
        #     assertIn(classfromaltText, classlist)


if __name__ == '__main__':
    unittest.main()
