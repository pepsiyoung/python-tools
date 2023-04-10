import qrcode

# 生成二维码
img = qrcode.make(data="https://jmssub.net/members/getsub.php?service=705286&id=b87e62a7-e5c8-430f-8a18-0c85b10b8dbe")
img.show()