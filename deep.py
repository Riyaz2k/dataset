import cv2
web=cv2.VideoCapture(0)
f=0
while(True):
    _,frame=web.read()
    cv2.imshow("camera",frame)
    cv2.imwrite("riyaz/"+str(f)+".jpg",frame)
    f+=1
    key=cv2.waitKey(1)
    if(key==27):
        break
cv2.destroyAllWindows()
web.release()
print("Done")
