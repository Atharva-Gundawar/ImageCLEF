"""
About:
    Single Image classification for "csv", "py", "png", "jpg" file types 
    to increase file upload size use : streamlit run main.py --server.maxUploadSize=1028
Usage:
    Replace contents of predict function 
    Run using :streamlit run main.py .
Template:
    https://github.com/Atharva-Gundawar/Streamlit-template-for-Image-Classification-and-Object-detection/blob/main/ImageClassification.py
"""

import streamlit as st
import Image
from predict import return_prediction

FILE_TYPES = ["csv", "py", "png", "jpg"]
STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""


def main():
    """Run this function to display the Streamlit app"""
    st.info(__doc__)
    st.title("Upload + Classification Example")
    st.markdown(STYLE, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload file", type=FILE_TYPES)
    show_file = st.empty()
    if not uploaded_file:
        show_file.info("Please upload a file of type: " + ", ".join(FILE_TYPES))
        return
    
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label,time_req = get_labels(uploaded_file)
    st.write(f'{label}')
    st.write(f'{time_req}')
    
    uploaded_file.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('Stopped due to KeyboardInterrupt')