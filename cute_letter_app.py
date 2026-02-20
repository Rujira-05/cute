import streamlit as st
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="มีจดหมายมาส่ง 💌", page_icon="💌")

# ตกแต่งด้วย CSS ให้ดูน่ารักมุ้งมิ้ง
st.markdown("""
<style>
    /* เปลี่ยนสีพื้นหลัง */
    .stApp {
        background-color: #ffe6f2;
    }
    /* แต่งกล่องข้อความจดหมาย */
    .letter-box {
        background-color: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(255, 102, 179, 0.2);
        border: 3px dashed #ffb3d9;
        text-align: center;
        font-size: 22px;
        color: #555;
        margin-top: 20px;
        animation: fadeIn 2s;
    }
    /* หัวข้อ */
    .cute-title {
        color: #ff4d94;
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    /* ซองจดหมาย */
    .envelope {
        text-align: center;
        font-size: 120px;
        margin: 40px 0;
        cursor: pointer;
        transition: transform 0.3s;
    }
    .envelope:hover {
        transform: scale(1.1);
    }
    /* แอนิเมชันตอนจดหมายปรากฏ */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# เก็บสถานะของจดหมาย
if "name" not in st.session_state:
    st.session_state.name = ""
if "opened" not in st.session_state:
    st.session_state.opened = False

# ส่วนรับชื่อเล่น - แสดงเฉพาะถ้ายังไม่มีชื่อ
if not st.session_state.name:
    st.markdown('<div class="cute-title">💌 จดหมายมาส่ง 💌</div>', unsafe_allow_html=True)
    name_input = st.text_input("ใส่ชื่อเล่นของคุณตรงนี้เลยยย 💕:", placeholder="พิมพ์ชื่อตรงนี้...")
    
    if name_input:
        st.session_state.name = name_input
        st.session_state.opened = False
        st.rerun()
else:
    name = st.session_state.name
    
    # แสดงหัวข้อ
    st.markdown(f'<div class="cute-title">💌 มีจดหมายจาก ลิซ่า ถึง {name} 💌</div>', unsafe_allow_html=True)
    
    # แสดงซองจดหมายหรือข้อความจดหมาย
    if not st.session_state.opened:
        # แสดงซองจดหมาย
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="envelope">📮</div>', unsafe_allow_html=True)
            if st.button("กดตรงนี้เพื่อเปิดซองจดหมาย 🌸", use_container_width=True, key="open_btn"):
                st.session_state.opened = True
                st.rerun()
    else:
        # แสดงเนื้อหาจดหมาย
        st.balloons()
        
        # หน่วงเวลาให้ดูตื่นเต้นนิดนึง
        with st.spinner('กำลังเปิดจดหมาย...'):
            time.sleep(1.5)
        
        st.markdown(f"""
        <div class="letter-box">
            <p>สวัสดี <b>{name}</b>! 🌷</p>
            <p>มองไรงะ<br>มีปัญหาเบ๋อ<br>ยังอีก😊</p>
            <br>
            <p style="color: #ff4d94;"><b>รัก,<br>ลิซ่า 💖</b></p>
        </div>
        """, unsafe_allow_html=True)
        
       

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff4d94;'>Made with 💖 by Lisa</p>", unsafe_allow_html=True)
