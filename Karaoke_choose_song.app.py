import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Karaoke Night Request",
    page_icon="🎤",
    layout="centered"
)

# 2. Custom CSS for a colorful theme
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #1f1c2c 0%, #928dab 100%);
        color: #FFFFFF;
    }

    /* Main Cards Container */
    .stForm, div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 15px !important;
        padding: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* Headings */
    h1 {
        color: #FFD700 !important;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
    }

    h3 {
        color: #00FFFF !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #ff007f, #7928ca) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 10px 24px !important;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 15px #ff007f;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Initialize Session State for storing requests persistent across users during app execution
if "requests" not in st.session_state:
    st.session_state["requests"] = []

# 4. List of available songs from image
SONGS = [
“ABBA - Dancing Queen"
“Adele - Someone Like You"
“Aerosmith - Crazy"
“Aerosmith - I don't want to miss a thing"
“Alejandro Sanz - Corazón partío"
“Andrés Calamaro - Flaca"
“Aqua - Barbie Girl"
“Backstreet boys - I want it that way"
“Black Eyed Peas - I Gotta Feeling"
“Bon Jovi - It's my life"
“Bon Jovi - Livin' on a Prayer"
“Bruno Mars - The Lazy Song"
“Camilo Sesto - Vivir así es morir de amor"
“Eminem feat Rihanna - Love The Way You Lie"
“Enanitos verdes - Lamento boliviano"
“Evanescence - Bring Me to Life"
“Evanescence - My Inmortal"
“Green Day - Boulevard of Broken Dreams"
“Guns N' Roses - Sweet Child O'Mine"
“James Blunt - You're Beautiful"
“Jason Mraz - I'm yours"
“José José - El triste"
“Katy Perry - Hot N Cold"
“Lady GaGa - Alejandro"
“Lady GaGa - Bad Romance"
“Lady Gaga - Poker Face"
“Lagy gaga & Bruno Mars - Die with a smile"
“Linkin Park - In The End"
“Linkin Park - Numb"
“Marc Anthony - Ahora quien (salsa)"
“Maroon 5 - She Will Be Loved"
“Mena Massoud, Naomi Scott - A Whole New World"
“Michael Jackson - Smooth Criminal"
“Michel Teló - Ai Se Eu Te Pego"
“Nirvana - Smells Like Teen Spirit"
“O-Zone - Dragostea din teï"
“Queen - Bohemian Rhapsody"
“Queen - Don't Stop Me Now"
“Queen - I Want to Break Free"
“Queen - We Are the Champions"
“Queen - We Will Rock You"
“Radiohead - Creep"
“Slipknot - Snuff"
“Slawomir - Milosc w Zakopanem"
“The Beatles - Yesterday"
“The Cranberries - Zombie"
“Vlad Topalov - Kak zhe tak mozhet byt"
“Amy Winehouse feat. Mark Ronson - Valerie"
“Chutci - Samaya"
“Frank Sinatra - My Way"
“Gayle - Abcdefu"
“John Legend - All of Me"
“Natasha Bedingfield - Unwritten"
“Rufus Wainwright - Hallelujah (Shrek version)"
]

# 5. Header Section
st.title("🎤 Karaoke Night Request Box 🎶")
st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Pick your track, grab the mic, and get ready to shine!</p>",
    unsafe_allow_html=True)

# 6. Song Request Form
with st.form("karaoke_form", clear_on_submit=True):
    name = st.text_input("👤 Your Name or Stage Name:")
    selected_song = st.selectbox("🎵 Select your song:", ["-- Select a song --"] + SONGS)
    submitted = st.form_submit_button("🔥 Send Song Request!")

if submitted:
    if not name.strip():
        st.error("Please enter your name before submitting!")
    elif selected_song == "-- Select a song --":
        st.error("Please choose a song from the list!")
    else:
        st.session_state["requests"].append({"Name": name.strip(), "Song": selected_song})
        st.balloons()
        st.success(
            f"🎉 **Awesome pick, {name}!** You chose **{selected_song}**. Get ready—you'll be taking the stage soon!")

# 7. Host Admin Panel (Password Protected)
st.divider()
with st.expander("🔐 Host / Admin Panel"):
    st.write("Access the singer queue:")
    password = st.text_input("Enter Admin Password:", type="password")

    # Change "karaoke2026" to any password you prefer
    if password == "Karaoke2026":
        st.success("Access Granted!")
        st.subheader("📋 Singer Queue")

        if len(st.session_state["requests"]) > 0:
            df = pd.DataFrame(st.session_state["requests"])
            st.dataframe(df, use_container_width=True)

            if st.button("🗑️ Clear Queue"):
                st.session_state["requests"] = []
                st.rerun()
        else:
            st.info("No song requests submitted yet.")
    elif password:
        st.error("Incorrect password.")
