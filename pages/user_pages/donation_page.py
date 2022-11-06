def donation_page():

    from dependencies import st, Image, date
    from dependencies import users
    from classes.donation import Donation

    user_email = st.session_state.email
    active_user = users.find_one({"email": user_email})

    st.subheader("We encourage donors not to purchase new medicines as our endeavour \
        is to increase impact by reducing waste")

    def clear_form():
        st.session_state["medicine_name"] = ""
        st.session_state["expiry_date"] = date.today()
        st.session_state["quantity"] = ""
        st.session_state["collection_time"] = date.today()

    st.markdown("---")

    col1, col2 = st.columns([2, 3])
    med_list = ["Common acute bacterial, viral and parasitic infections",
                "Chronic diseases like hypertension, diabetes, heart disease etc.",
                "Respiratory conditions", "Gastrointestinal diseases", "Allergies",
                "Skin Conditions", "Aches and Pains", "Cold relief", "Neurological diseases"]

    do_not_donate = ["Liquids", "Injectables", "Ayurvedic or Homeopathic medicines",
                     "Narcotics or psychotropic drugs"]

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
        with st.form("donation_form"):
            st.write("User Details")
            name = st.text_input(
                "Name", placeholder=active_user["first_name"]+" "+active_user["last_name"], disabled=True)
            phone = st.text_input(
                "Phone Number", placeholder=active_user["phone"], disabled=True)
            email = st.text_input(
                "Email Address", placeholder=active_user["email"], disabled=True)

            st.markdown("---")
            st.write("Donation Details")
            medicine_name = st.text_input("Medicine Name", key="medicine_name")
            expiry_date = st.date_input("Expiry Date", key="expiry_date")
            quantity = st.text_input("Quantity", key="quantity")
            collection_time = st.date_input(
                "Collection Time", key="colletion_time")
            donate_button = st.form_submit_button(label="Donate")
            clear_button = st.form_submit_button(
                label="Clear Form", on_click=clear_form)

        if donate_button:
            n_errors = 0

            if medicine_name == "":
                st.error("Medicine name is a required field!")
                n_errors += 1
            if quantity == "":
                st.error("Quantity is a required field!")
                n_errors += 1
            elif not float(quantity).is_integer():
                st.error("Quantity must be an integer!")
                n_errors += 1
            elif int(quantity) <= 0:
                st.error("Quantity must be greater than 0!")
                n_errors += 1
            if expiry_date == "":
                st.error("Expiry date is a required field!")
                n_errors += 1
            if collection_time == "":
                st.error("Collection time is a required field!")
                n_errors += 1
            if expiry_date < collection_time:
                st.error("Collection time must be prior to the expiry date")
                n_errors += 1
            if collection_time <= date.today() or expiry_date <= date.today():
                st.error(
                    "Collection time and Expiry date must be past the current date")
                n_errors += 1

            if n_errors == 0:
                user_id = active_user["_id"]
                donation = Donation(user_id, medicine_name,
                                    str(expiry_date), int(quantity), str(collection_time))
                donation.donate_medicine()
                st.success(
                    "Donation Successful!\nYou can view your donations and approval status in User Donation History.")

    st.markdown("---")
