import streamlit as st

st.set_page_config(page_title="Form chọn món ăn", layout="wide")
# nếu phiên hoạt động không có phiên student

if 'meal' not in st.session_state:
    st.session_state.meal = [] # phiên hoạt động
    

khai_vi = ["Salad", "Nộm", "Rượu vang", "Sasimi"]
mon_chinh = ["Cua hoàng đế", "Tôm hùm alaska", "Bào ngư", "Vi cá"]
trang_mieng = ["Hoa quả", "kem", "Sữa chua", "nước trái cây", "bánh"]
mon_ngau_nhien = ["Bún", "Miến", "Phở"]

text= "Xin chào đây là nội dung bạn đã download được"
st.download_button("Download", text)



with st.form(key="str", clear_on_submit=False):
    st.title("Form chọn món ăn: ")

    slider = st.slider("Chọn bàn ăn", min_value=1, max_value=20, value=2)
    
    options_khai_vi = st.multiselect("Chọn món khai vi", khai_vi)
    options_mon_chinh = st.multiselect("Chọn món chính", mon_chinh)
    options_trang_mieng = st.multiselect("Chọn món tráng miệng", trang_mieng)
    option_ngau_nhien = st.selectbox("Chọn món ngẫu nhiên", mon_ngau_nhien)
    
    agree = st.checkbox("Đồng ý")
    
    
    submited = st.form_submit_button("Gửi lên")
    if submited:
        if options_khai_vi and options_mon_chinh and options_trang_mieng and option_ngau_nhien and slider and agree :
            st.session_state.meal.append(
                {
                    "so_ban": slider,
                    "khai_vi": options_khai_vi,
                    "mon_chinh": options_mon_chinh,
                    "trang_mieng": options_trang_mieng,
                    "ngau_nhien": option_ngau_nhien,
                }
            )
            st.success("Chọn món thành công")
        else:
            st.warning("Bạn cần nhập đầy đủ thông tin")
        
count_meal = len(st.session_state.meal)
if count_meal > 0: # nếu có món ăn
    cols = st.columns(count_meal)
    
    for i in range(count_meal):
        with cols[i]:
            st.title(f"Món thứ {i + 1}")
            st.write(f"Số bàn: {st.session_state.meal[i]['so_ban']}")
            st.write(f"Món khai vị: {','.join(st.session_state.meal[i]['khai_vi'])}")
            st.write(f"Món chính: {','.join(st.session_state.meal[i]['mon_chinh'])}")
            st.write(f"Món tráng miệng: {','.join(st.session_state.meal[i]['trang_mieng'])}")
            st.write(f"Món ngẫu nhiên: {st.session_state.meal[i]['ngau_nhien']}")
    
