import streamlit as st
import base64
    
def get_base64(image_path):
    print(image_path)
    with open(image_path, "rb") as img:  
      return base64.b64encode(img.read()).decode()

logo = get_base64("logo.png")


def header_home():
    st.markdown (f"""
    <div style="display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    margin-bottom:30px;">
        <img src="data:image/png;base64,{logo}"
        width="120">
            <h1 style="text-align:center; color:white;
        margin-top:10px;">
               SNAP<br>CLASS
            </h1>
          </div>
          """,unsafe_allow_html=True)             

def header_dashboard():
    st.markdown (f"""
        <div style="display:flex; justify-content:center; align-items:center; gap:15px;
        margin-bottom:20px;">
            <img src="data:image/png;base64,{logo}"
        width="80">    
            <h2 style="color:#5865F2; margin:0;">
              SNAP<br>CLASS
        </h2>
      </div>  
          """, unsafe_allow_html=True)

