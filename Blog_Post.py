import streamlit as st

def app():
	st.title("Education")
	st.write("Today I am going to be talking about education! Our life revolves around education and its important that we know that! Many kids might not like going to school, but lots of children around the world dream of having an opprutunity to learn. Every kid should have the right to learn! Everybody should be grateful for having an amazing life! Not many people around the world are blessed for a happy life!")
	st.sidebar.slider("Rate the blog",1, 10)
	st.sidebar.selectbox("Would you recommend it?", ("Yes", "No"))
	if st.sidebar.button("Submit Opinion"):
		st.sidebar.success("Your opinion was recorded! Thank you!")
	st.text_input("Feedback:")
	if st.button("Submit Feedback"):
	  	st.success("You have submitted your feedback! Thank you for your time!")
