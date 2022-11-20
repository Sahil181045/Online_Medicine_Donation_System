from dependencies import st, hide_icons, hide_sidebar, remove_whitespaces
from pages.user_pages.donation_page import donation_page
from pages.user_pages.user_donation_history import user_donation_history

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

selected = st.selectbox("", ("Donate Medicine", "View Donation History"), label_visibility="hidden")
st.write("####")

if selected == "Donate Medicine":
    donation_page()
if selected == "View Donation History":
    user_donation_history()
