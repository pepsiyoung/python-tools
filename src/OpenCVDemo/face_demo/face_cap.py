import cv2 as cv

cap = cv.VideoCapture(0)

num = 1
face_name = "Boss"
face_id = 1

print(cap.isOpened())

while cap.isOpened():
    # 捕获摄像头图像
    ret_flag, vshow = cap.read()
    # 显示捕获的照片
    cv.imshow("capture_test", vshow)
    # 图像刷新的频率
    k = cv.waitKey(1) & 0xff
    # 设置按键保存照片
    if k == ord('s'):
        # 保存图片
        cv.imencode(".jpg", vshow)[1].tofile(f"/Users/pepsiyoung/Project/my/python/python-tools/src/OpenCVDemo/faceDetect/imgdata/{str(face_id)}_{face_name}_{str(num)}.jpg")
        print(f"成功保存第{str(num)}张照片")
        num += 1
    elif k == ord(' '):
        break
# 关闭摄像
cap.release()
# 销毁窗口
cv.destroyAllWindows()
