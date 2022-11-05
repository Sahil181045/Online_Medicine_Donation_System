from dependencies import st, Image
from dependencies import users
from classes.donation import *

user_email = st.session_state.email
active_user = users.find_one({"email": user_email})

st.set_page_config(layout="wide")

st.write("We encourage donors not to purchase new medicines as our endeavour \
	is to increase impact by reducing waste")

st.markdown("---")

col1, col2 = st.columns([2, 3])
med_list = ["Common acute bacterial, viral and parasitic infections",
            "Chronic diseases like hypertension, diabetes, heart disease etc.",
            "Respiratory conditions", "Gastrointestinal diseases", "Allergies",
            "Skin Conditions", "Aches and Pains", "Cold relief", "Neurological diseases"]

do_not_donate = ["Liquids", "Injectables", "Ayurvedic or Homeopathic medicines",
                 "Narcotics or psychotropic medicines"]

with col1:
    medicine_img = Image.open("images/medicine.png")
    st.image(medicine_img, use_column_width=True)
    st.subheader(
        "You may donate unexpired medicines which can be used to treat:")
    for med in med_list:
        st.write(":white_check_mark:", med)
    st.subheader("Please do not donate:")
    for med in do_not_donate:
        st.write(":x:", med)

with col2:
    with st.form("donation_form", clear_on_submit=True):
        st.write("User Details")
        name = st.text_input(
            "Name", placeholder=active_user["first_name"]+" "+active_user["last_name"], disabled=True)
        phone = st.text_input(
            "Phone Number", placeholder=active_user["phone"], disabled=True)
        email = st.text_input(
            "Email Address", placeholder=active_user["email"], disabled=True)

        st.markdown("---")
        st.write("Donation Details")
        medicine_name = st.text_input("Medicine Name")
        expiry_date = st.date_input("Expiry Date")
        quantity = st.text_input("Quantity")
        collection_time = st.date_input("Collection Time")
        donate_button = st.form_submit_button("Donate")
st.markdown("---")

columns = st.columns((3, 1, 3))
clear_button = columns[1].button("Clear Form")


if donate_button:
    n_errors = 0

    if medicine_name == "":
        st.error("Medicine name is a required field!")
        n_errors += 1
    if quantity == "":
        st.error("Quantity is a required field!")
        n_errors += 1
    if expiry_date == "":
        st.error("Expiry date is a required field!")
        n_errors += 1
    if collection_time == "":
        st.error("Collection time is a required field!")
        n_errors += 1

    if n_errors == 0:
        user_id = active_user["_id"]
        donation = Donation(user_id, medicine_name,
                            str(expiry_date), int(quantity), str(collection_time))
        donation.donate_medicine()
        st.success("Donation successful!")

if clear_button:
    pass
