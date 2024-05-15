# pip install opencv-python pip install mediapipe

import cv2
import mediapipe as mp
import pyautogui
camera=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh()
screen_w,screen_h=pyautogui.size()# it's because we don't move cursor in hole screen so we apply this 1
#for video continuesely runing
while True:
    _, frame=camera.read()
    frame=cv2.flip(frame,1)# for flip the curser
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    ouput=face_mesh.process(rgb_frame)
    landmark_points=ouput.multi_face_landmarks
    frame_h,frame_w,_=frame.shape
    if landmark_points:
        landmarks=landmark_points[0].landmark
        
        for id,landmark in  enumerate(landmarks[465:480]):#enumerate it's give id
            X=int(landmark.x * frame_w)
            Y=int(landmark.y * frame_h)
            cv2.circle(frame,(X,Y),3,(0,255,0))#many green marks on face face dedects
            if id==1:
                screen_x=int(landmark.x*screen_w)
                screen_y=int(landmark.y*screen_h)
                pyautogui.moveTo(screen_x,screen_y)
    cv2.imshow("eyes controll mouse",frame)
    cv2.waitKey(1)
    # detect the face  pip install mediapipe
    #  for cursour pip install PyAutoGUI
    