"""
1. Chuẩn bị và đăng ký đề tài cuối khoá
2. Lịch trình cho buổi tuần sau:
    + Về nhà làm bài cuối khoá
    + Có 1 giờ để hoàn thiện bài cuối khoá
    + 30p cuối để thuyết trình về bài của mình
    
Hiếu: Website về khủng long
Thế Nghi: Website đặt phòng khách sạn
Huy: Dự báo thời tiết

"""

import streamlit as st

st.set_page_config(page_title="Đặt đồ uống", layout="wide")

list_do_uong = ["Nước trái cây", "trà sữa", "coca", "pepsi"]
list_duong = ["Đường trắng", "Đường mía", "Đường ăn kiêng"]
list_thach =  ["THạch rau câu", "Thạch trân châu", "Thạch sợi"]

thong_tin_hoa_don = ''

with st.form(key="str", clear_on_submit=False):
    st.title("Đặt đồ uống")
    
    do_uong = st.selectbox("Bạn muốn đặt đồ uống gì", list_do_uong)
    duong = st.selectbox("Bạn muốn thêm loại đường nào: ", list_duong)
    thach = st.selectbox("Bạn muốn thêm loại thạch nào: ", list_thach)
    
    so_luong = st.slider("Số lượng",min_value=1, max_value=50, value=1)
    
    submited = st.form_submit_button("Đặt")
    
    if submited:
        if do_uong and duong and thach and so_luong:
            thong_tin_hoa_don = f"Đồ uống: {do_uong} \n Đường: {duong} \n Thạch: {thach} \n Số lượng: {so_luong}"
            st.write(thong_tin_hoa_don)
            st.success("Chọn món thành công")
        else:
            st.warning("Bạn cần nhập đầy đủ thông tin")

in_hoa_don = st.checkbox("In hoá đơn")

if in_hoa_don:
    st.download_button("Tải xuống hoá đơn", thong_tin_hoa_don)
