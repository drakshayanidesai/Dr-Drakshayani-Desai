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
    img = cv2.imdecode(file_bytes, 1)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image to reduce noise
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply the HoughCircles function to detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=5, maxRadius=80)

# Check if any circles were detected
if circles is not None:
    # Convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
    
    # Initialize a counter for the number of circles detected
    num_circles = 0
    
    # Loop through each detected circle
    for (x, y, r) in circles:
        # Draw the circle on the image
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        
        # Increment the counter for the number of circles detected
        num_circles += 1
        
        # Print the dimensions of the circle
        #print('Circle', num_circles, ': x =', x, 'y =', y, 'r =', r)
        
    # Display the image with the detected circles
    #cv2.imshow("Detected Circles", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
st.markdown(f'Total_pipe Count is = {num_circles}')
st.image(img, channels="BGR")
# image5 actual apporx-1382  
#print("pipes in the image : ", len(cnt))