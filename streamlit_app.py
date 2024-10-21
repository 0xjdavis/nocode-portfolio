import streamlit as st
from streamlit_card import card
import base64

# Set page config
st.set_page_config(page_title="AI Engineer Portfolio", page_icon="🎨🤖", layout="wide")

# Custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Header
st.markdown("<h1 class='gradient-text'>From Pixels to Neurons: My AI Journey</h1>", unsafe_allow_html=True)
st.subheader("A Creative AI Engineer's Portfolio")

# About Me
st.markdown("## About Me")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/300x300.png?text=Your+Image+Here", width=300)
with col2:
    st.markdown("""
    👋 Hello! I'm [Your Name], a graphic designer who fell in love with the world of AI.
    
    🎨 My background in design gives me a unique perspective on AI development, allowing me to create
    intuitive and visually appealing AI solutions.
    
    🤖 Now, I'm on a mission to blend creativity with cutting-edge AI technology to build innovative
    applications that are not only powerful but also beautiful and user-friendly.
    """)

# Skills
st.markdown("## Skills")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Design")
    st.markdown("- Adobe Creative Suite")
    st.markdown("- UI/UX Design")
    st.markdown("- Visual Communication")
    st.markdown("- Brand Identity")
with col2:
    st.markdown("### AI & Programming")
    st.markdown("- Python")
    st.markdown("- Machine Learning")
    st.markdown("- Deep Learning")
    st.markdown("- Computer Vision")
    st.markdown("- Natural Language Processing")

# Projects
st.markdown("## Projects")
col1, col2 = st.columns(2)

with col1:
    card(
        title="AI Art Generator",
        text="A Streamlit app that generates AI art using GANs",
        image="https://via.placeholder.com/300x200.png?text=AI+Art+Generator",
        url="https://your-streamlit-app-url.com",
    )
    st.markdown("[GitHub Repo](https://github.com/yourusername/ai-art-generator)")

with col2:
    card(
        title="Sentiment Analysis Dashboard",
        text="Real-time sentiment analysis of social media posts",
        image="https://via.placeholder.com/300x200.png?text=Sentiment+Analysis",
        url="https://your-streamlit-app-url.com",
    )
    st.markdown("[GitHub Repo](https://github.com/yourusername/sentiment-analysis)")

# Add more projects as needed

# Contact
st.markdown("## Let's Connect!")
st.markdown("""
- 📧 Email: your.email@example.com
- 🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)
- 💼 LinkedIn: [Your Name](https://www.linkedin.com/in/yourprofile)
- 🐙 GitHub: [yourusername](https://github.com/yourusername)
""")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
