import streamlit as st
import time


button = st.button("Show Balloon")

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