import requests
import streamlit as st
from PIL import Image


STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la_muse": "la_muse",
    "mosaic": "mosaic",
    "starry night": "starry_night",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie",
}


st.set_option("deprecation.showfileUploaderEncoding", False)

#H1 header
st.title("Style transfer web app")

#File uploader widget
image = st.file_uploader("Choose an image")

#displays the select widget for the styles
style = st.selectbox("Choose the style", [i for i in STYLES.keys()])

#displays a button
if st.button("Style Transfer"):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        res = requests.post(f"http://0.0.0.0:8081/{style}", files=files)
        img_path = res.json()
        image = Image.open(img_path.get("name"))
        st.image(image, width=500)