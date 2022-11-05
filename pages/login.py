from ..dependencies import st, switch_page
from ..classes.client import *

st.header("User Login")
email = st.text_input("E-mail", key="email_login")
password = st.text_input("Password", type="password", key="password_login")
clicked = st.button("Login")
clicked_register = st.button("New user? Click here to register!")

if clicked_register:
    switch_page("register")

if clicked:
    if email == "":
        st.error("E-mail is a required field!")
    if password == "":
        st.error("Password is a required field!")

    else:
        client = Client(email, password)
        result = client.authenticate()

        if result == "no_user":
            st.error("User does not exist!")
        elif result == "failure":
            st.error("Incorrect password!")
        else:
            st.success("Login successful!")
