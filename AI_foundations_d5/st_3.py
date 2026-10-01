import streamlit as st
import time

st.set_page_config(page_title="Chat UI Demo")
st.title("Chat UI Demo")

with st.chat_message("assistant"):
    st.write(f"Hello,my name is Alexa! Type somethign to get started.")

user_message=st.chat_input("Type Something...")
if user_message:
    with st.chat_message("user"):
        st.write(user_message)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1.5)
        st.write(f"You said {user_message}. But, I'm still in development. I can't reply yet.")
