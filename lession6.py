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