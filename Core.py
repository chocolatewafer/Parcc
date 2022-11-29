import cv2
import pytesseract
import argparse
import numpy as np
import imutils
from imutils import paths

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ACER\AppData\Local\Tesseract-OCR\tesseract.exe'

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                        help="path to input directory of images")
ap.add_argument("-c", "--clear-border", type=int, default=-1,
                    help="whether or to clear border pixels before OCR'ing")
ap.add_argument("-p", "--psm", type=int, default=7,
                help="default PSM mode for OCR'ing license plates")
ap.add_argument("-d", "--debug", type=int, default=-1,
                help="whether or not to show additional visualizations")
args = vars(ap.parse_args())

imagePaths = sorted(list(paths.list_images(args["input"])))
# loop over all image paths in the input directory
for imagePath in imagePaths:
    # load the input image from disk and resize it
    image = cv2.imread(imagePath)
    image = imutils.resize(image, width=600)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('', cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)

    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
    edged = cv2.Canny(bfilter, 30, 200)  # Edge detection
    cv2.imshow('', cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('', cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2 + 1, y1:y2 + 1]
    cv2.imshow('', cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    options += " --psm {}".format(7)


    reader = pytesseract.image_to_string(cropped_image, config=options)
    result = reader
    text = result
    font = cv2.FONT_HERSHEY_SIMPLEX
    res = cv2.putText(image, text=text, org=(approx[0][0][0], approx[1][0][1] + 60), fontFace=font, fontScale=1,
                      color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    res = cv2.rectangle(image, tuple(approx[0][0]), tuple(approx[2][0]), (0, 255, 0), 3)
    cv2.imshow('', cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
