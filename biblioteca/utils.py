import requests
import cv2
from base64 import b64decode, b64encode


def detect_face(fotoData, fn="staticfiles/tempofoto.png"):
    # definicion de urls
    url = "http://api.pyimagesearch.com/face_detection/detect/"

    # guardar Base64 a archivo temporal de imagen
    if (fotoData.find("data:image/png;base64,") != -1):
        imgdata = b64decode(fotoData.replace("data:image/png;base64,", ""))
        with open(fn, 'wb') as f:
            f.write(imgdata)

    # detectar caras
    f = open(fn, "rb")
    payload = {"image": f}
    r = requests.post(url, files=payload).json()
    print(r)

    if not (r.get("success") and r.get("num_faces") > 0):
        return None

    # pintar rectangulos
    image = cv2.imread(fn)
    for (startX, startY, endX, endY) in r["faces"]:
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
    cv2.imwrite(fn, image)

    print("caras local: {}".format(r))

    f = open(fn, "rb").read()
    encoded = b64encode(f).decode('ascii')

    return "data:image/png;base64,"+encoded
