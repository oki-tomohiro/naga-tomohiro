#pip install opencv-python 
#pip install matplotlib
#opencv-pythonとmatplotlibをinstallする.別々のセルで行うほうが良い.
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)
i = 0
count = 0
im = np.zeros(1000000)

while(True):
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    count += 1
    im[i] = frame.mean()
    i += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

x = np.linspace(0,count,count)
y = im[0:count]

plt.figure(figsize=(15,5))
plt.plot(x,y)

cap = cv2.VideoCapture(0)
print("FPS = ",end="")
print(cap.get(cv2.CAP_PROP_FPS)) #FPS表示

#今回やるもの
#画像の平均値を入れる(print(frame.mean())で)
#カメラから動画を取得して表示するコードは,https://weblabo.oscasierra.net/python/opencv-videocapture-camera.htmlより引用
#FPS表示のコードは,https://note.nkmk.me/python-opencv-fps-measure/より引用
#カメラに手を付けて,光を当てる
#このとき,動画がまるで心拍数と同じタイミングで微妙に点滅していることがわかる.