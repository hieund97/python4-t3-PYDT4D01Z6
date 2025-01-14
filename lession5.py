import streamlit as st


name = st.text_input("Nhập tên học sinh: ")
birth_day = st.text_input("Nhập ngày sinh: ")
subject = st.text_input("Nhập môn học: ")
hobies = st.text_input("Nhập sở thích: ")

st.title("Giới thiệu bản thân")
st.write(f"Họ và tên: {name}")
st.write(f"Ngày sinh: {birth_day}")
st.write(f"Môn học yêu thích: {subject}")
st.write(f"Sở thích: {hobies}")