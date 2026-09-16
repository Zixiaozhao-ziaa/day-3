import streamlit as st

st.title("DAY 3")

if "bubble1" not in st.session_state:
    st.session_state.bubble1 = False

if "bubble2" not in st.session_state:
    st.session_state.bubble2 = False

if "bubble3" not in st.session_state:
    st.session_state.bubble3 = False

## if st.session_state.bubble1 is False and st.session_state.bubble2 is False and st.session_state.bubble3 is False:
##    st.write("All bubbles are False")

if st.session_state.bubble1 is False