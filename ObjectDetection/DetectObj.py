import cv2

class DetectObj:

    def __init__(self,Haarfile):
        self.HaarfilePath=Haarfile;

    def detect(self,image):
            haarfile=self.HaarfilePath;
            faceCascade = cv2.CascadeClassifier(haarfile)
            # Read the image
            image = cv2.imread(image)
            try:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            except:
                return
            matchs = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
            )
            print("Found {0} Match!".format(len(matchs)));

            # Draw a rectangle around the faces
            for (x, y, w, h) in matchs:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
              
            #cv2.imshow("Match found", image)
            #cv2.waitKey(0)

            if len(matchs)==0:
                return False
            else:
                cv2.imwrite('Images/MatchFound.png',image)
                return True
