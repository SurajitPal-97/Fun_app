import streamlit as st
import os

from PIL import Image
import random

st.title("Hiii Puchuuu!!!")

st.header("I feel j I am in love with you...")

st.write("Do you love suju ?")

ans=st.text_input("Write your answer:")

if ans:
    st.write("Suju loves you too..")

love_levels=["onek","Sobcheyeeee bsiii"]

love=st.select_slider("Select how much do you love suju:",options=love_levels)

if love=="Sobcheyeeee bsiii":
    st.balloons()
    st.write("Suju o tmy sobcheyeeeee bsiiiii valobaseee")


PHOTO_FOLDER="photoes"
with st.expander("baby do you wanna see our  some memories together "):


    st.title("Our Memory Gallery")

    photo_files = [f for f in os.listdir(PHOTO_FOLDER) if f.endswith(('jpg', 'jpeg', 'png'))]
    random.shuffle(photo_files)
    if photo_files:
        cols = st.columns(3)  # Make 3-column layout
        for index, file_name in enumerate(photo_files):
            image_path = os.path.join(PHOTO_FOLDER, file_name)
            image = Image.open(image_path)  # Open the image
            with cols[index % 3]:  # Place image into one of the 3 columns
                custom_captions = {
        "first_outing.jpg": "Our first long outing, that long train journey, ekasthe vog khawa, and fera r smy er thrill, long toto joiurney oi thandaiiii ",
        "First_puja.jpg": "mone pore ei moment ta, toke koto koste maniyechilam sedin, ohh tr sei rag rag mukh but tau valobese jol khete khete kadhe matha deua",
        "First_valentinesday.jpg": "Our first valentines day together 😛",
        "first_restaurant_date.jpg":"Pratham kono restaurant e khetye jaua amader"}
                caption = custom_captions.get(file_name, "Our Moment ❤️")
                st.image(image, caption=caption, use_container_width=True)


            









