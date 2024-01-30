import streamlit as st

def press():
    st.write('you werent suppposed to press that')
    st.button('no', key=1, disabled=True)

def love():
    with cent_co:
        st.write('yipeee‼️❤️💐😘')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('valentinegato.png', width=300)
    st.button('yes', key=2, on_click=love)

st.button('no',key=1, on_click=press)


