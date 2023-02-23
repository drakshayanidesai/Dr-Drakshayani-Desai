import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
st.title('Count Pipes in the Image')
st.header('Upload your Image:')
uploaded_file = st.file_uploader("Choose an image", type="png")

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

  
#image = cv2.imread('C:\\Users\\vgarlapati\\Downloads\\FW_Req_images\\Pipes_5.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
blur = cv2.GaussianBlur(gray, (7,11), 0)
canny = cv2.Canny(blur, 30, 150, 3)
dilated = cv2.dilate(canny, (1, 1), iterations=0)
  
(cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
total_pipes = len(cnt)
st.markdown(f'Total_pipe Count is = {total_pipes}')
st.image(rgb, channels="BGR")
# image5 actual apporx-1382  
#print("pipes in the image : ", len(cnt))