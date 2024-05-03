from audiocraft.models import MusicGen

import streamlit as st
import os
import torch
import numpy as np
import base64

@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained("facebook/musicgen-small")
    return model

st.set_page_config(
    page_title='MusicGen',
    page_icon='🎵',
    layout='centered',
    initial_sidebar_state='collapsed'
)

def main():
    st.title("Music Generation with MusicGen")

    with st.expander("Expand for more information"):
        st.write("This is a demo of MusicGen, a model for generating music. It is based on the MusicNet dataset, which contains a large collection of classical music. The model is trained on this dataset and can generate music in the style of the composers in the dataset.")

    text_area = st.text_area("Enter the kind of melofy you want", height=200)
    time_slider = st.slider("Length of the melody (in seconds)", min_value=1, max_value=60, value=30, step=10)

    if text_area and time_slider:
        st.json(
            {
                "Description": text_area,
                "Selected Time Duration": time_slider
            }
        )

        st.subheader("Your music has been generated")

if __name__ == '__main__':
    main()