from ..dependencies import st, switch_page
from ..classes.client import *

st.header("Registration Details")

col1, col2 = st.columns(2)
with col1:
    first_name = st.text_input("First name")
with col2:
    last_name = st.text_input("Last name")

col1, col2 = st.columns([3, 1])
with col1:
    email = st.text_input("E-mail")
with col2:
    phone = st.text_input("Phone number")

address = st.text_area("Address")

col1, col2 = st.columns(2)
with col1:
    password = st.text_input("Password", type="password")
with col2:
    confirm_password = st.text_input("Confirm password", type="password")

clicked = st.button("Register")
clicked_login = st.button("Already registered? Click here to login!")

if clicked_login:
    switch_page("login")

if clicked:
    if first_name == "":
        st.error("First name is a required field!")
    if last_name == "":
        st.error("Last name is a required field!")
    if email == "":
        st.error("E-mail is a required field!")
    if address == "":
        st.error("Address is a required field!")
    if phone == "":
        st.error("Phone number is a required field!")
    if password == "":
        st.error("Password is a required field!")
    if password != confirm_password:
        st.error("Password and Confirm password must be same!")
    if len(password) < 6:
        st.error("Password must be atleast 6 characters long!")

    else:
        client = Client(email, password, first_name,
                        last_name, phone, address)
        result = client.register()

        if result == "already_exists":
            st.error("User already exists!")
        else:
            st.success("Registration successful!")
