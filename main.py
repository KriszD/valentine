import streamlit as st

def love():
    with cent_co:
        st.write('yipeee‼️❤️💐😘')
        st.image('cha.jpg', width=150)

left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image('valentinegato.png', width=300)
    st.write('will you be my valentine? :3')
    st.button('yes', key=2, on_click=love)

st.button('no', disabled=True)
