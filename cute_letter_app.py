import streamlit as st
import random
import math
from datetime import datetime

st.set_page_config(page_title="Letter from Lisa 💌", layout="centered")

# CSS styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffe6f2 0%, #ffcceb 100%);
    }
    .main {
        background: linear-gradient(135deg, #ffe6f2 0%, #ffcceb 100%);
    }
    .stContainer {
        background: #ffe6f2;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #ff4d94;'>💌 Letter from Lisa 💌</h1>", unsafe_allow_html=True)

# Ask for name
if "name" not in st.session_state:
    with st.form("name_form"):
        name_input = st.text_input("ใส่ชื่อเล่นของคุณตรงนี้เลยยย 💕:", value="", placeholder="ชื่อของคุณ")
        submitted = st.form_submit_button("✨ ตกลง ✨")
        
        if submitted:
            if name_input.strip():
                st.session_state.name = name_input
                st.session_state.opened = False
                st.rerun()
            else:
                st.session_state.name = "คนน่ารัก"
                st.session_state.opened = False
                st.rerun()
else:
    name = st.session_state.name
    
    # Envelope animation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"<h2 style='text-align: center;'>📮 มีจดหมายให้ {name} 📮</h2>", unsafe_allow_html=True)
        
        # Button to open letter
        if not st.session_state.get("opened", False):
            if st.button("🎀 คลิกเพื่อเปิดจดหมาย 🎀", key="open_btn", use_container_width=True):
                st.session_state.opened = True
                st.rerun()
        
        # Show letter
        if st.session_state.get("opened", False):
            # Envelope flap animation
            st.markdown("""
                <div style='text-align: center; font-size: 48px; margin: 20px 0;'>
                    📬 ✨ 📬
                </div>
            """, unsafe_allow_html=True)
            
            # Letter content with flowers
            st.markdown(f"""
                <div style='background: white; border-radius: 15px; padding: 30px; 
                            box-shadow: 0 4px 15px rgba(255, 77, 148, 0.3); 
                            border: 2px solid #ffb3d9; text-align: center;'>
                    
                    <div style='font-size: 24px; margin-bottom: 20px;'>🌸 🌺 🌼 🌷 ✨ 💖 🌸</div>
                    
                    <h3 style='color: #ff4d94;'>สวัสดี {name}! 👋</h3>
                    
                    <p style='color: #333; font-size: 16px; line-height: 1.8;'>
                        ขอให้วันนี้เป็นวันที่ดี<br>
                        สดใสเหมือนดอกไม้พวกนี้นะ<br>
                        ยิ้มเยอะๆ ล่ะ 😊
                    </p>
                    
                    <div style='font-size: 24px; margin: 20px 0;'>🌸 🌺 🌼 🌷 ✨ 💖 🌸</div>
                    
                    <p style='color: #ff4d94; font-size: 18px; font-style: italic;'>
                        รัก,<br>
                        ลิซ่า 💕
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Flower animations with emojis
            st.markdown("""
                <div style='text-align: center; margin-top: 30px; font-size: 32px;'>
                    <div style='animation: bounce 1s infinite;'>🌸</div>
                    <div style='animation: bounce 1s infinite 0.2s;'>🌺</div>
                    <div style='animation: bounce 1s infinite 0.4s;'>🌼</div>
                    <div style='animation: bounce 1s infinite 0.6s;'>🌷</div>
                    <div style='animation: bounce 1s infinite 0.8s;'>✨</div>
                    <div style='animation: bounce 1s infinite 1s;'>💖</div>
                    
                    <style>
                        @keyframes bounce {
                            0%, 100% { transform: translateY(0); }
                            50% { transform: translateY(-20px); }
                        }
                    </style>
                </div>
            """, unsafe_allow_html=True)
            
            # Reset button
            if st.button("🔄 เปิดอีกครั้ง", key="reset_btn", use_container_width=True):
                st.session_state.opened = False
                st.rerun()
            
            if st.button("✏️ เปลี่ยนชื่อ", key="change_name_btn", use_container_width=True):
                del st.session_state.name
                st.rerun()
    
    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ff4d94;'>Made with 💖 by Lisa</p>", unsafe_allow_html=True)
