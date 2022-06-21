# importing libraries
import cv2
import numpy as np
import face_recognition as face_rec


# function to resize image
def resize(rimg, size):
    width = int(rimg.shape[1] * size)
    height = int(rimg.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(rimg, dimension, interpolation=cv2.INTER_AREA)


# image declaration
img = face_rec.load_image_file('images/j1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = resize(img, 0.5)

img_test = face_rec.load_image_file('images/j2.jpg')
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
img_test = resize(img_test, 0.5)

# finding face location
faceLoc = face_rec.face_locations(img)[0]
encode_face = face_rec.face_encodings(img)[0]
cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLoc_test = face_rec.face_locations(img_test)[0]
encode_face_test = face_rec.face_encodings(img_test)[0]
cv2.rectangle(img_test, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

results = face_rec.compare_faces([encode_face], encode_face_test)
print(results)

cv2.imshow('J Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
