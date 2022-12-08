# OSS팀플 연습 
# 사진에서 얼굴(크기도) 검출 - 희현
# 사진에서 하얀색(마스크-크기도 검출)-희진, 선인
# 1&2 성공 시 얼굴에서 하얀색이 차지하는 비율 검출 -도이
# 그 비율에 따라서 마스크 0,X유무 판단

# 사진 파일 하나 더 추가함 img1으로

import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default_.xml')

img = cv2.imread('./image/heejin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
cv2.namedWindow('Heejin', cv2.WINDOW_NORMAL) //사용자가 사진의 크기를 바꿀 수 있음
cv2.imshow('Heejin', img)
cv2.waitKey()