import os
import cv2
val_images = os.listdir("val_img")

for img in val_images:
    im = cv2.imread(os.path.join("val_img", img))
    im = cv2.resize(im, (256, 256))  # 512 x 384 is our image size
    cv2.imwrite(os.path.join("resized_test_img", img), im)