from PIL import Image


# im = Image.open(r"E:\DataCollect\8.7裂片原图_08_3568\8-000655-A.jpg")
# w, h = im.size
# im.show()

# x_middle = int(w / 2) + 4

# l_x1, l_y1 = 0, 0
# l_x2, l_y2 = x_middle, h
# l_im = im.crop((l_x1, l_y1, l_x2, l_y2))
# l_im.show()

# r_x1, r_y1 = x_middle, 0
# r_x2, r_y2 = w, h
# r_im = im.crop((r_x1, r_y1, r_x2, r_y2))
# r_im.show()

# l_w, l_h = l_im.size
# l_cut_im = l_im.crop((48, 15, l_w, l_h - 46))
# l_cut_im.show()

class ImageProcess:

    @staticmethod
    def cut_middle(im_path, middle_px):
        im = Image.open(im_path)
        w, h = im.size
        return im.crop((0, 0, middle_px, h)), im.crop((middle_px, 0, w, h))

    @staticmethod
    def cut_around(im: Image, box):
        print(type(im))


if __name__ == "__main__":
    left_im, right_im = ImageProcess.cut_middle(r"E:\DataCollect\8.7裂片原图_08_3568\8-000655-A.jpg", 1788)
    ImageProcess.cut_around(left_im)
