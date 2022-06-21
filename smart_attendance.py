import cv2
import numpy as np
import face_recognition as face_rec
import os


# function to resize image
def resize(r_img, size):
    width = int(r_img.shape[1] * size)
    height = int(r_img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(r_img, dimension, interpolation=cv2.INTER_AREA)


path = 'images'
studentImg = []
studentName = []
studentList = os.listdir(path)
print(studentList)
for i in studentList:
    currImg = cv2.imread(f'{path}/{i}')
    studentImg.append(currImg)
    studentName.append(os.path.splitext(i)[0])


print(studentName)


def fin_encoding(images):
    encoding_list = []
    for img in images:
        img = resize(img, 0.50)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode_img = face_rec.face_encodings(img)[0]
        encoding_list.append(encode_img)
    return encoding_list


encode_list = fin_encoding(studentImg)

vid = cv2.VideoCapture(0)

while True:
    success, frame = vid.read()
    Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    frames = cv2.cvtColor(Smaller_frames, cv2.COLOR_BGR2RGB)

    faces_in_frame = face_rec.face_locations(frames)
    encode_in_frame = face_rec.face_encodings(frames, faces_in_frame)

    for encode_face, faceLoc in zip(encode_in_frame, faces_in_frame):
        matches = face_rec.compare_faces(encode_list, encode_face)
        face_dis = face_rec.face_distance(encode_list, encode_face)
        print(face_dis)
        matchIndex = np.argmin(face_dis)

        if matches[matchIndex]:
            name = studentName[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.rectangle(frame, (x1, y2-25), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2. imshow('Video', frame)
        cv2.waitKey(1)
