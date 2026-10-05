import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Spooky Karaoke Night",
    page_icon="🎃",
    layout="centered"
)

# 2. Custom CSS for Spooky Theme
st.markdown("""
    <style>
    /* Dark Spooky Background */
    .stApp {
        background: linear-gradient(rgba(10, 5, 20, 0.88), rgba(35, 10, 50, 0.88)), 
                    url("https://images.unsplash.com/photo-1508739773434-c26b3d09e071?q=80&w=1200&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f1f1f1;
    }

    /* Headings */
    h1 {
        color: #ff5500 !important;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff5500, 2px 2px 5px #000;
        font-family: 'Trebuchet MS', 'Arial', sans-serif;
        text-align: center;
        margin-bottom: 0px !important;
    }

    h2, h3 {
        color: #bb86fc !important;
        text-shadow: 0 0 8px #8a2be2;
    }

    p, label {
        color: #e0e0e0 !important;
        font-weight: bold;
    }

    /* Container Styling */
    .stForm, div[data-testid="stExpander"], div[data-testid="stVerticalBlock"] > div.stElementContainer > div[data-testid="stMarkdownContainer"] {
        border-radius: 20px !important;
    }
    
    .stForm, div[data-testid="stExpander"] {
        background-color: rgba(20, 10, 30, 0.85) !important;
        padding: 25px !important;
        border: 2px solid #8a2be2 !important;
        box-shadow: 0 0 25px rgba(138, 43, 226, 0.6), inset 0 0 15px rgba(255, 85, 0, 0.2);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #ff5500, #8a2be2) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 30px !important;
        border: 2px solid #ffaa00 !important;
        padding: 10px 24px !important;
        width: 100%;
        box-shadow: 0 0 15px #ff5500;
        transition: all 0.3s ease-in-out;
    }
    
    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 25px #8a2be2, 0 0 10px #ff5500;
        color: #ffeb3b !important;
    }

    /* Large Glowing Emojis Banner */
    .spooky-emoji-banner {
        text-align: center;
        font-size: 55px;
        margin: 15px 0;
        text-shadow: 0 0 15px #ff5500, 0 0 25px #8a2be2;
    }
    </style>
""", unsafe_allow_html=True)

# 3. GLOBAL SHARED DATA STORAGE
@st.cache_resource
def get_global_requests():
    return []

requests_queue = get_global_requests()

# 4. List of available songs
SONGS = [
    "ABBA - Dancing Queen",
    "Adele - Someone Like You",
    "Aerosmith - Crazy",
    "Aerosmith - I don't want to miss a thing",
    "Alejandro Sanz - Corazón partío",
    "Amy Winehouse feat. Mark Ronson - Valerie",
    "Andrés Calamaro - Flaca",
    "Aqua - Barbie Girl",
    "Backstreet boys - I want it that way",
    "Black Eyed Peas - I Gotta Feeling",
    "Bon Jovi - It's my life",
    "Bon Jovi - Livin' on a Prayer",
    "Britney Spears - Baby One More Time",
    "Britney Spears - Toxic",
    "Britney Spears - Oops! I did it again",
    "Bruno Mars - The Lazy Song",
    "Camilo Sesto - Vivir así es morir de amor",
    "Chutci - Samaya",
    "Eminem feat Rihanna - Love The Way You Lie",
    "Enanitos verdes - Lamento boliviano",
    "Evanescence - Bring Me to Life",
    "Evanescence - My Inmortal",
    "Frank Sinatra - My Way",
    "Gayle - Abcdefu",
    "Green Day - Boulevard of Broken Dreams",
    "Guns N' Roses - Sweet Child O'Mine",
    "James Blunt - You're Beautiful",
    "Jason Mraz - I'm yours",
    "John Legend - All of Me",
    "José José - El triste",
    "Katy Perry - Hot N Cold",
    "Lady GaGa - Alejandro",
    "Lady GaGa - Bad Romance",
    "Lady Gaga - Poker Face",
    "Lagy gaga & Bruno Mars - Die with a smile",
    "Linkin Park - In The End",
    "Linkin Park - Numb",
    "Marc Anthony - Ahora quien (salsa)",
    "Maroon 5 - She Will Be Loved",
    "Mena Massoud, Naomi Scott - A Whole New World",
    "Michael Jackson - Smooth Criminal",
    "Michel Teló - Ai Se Eu Te Pego",
    "Natasha Bedingfield - Unwritten",
    "Nirvana - Smells Like Teen Spirit",
    "O-Zone - Dragostea din teï",
    "Queen - Bohemian Rhapsody",
    "Queen - Don't Stop Me Now",
    "Queen - I Want to Break Free",
    "Queen - We Are the Champions",
    "Queen - We Will Rock You",
    "Radiohead - Creep",
    "Rufus Wainwright - Hallelujah (Shrek version)"
    "Slipknot - Snuff",
    "Slawomir - Milosc w Zakopanem",
    "The Beatles - Yesterday",
    "The Cranberries - Zombie",
    "Tommy Cash - Espresso Macchiato",
    "Vlad Topalov - Kak zhe tak mozhet byt",     
    
]

