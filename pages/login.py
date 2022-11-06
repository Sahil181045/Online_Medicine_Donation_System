from dependencies import st, switch_page
from classes.client import *

st.set_page_config(layout="wide")

if st.session_state.profile == "user":
	st.header("User Login")
else:
	st.header("Admin Login")
	
email = st.text_input("E-mail", key="email_login")
password = st.text_input("Password", type="password", key="password_login")
clicked = st.button("Login")
clicked_register = st.button("New user? Click here to register!")

if clicked_register:
	switch_page("register")

if clicked:
	n_errors = 0

	if email == "":
		st.error("E-mail is a required field!")
		n_errors += 1
	if password == "":
		st.error("Password is a required field!")
		n_errors += 1

	if n_errors == 0:
		client = Client(email, password)
		result = client.authenticate()

		if result == "no_user":
			st.error("User does not exist!")
		elif result == "no_admin":
			st.error("Admin does not exist!")
		elif result == "failure":
			st.error("Incorrect password!")
		else:
			st.session_state.email = email
			if st.session_state.profile == "user":
				switch_page("user_page")
			else:
				switch_page("admin_page")
