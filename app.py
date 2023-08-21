# app.py
import streamlit as st

def main():
    st.title("Мое первое приложение Streamlit")
    st.write("Привет, это мое первое приложение с помощью Streamlit!")
    col1, col2, col3 = st.columns(3)

    with col1:
    	st.header("A cat")
   	st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
	st.header("A dog")
	st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
	st.header("An owl")
	st.image("https://static.streamlit.io/examples/owl.jpg")

if __name__ == "__main__":
    main()