# 5. Header Banner
st.markdown("<h1 style='font-size: 42px;'>🎃 Spooky Karaoke Night 🎤</h1>", unsafe_allow_html=True)

# Pure Spooky Emoji Banner
st.markdown("<div class='spooky-emoji-banner'>🦇 🎃 💀 🕷️ 🕯️ 🕸️ 🧛</div>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; font-size: 19px; color: #ffaa00 !important; margin-bottom: 25px;'>"
    "🕷️ Summon your track, grab the mic, and wake the dead! 👻</p>",
    unsafe_allow_html=True
)

# 6. Song Request Form
with st.form("spooky_karaoke_form", clear_on_submit=True):
    st.subheader("🕸️ Claim Your Spotlight")
    
    name = st.text_input("🧙‍♂️ Your Name / Stage Name:")
    selected_song = st.selectbox("🎶 Select Your Song:", ["-- Select a song --"] + SONGS)
    
    st.write("---")
    
    # Track Mode Selection
    track_mode = st.radio(
        "🎧 Performance Mode:",
        [
            "🎤 Pure Karaoke (Instrumental only)", 
            "🎙️ Sing-Along (Original song with vocals)"
        ],
        index=0
    )
    
    submitted = st.form_submit_button("🔥 Send Song Request!")

if submitted:
    if not name.strip():
        st.error("⚠️ Please enter your name before submitting!")
    elif selected_song == "-- Select a song --":
        st.error("⚠️ Please pick a song from the list!")
    else:
        requests_queue.append({
            "Name": name.strip(),
            "Song": selected_song,
            "Mode": track_mode
        })
        st.balloons()
        st.success(
            f"🎉 **Awesome pick, {name}!** You selected **{selected_song}** ({track_mode}). Get ready to hit the stage!"
        )

# 7. Public Live Queue (Visible to all guests)
st.divider()
st.subheader("📜 Live Singer Queue & Playlist")

if len(requests_queue) > 0:
    df_public = pd.DataFrame(requests_queue)
    # Add 1-based index numbering for performance order
    df_public.index = range(1, len(df_public) + 1)
    st.dataframe(df_public, use_container_width=True)
else:
    st.info("👻 No song requests yet. Be the first to take the stage!")

# 8. Host Admin Panel (For resetting/clearing queue)
st.divider()
with st.expander("🔐 Host / Admin Panel"):
    st.write("Access the host controls:")
    
    admin_form = st.form("admin_login_form")
    password = admin_form.text_input("Enter Admin Password:", type="password")
    admin_login = admin_form.form_submit_button("🔑 Enter Admin Panel")

    if admin_login:
        if password == "Karaoke2026":
            st.session_state["karaoke_admin_logged_in"] = True
        else:
            st.session_state["karaoke_admin_logged_in"] = False
            st.error("Incorrect password.")

    if st.session_state.get("karaoke_admin_logged_in", False):
        st.success("Access Granted, Host!")

        if len(requests_queue) > 0:
            if st.button("🗑️ Reset / Clear Singer Queue"):
                requests_queue.clear()
                st.success("Singer queue has been cleared!")
                st.rerun()
        else:
            st.info("Queue is currently empty.")
