import streamlit as st

# Tiêu đề ứng dụng
st.title("Thực Đơn Các Bữa Ăn Trong Ngày")

# Thực đơn cho bữa sáng
st.header("Bữa Sáng")
breakfast_options = ["Xôi", "Bánh mì", "Phở", "Bánh cuốn", "Cháo"]
selected_breakfast = st.multiselect("Chọn món ăn cho bữa sáng:", breakfast_options)

st.header("Bữa Trưa")
main_dishes = ["Thịt kho", "Cá chiên", "Gà xào", "Tôm rang", "Sườn nướng"]
vegetables = ["Rau muống", "Bông cải", "Đậu xanh", "Canh bí", "Canh rau"]
selected_main_dishes_lunch = st.multiselect("Chọn 2 món mặn cho bữa trưa:", main_dishes, max_selections=2)
selected_vegetable_lunch = st.selectbox("Chọn 1 món rau hoặc canh cho bữa trưa:", vegetables)

# Thực đơn cho bữa tối
st.header("Bữa Tối")
selected_main_dishes_dinner = st.multiselect("Chọn 2 món mặn cho bữa tối:", main_dishes, max_selections=2)
selected_vegetable_dinner = st.selectbox("Chọn 1 món rau hoặc canh cho bữa tối:", vegetables)


st.subheader("Thực Đơn Của Bạn")
st.write("Bữa Sáng: ", ", ".join(selected_breakfast) if selected_breakfast else "Chưa chọn món")
st.write("Bữa Trưa: ", ", ".join(selected_main_dishes_lunch) + " và " + selected_vegetable_lunch)
st.write("Bữa Tối: ", ", ".join(selected_main_dishes_dinner) + " và " + selected_vegetable_dinner)

