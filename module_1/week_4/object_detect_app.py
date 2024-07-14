import cv2
import numpy as np
import streamlit as st
from PIL import Image
MODEL = "T:\Documnets\AIO\AIO_2024\model\MobileNetSSD_deploy.caffemodel"
PROTOTXT = "T:\Documnets\AIO\AIO_2024\model\MobileNetSSD_deploy.prototxt.txt"


def process_image(image):
    blob = cv2.dnn.blobFromImage(cv2.resize(
        image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):

    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            cv2.rectangle(image, (start_x, start_y), (end_x, end_y), 80, 3)
    return image

def annotate_video(video):
    video = cv2.VideoCapture(video)

    processed_frame = []
    while True:
        ret, frame = video.read()

        if not ret:
            break
        detections = process_image(frame)
        process_frame = annotate_image(frame, detections=detections)

        processed_frame.append(process_frame)
    return processed_frame

def main():
    st.title('Object Detection fo Images')
    file = st.file_uploader("Upload file", type=['png', 'jpeg', 'jpg'])

    if file is not None:
        st.image(file, caption='Uploaded image')

        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        image_processed = annotate_image(image, detections)
        st.image(image_processed, caption="processed image")


if __name__ == "__main__":
    main()
