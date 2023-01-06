import time

im_path = r"C:\Users\admin\Desktop\待检测图\43-000235-A.jpg"

write_file = open(r"D:\Test\source1\name.jpg", "wb")
with open(im_path, "rb") as f:
    for index, line in enumerate(f.readlines()):
        write_file.write(line)
        time.sleep(0.02)
        print(index)

write_file.close()
print('end')

# img_bin = f.read()  # 内容读取

# with open(r"D:\Test\source1\name.jpg", "wb") as f:
#     # f.write(img_bin)
#     f.write()
#     print('111')

# https://blog.csdn.net/private_void_main/article/details/89510172
# https://bbs.csdn.net/topics/390330954
