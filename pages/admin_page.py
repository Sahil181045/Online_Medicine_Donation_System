from dependencies import st, hide_icons, hide_sidebar, remove_whitespaces
from pages.admin_pages.approve_donations import approve_donations
from pages.admin_pages.view_donations import view_donations

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

selected = st.selectbox("", ("Approve Donations", "View Donations"), label_visibility="hidden")
st.write("####")

if selected == "Approve Donations":
    approve_donations()
if selected == "View Donations":
    view_donations()
