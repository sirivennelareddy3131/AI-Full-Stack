import streamlit as st
st.set_page_config(page_title="Text Input Demo",page_icon=".")
st.title("Text input Demo")
st.markdown("""
<style>
.stApp{
background-color:#C8A2C8
}
""",unsafe_allow_html=True)


name=st.text_input("Enter your name::",placeholder="e.g.siri")
st.write(f"Hi,{name}!")

secret=st.text_input("Enter your password:",type="password")
st.write(f"You entered{len(secret)} characters.")

comments=st.text_area("Enter additional comments.",height=150)
st.write(f"You entered {len(comments)} characters.")

if st.button("Submit"):
    st.write("You clicked me...!")

if st.checkbox("Show Additional msg?"):
    st.write("This is the additional message.Have a good day...")
