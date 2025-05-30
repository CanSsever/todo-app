import streamlit as st
from PIL import Image

with st.expander("open camera"):
    camera_image = st.camera_input("Camera")
uploaded_image = st.file_uploader("Upload Image")


if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)
elif uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)
