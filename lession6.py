"""
huy: https://huy-ict-app.streamlit.app/
the nghi: https://thenghiicantech.streamlit.app/
hieu: https://ict-mhieu-python-4.streamlit.app/
"""


import streamlit as st

st.set_page_config(page_title="Bài hát yêu thích", page_icon=":smile:", layout="wide")

with st.sidebar:
    img_path = "https://vcdn1-giaitri.vnecdn.net/2019/07/03/sontungmtp-1562144392-2006-1562144411.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=KA3cbHW_fed0Z-ErY8pEmA"
    st.image(img_path, caption="Sơn Tùng M-TP")
    st.write("Họ và tên: Nguyễn Thanh Tùng")
    st.write("Nghệ danh: Sơn Tùng M-TP")
    st.write("Nguyễn Thanh Tùng, thường được biết đến với nghệ danh Sơn Tùng M-TP, là một nam ca sĩ kiêm sáng tác nhạc, nhà sản xuất thu âm, rapper và diễn viên người Việt Nam. Nổi tiếng vì tầm ảnh hưởng sâu rộng đối với âm nhạc Việt Nam, anh được mệnh danh là 'Hoàng tử V-pop' bởi Giải thưởng Âm nhạc Thế giới và BroadwayWorld.")


st.title("Bài hát yêu thích")
st.write("Đừng làm trái tim anh đau - Sơn Tùng MTP")

st.audio("dlttad.mp3", format="audio/mp3")

st.title("MV yêu thích")

st.video("https://www.youtube.com/watch?v=abPmZCZZrFA", format="video/mp4")