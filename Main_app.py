import streamlit as st

import Blog_Post
import Blog_login

pages_dict = {
                "Blog": Blog_Post,
                "Login": Blog_login,
                
            } 

st.sidebar.title("Navigation")

user_choice = st.sidebar.radio("Go to", tuple(pages_dict.keys()))
if user_choice == "Blog":
    Blog_Post.app() # The 'app()' function should not take any input if the selection option is "Home".
else:
        Blog_login.app()