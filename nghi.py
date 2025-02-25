import streamlit as st
list_options1 = ["Gỏi bò bóp thấu", "Gỏi Thái hải sản chua cay"]
list_options2 = ["Bò nướng kim tiền","Bò tơ cuộn rau rừng", "Lẩu bò kim chi"]
list_options3 = ["Chè đậu các loại", "Bánh chuối nướng", "Chè dừa dầm"]
with st.form("thực đơn"):
    st.title("thực đơn")
    khaivi = st.multiselect("Chọn món khai vị", list_options1)
    monchinh = st.multiselect("Chọn món chính", list_options2)
    trangmieng = st.multiselect("tráng miệng", list_options3)
    submitted = st.form_submit_button("submit")
    if submitted:
        st.write("các món bạn chọn là:")
        st.write("Món khai vị:")
        if len(khaivi) == 0:
            st.write("Bạn chưa chọn món khai vị")
        else:
            for i in range(len(khaivi)):
                st.write(khaivi[i])
        st.write("Món chính:")
        if len(monchinh) == 0:
            st.write("Bạn chưa chọn món chính")
        else:
            for i in range(len(monchinh)):
                st.write(monchinh[i])
        st.write("tráng miệng:")
        if len(trangmieng) == 0:
            st.write("Bạn chưa chọn món tráng miệng")
        else:
            for i in range(len(trangmieng)):
                st.write(trangmieng[i])
    
