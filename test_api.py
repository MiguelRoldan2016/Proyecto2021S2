# import the necessary packages
import requests
import cv2
# define the URL to our face detection API
fpath = "staticfiles/default.png"
url = "http://api.pyimagesearch.com/face_detection/detect/"


# # use our face detection API to find faces in images via image URL
# image = cv2.imread(fpath)
# payload = {"url": "https://recursoshumanos.tv/wp-content/uploads/2021/07/RHTV-MB-8_Web-Feynman-1-1000x500-1.png"}
# print(payload)
# r = requests.post(url, data=payload).json()
# print("caras url: {}".format(r))
# # loop over the faces and draw them on the image
# for (startX, startY, endX, endY) in r["faces"]:
#     cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# # show the output image
# cv2.imwrite("staticfiles/feynman2.png", image)
# # cv2.imshow("obama.jpg", image)
# # cv2.waitKey(0)


# # load our image and now use the face detection API to find faces in
# # images by uploading an image directly
image = cv2.imread(fpath)
payload = {"image": open(fpath, "rb")}
r = requests.post(url, files=payload).json()
print("caras local: {}".format(r))
print(r.get("success"))
print(r.get("num_faces"))
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
cv2.imwrite("staticfiles/feynman3.png", image)


# # show the output image
# cv2.imshow("adrian.jpg", image)
# cv2.waitKey(0)
