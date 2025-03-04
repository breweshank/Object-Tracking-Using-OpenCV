import cv2,time
import imutils
pinkLower=(164,57,221)
pinkUpper=(179,255,255)
time.sleep(1)
cam = cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    frame = imutils.resize(img,width=600)
    blur = cv2.GaussianBlur(img,(11,11),0)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask =cv2.inRange(hsv,pinkLower,pinkUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask = cv2.erode(mask,None,iterations=2)
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    if len(cnts) > 0:
        c = max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M= cv2.moments(c)
        if M["m00"]!=0:
            center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
            if radius >10:
                cv2.circle(img,(int(x),int(y)),int(radius),(0,255,0),2)
                cv2.circle(img,center,5,(255,255,255),-1)
                if radius >250:
                    cv2.putText(img,"to close",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),2)
                else:
                    if (center[0]<150):
                        cv2.putText(img,"Left",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),2)
                        print("left")
                    elif(center[0]>450):
                        cv2.putText(img,"Right",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),2)
                        print("right")
                    else:
                        cv2.putText(img,"Inframe",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),2)
                        print("Inframe")
    cv2.imshow("Object tracking",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()