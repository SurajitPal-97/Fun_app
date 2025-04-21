import streamlit as st
import os

from PIL import Image
import random
import base64

messages = [
    "You're my forever favorite notification 💌",
    "Tor sei ghure takano, 10th may ami te auto te bose theke, ohh ho hoo, tr sei chokher maya....",
    "Whenever I think of love, I see your face 😘",
    "Puchuuu biye korbe amyy...💖",
    "Toke sei black dress tai jokhn dekhechilamm, r tor sei lojja pauaa✨",
    "Loving you is my favorite habit 💭",
    "Tor sei Kalibari r samne amy tene chumu khawaa...."
]

def show_love_message(msg):
    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
            margin-top: 30px;
        ">
            <div style="
                background-color: rgba(255, 192, 203, 0.95);
                padding: 20px 40px;
                border-radius: 20px;
                font-size: 26px;
                color: #4b004b;
                font-weight: bold;
                box-shadow: 0 4px 20px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 600px;
            ">
                💌 {msg}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def add_bg_music(mp3_file):
    with open(mp3_file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    st.markdown(f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

def set_bg(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set semi-transparent overlay
overlay_css = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-color: rgba(0, 0, 0, 0.55); 
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
}
</style>
"""
st.markdown(overlay_css, unsafe_allow_html=True)

# Set white text for headings, sliders, etc.
text_css = """
<style>
h1, h2, h3, p, .stTextInput label, .stSelectbox label,
.stSlider label, .stMarkdown, .stButton, .stExpander {
    color: white !important;
    font-weight: bold !important;
    text-shadow: 1px 1px 2px black;
}
</style>
"""
st.markdown(text_css, unsafe_allow_html=True)

# Call this at the top with your image filename
set_bg("newbg.jpg")  # Replace with your background image file


st.title("Our web Dashboard where we will have our cutest moments and massages")
st.write("Our love story started a long time ago but it is firstly initiated with a small text on whatsapp, which is.....")
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

if st.button("Want some music puchu? if yes hit this bbutton 💖"):
    add_bg_music("bg_music.mp3")

if st.button("💌 Click for a surprise love note!"):
    surprise = random.choice(messages)
    show_love_message(surprise)

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


            









