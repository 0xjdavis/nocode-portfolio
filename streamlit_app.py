import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header
from streamlit_extras.card import card
import base64

# Page config
st.set_page_config(page_title="AI Designer Portfolio", page_icon="🎨", layout="wide")

# Custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Navigation
def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    st.components.v1.html(nav_script)

# Header
st.markdown("<h1 class='main-title'>AI-Powered Design Innovation</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Bridging the gap between stunning visuals and cutting-edge AI</p>", unsafe_allow_html=True)

# Navigation menu
menu = ["Home", "Projects", "Skills", "Contact"]
choice = st.selectbox("Menu", menu, key="nav")

if choice == "Projects":
    nav_page("Projects")
elif choice == "Skills":
    nav_page("Skills")
elif choice == "Contact":
    nav_page("Contact")

# About Me
colored_header(
    label="About Me",
    description="A brief introduction",
    color_name="blue-70"
)

st.markdown("""
As a product designer with a passion for AI, I bring a unique blend of creativity and technical expertise to every project. 
My journey from crafting pixel-perfect designs to developing neural networks has equipped me with a holistic understanding of both form and function.

I specialize in creating AI-powered applications that are not only intelligent but also intuitive and visually captivating. 
My mission is to push the boundaries of what's possible at the intersection of design and artificial intelligence.
""")

# Featured Project
colored_header(
    label="Featured Project",
    description="Highlight of recent work",
    color_name="blue-70"
)

card(
    title="AI-Powered Design Assistant",
    text="An intelligent tool that assists designers in creating harmonious color schemes and layouts",
    image="https://via.placeholder.com/600x400.png?text=AI+Design+Assistant",
    url="#"
)

# Call to Action
st.markdown("<div class='cta-container'>", unsafe_allow_html=True)
st.button("View All Projects", key="view_projects")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p class='footer'>© 2023 Your Name. All rights reserved.</p>", unsafe_allow_html=True)
