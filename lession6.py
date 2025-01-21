"""
huy: https://huy-ict-app.streamlit.app/
the nghi: https://thenghiicantech.streamlit.app/
hieu: https://ict-mhieu-python-4.streamlit.app/
"""


import streamlit as st
import time

st.set_page_config(page_title="Thổi bóng bay", page_icon=":smile:", layout="wide")

button = st.button("Thổi bóng bay lên")

if button:
    progress_bar = st.progress(0)
    st.write("Đang xử lý dữ liệu bóng bay . . . . . .")


    percent_complete = 0
    for percent in range(100):
        time.sleep(0.1)
        percent_complete += percent + 10
        if percent_complete > 100:
            percent_complete = 100
        progress_bar.progress(percent_complete)
        if percent_complete == 100:
            st.balloons()
            break

with st.expander("Thực hành"):
    st.write("Đây là thông tin mở rộng")
    
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Đây là cột dành cho mèo")
    st.write("Con mèo")

with col2:
    st.header("Đây là cột dành cho hổ")
    st.write("Con hổ")
    
with col3:
    st.header("Đây là cột dành cho rồng")
    st.write("Con rồng")
    
st.sidebar.write("1. Lời nói đầu")

with st.sidebar:
    st.sidebar.write("2. Mục lục")

image_path = "https://i1-vnexpress.vnecdn.net/2025/01/21/huy-6161-1737434813-3768-1737435120.jpg?w=680&h=0&q=100&dpr=1&fit=crop&s=NYdZpvG8-K_W6p5gg0RMww"
st.image(image_path, caption="Ảnh tên lửa")

st.audio("sample-12s.mp3", format="audio/mp3")