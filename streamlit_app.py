import streamlit as st
from st_on_hover_tabs import on_hover_tabs
import streamlit as st

st.set_page_config(layout="wide")

st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
        tabs = on_hover_tabs(tabName=['Dashboard', 'Money', 'Economy'], 
                             iconName=['dashboard', 'money', 'economy'],
                             styles = {'navtab': {'background-color':'#111',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       },
                             key="1")

if tabs =='Dashboard':
    st.title("Navigation Bar")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Money':
    st.title("Paper")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Economy':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))
    

# Page config
st.set_page_config(page_title="Apple Vision Pro", page_icon="🥽", layout="wide")

# Custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Hero Section
parallax_hero(
    background_image="https://www.apple.com/v/apple-vision-pro/a/images/overview/hero/hero_startframe__cb662mbguk6e_large.jpg",
    height="100vh",
    text="Apple Vision Pro",
    subtext="Welcome to the era of spatial computing."
)

# Introduction
st.markdown("&lt;h2 class='apple-h2'&gt;Apple Vision Pro&lt;/h2&gt;", unsafe_allow_html=True)
st.markdown("&lt;p class='apple-p'&gt;Apple Vision Pro seamlessly blends digital content with your physical space. You can explore new worlds while staying present in yours, and do things you never thought possible — all in a way that's natural, intuitive, and magical.&lt;/p&gt;", unsafe_allow_html=True)

# Video Section
st.video("https://www.apple.com/105/media/us/apple-vision-pro/2023/7e268c13-eb22-493d-a860-f0637bacb569/anim/foundation-digital-canvas/large.mp4")

# Features Section
st.markdown("&lt;h3 class='apple-h3'&gt;Featuring&lt;/h3&gt;", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://www.apple.com/v/apple-vision-pro/a/images/overview/intro/hardware_base__ecl2v43j73o2_large.jpg", use_column_width=True)
    st.markdown("&lt;p class='feature-text'&gt;Revolutionary dual-chip design&lt;/p&gt;", unsafe_allow_html=True)
with col2:
    st.image("https://www.apple.com/v/apple-vision-pro/a/images/overview/intro/eyesight__fo87cv0zkgia_large.jpg", use_column_width=True)
    st.markdown("&lt;p class='feature-text'&gt;Groundbreaking EyeSight feature&lt;/p&gt;", unsafe_allow_html=True)
with col3:
    st.image("https://www.apple.com/v/apple-vision-pro/a/images/overview/intro/spatial_experiences__bukix9ufzu82_large.jpg", use_column_width=True)
    st.markdown("&lt;p class='feature-text'&gt;Immersive spatial experiences&lt;/p&gt;", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("&lt;p class='footer'&gt;© 2023 Apple Inc. All rights reserved.&lt;/p&gt;", unsafe_allow_html=True)
