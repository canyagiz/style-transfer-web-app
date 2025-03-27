import requests
import streamlit as st
from PIL import Image
import json


STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la muse": "la_muse",
    "mosaic": "mosaic",
    "starry night": "starry_night",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie", 
}

st.title("Style Transfer Web App")

image = st.file_uploader("Choose an image")

style = st.selectbox("Choose a style", [i for i in STYLES.keys()])

if st.button("Style Transfer"):
    if image is not None and style is not None:
        try:
            with st.spinner("Applying style transfer..."):
                files = {"file": image.getvalue()}
                res = requests.post(f"http://backend:8080/{style}", files=files)
                
                # Check if the request was successful
                if res.status_code == 200:
                    try:
                        img_pth = res.json()
                        image = Image.open(img_pth.get("name"))
                        st.image(image, width=500)    

                    except json.JSONDecodeError:
                        st.error(f"Error: Invalid JSON response from backend. Response: {res.text[:100]}...")
                else:
                    st.error(f"Error: Backend returned status code {res.status_code}. Response: {res.text[:100]}...")
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.write("Please make sure the backend service is running and accessible.")