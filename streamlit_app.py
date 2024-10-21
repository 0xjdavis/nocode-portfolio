import streamlit as st
import streamlit_card as stcard
from streamlit_timeline import timeline
from streamlit_lottie import st_lottie
import requests
import json

# Page config
st.set_page_config(page_title="AI Designer Portfolio", page_icon="🎨🤖", layout="wide")

# Custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Hero Section
st.markdown("<div class='hero'>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("<h1 class='gradient-text'>AI-Powered Design Innovation</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Bridging the gap between stunning visuals and cutting-edge AI</p>", unsafe_allow_html=True)
with col2:
    st_lottie(lottie_coding, height=300, key="coding")
st.markdown("</div>", unsafe_allow_html=True)

# About Me
st.markdown("## About Me")
st.markdown("""
As a product designer with a passion for AI, I bring a unique blend of creativity and technical expertise to every project. 
My journey from crafting pixel-perfect designs to developing neural networks has equipped me with a holistic understanding of both form and function.

I specialize in creating AI-powered applications that are not only intelligent but also intuitive and visually captivating. 
My mission is to push the boundaries of what's possible at the intersection of design and artificial intelligence.
""")

# Timeline
st.markdown("## My Journey")
timeline_data = [
    {"id": 1, "title": "Started as a Product Designer", "content": "Began my career creating user-centric designs for various digital products", "year": "2015"},
    {"id": 2, "title": "Discovered AI", "content": "Became fascinated with the potential of AI in design and started learning", "year": "2018"},
    {"id": 3, "title": "Transition to AI Engineering", "content": "Started applying AI concepts to enhance design processes and user experiences", "year": "2020"},
    {"id": 4, "title": "AI-Powered Design Innovation", "content": "Now creating cutting-edge applications that blend beautiful design with powerful AI capabilities", "year": "Present"}
]
timeline(timeline_data, height=400)

# Skills
st.markdown("## Skills")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Design")
    st.markdown("""
    <div class="skill-bar">
        <div class="skill" style="width:95%;">UI/UX Design 95%</div>
    </div>
    <div class="skill-bar">
        <div class="skill" style="width:90%;">Visual Communication 90%</div>
    </div>
    <div class="skill-bar">
        <div class="skill" style="width:85%;">Prototyping 85%</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("### AI & Programming")
    st.markdown("""
    <div class="skill-bar">
        <div class="skill" style="width:85%;">Python 85%</div>
    </div>
    <div class="skill-bar">
        <div class="skill" style="width:80%;">Machine Learning 80%</div>
    </div>
    <div class="skill-bar">
        <div class="skill" style="width:75%;">Deep Learning 75%</div>
    </div>
    """, unsafe_allow_html=True)

# Projects
st.markdown("## Projects")
col1, col2 = st.columns(2)

with col1:
    stcard.card(
        title="AI-Powered Design Assistant",
        text="An intelligent tool that assists designers in creating harmonious color schemes and layouts",
        image="https://via.placeholder.com/300x200.png?text=AI+Design+Assistant",
        url="https://your-streamlit-app-url.com",
    )
    st.markdown("[GitHub Repo](https://github.com/yourusername/ai-design-assistant)")

with col2:
    stcard.card(
        title="Generative Art Platform",
        text="A platform that uses GANs to create unique, AI-generated artworks based on user inputs",
        image="https://via.placeholder.com/300x200.png?text=Generative+Art+Platform",
        url="https://your-streamlit-app-url.com",
    )
    st.markdown("[GitHub Repo](https://github.com/yourusername/generative-art-platform)")

# Contact Form
st.markdown("## Let's Connect")
contact_form = """
<form action="https://formsubmit.co/your@email.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Social Links
st.markdown("""
<div class="social-links">
    <a href="https://twitter.com/yourhandle" target="_blank"><i class="fab fa-twitter"></i></a>
    <a href="https://linkedin.com/in/yourprofile" target="_blank"><i class="fab fa-linkedin"></i></a>
    <a href="https://github.com/yourusername" target="_blank"><i class="fab fa-github"></i></a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p class='footer'>© 2023 Your Name. All rights reserved.</p>", unsafe_allow_html=True)
