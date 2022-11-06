def user_donation_history():

    from dependencies import st
    from dependencies import users, donations

    user_email = st.session_state.email
    active_user = users.find_one({"email": user_email})
    user_id = active_user["_id"]
    search_query = {"user_id": user_id}

    user_donations_list = list(donations.find(search_query))
    n = len(user_donations_list)

    st.header("Donation History")

    cols = st.columns(6)
    fields = ["Sr No.", "Medicine name", "Expiry date",
              "Quantity", "Collection time", "Approval status"]

    st.markdown("---")

    for col, field in zip(cols, fields):
        col.write("**"+field+"**")

    for i in range(n):
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.write(str(i+1))
        col2.write(user_donations_list[i]["medicine_name"])
        col3.write(user_donations_list[i]["expiry_date"])
        col4.write(user_donations_list[i]["quantity"])
        col5.write(user_donations_list[i]["collection_time"])
        col6.write(user_donations_list[i]["approval_status"])
        st.markdown("---")
