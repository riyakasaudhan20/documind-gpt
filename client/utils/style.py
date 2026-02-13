import streamlit as st

def apply_custom_style():
    st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%); color: #ffffff; }
h1 { color: #00d2ff; font-family: 'Inter', sans-serif; font-weight: 800; text-shadow: 0px 4px 10px rgba(0, 210, 255, 0.3); }
[data-testid="stSidebar"] { background-color: rgba(30, 30, 47, 0.8); border-right: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); }
.stExpander, .stChatMessage { background: rgba(255, 255, 255, 0.05) !important; border-radius: 15px !important; border: 1px solid rgba(255, 255, 255, 0.1) !important; box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1) !important; backdrop-filter: blur(5px) !important; }
.stChatInputContainer { padding-bottom: 20px; }
.stButton > button { background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%); color: white; border: none; border-radius: 10px; font-weight: 600; transition: all 0.3s ease; }
.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0, 210, 255, 0.3); border: none; color: white; }
.stToast { background-color: #1e1e2f !important; color: #00d2ff !important; border: 1px solid #00d2ff !important; }
</style>
""", unsafe_allow_html=True)
