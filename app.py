from dependencies import st, switch_page, Image, hide_icons, hide_sidebar, remove_whitespaces

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

st.title("Online Medicine Donation System")
st.subheader("Select Your Role")

col1, col2 = st.columns(2)
user_img = Image.open("images/useravatar.png")
with col1:
    st.image(user_img, output_format="jpg", width=230)
    clicked_user = st.button("User")

admin_img = Image.open("images/adminavatar.png")
with col2:
    st.image(admin_img, output_format="jpg", width=230)
    clicked_admin = st.button("Admin")

if clicked_user:
    st.session_state.profile = "user"
    switch_page("login")
elif clicked_admin:
    st.session_state.profile = "admin"
    switch_page("login")
