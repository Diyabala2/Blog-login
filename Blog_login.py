import streamlit as st
def app():
	st.title("Login page")
	st.text_input("Username:")
	p=st.text_input("Password:")
	pa="Diya12"

	if st.button("Submit"):
		if p==pa:
	 	 st.success("Successfully logged in!")
		if p !=pa:
		 st.info("Try Again!")
 


