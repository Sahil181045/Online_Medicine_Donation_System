def approve_donations():

    from dependencies import st
    from dependencies import donations, users
    from classes.admin import Admin

    donations_list = list(donations.find())
    n = len(donations_list)

    st.header("Approve Donations")

    cols = st.columns(8)
    fields = ["Sr No.", "Username", "Phone No.", "Medicine name",
              "Expiry date", "Quantity", "Collection time", "Actions"]

    st.markdown("---")
    for col, field in zip(cols, fields):
        col.write("**"+field+"**")

    count = 0
    for i in range(n):
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        if donations_list[i]["approval_status"] == "Pending":
            count += 1
            col1.write(count)
            user = users.find_one({"_id": donations_list[i]["user_id"]})
            col2.write(user["first_name"]+" "+user["last_name"])
            col3.write(user["phone"])
            col4.write(donations_list[i]["medicine_name"])
            col5.write(donations_list[i]["expiry_date"])
            col6.write(donations_list[i]["quantity"])
            col7.write(donations_list[i]["collection_time"])
            with col8:
                placeholder_accept = st.empty()
                placeholder_reject = st.empty()
                clicked_accept = placeholder_accept.button("Approve", key="ACC-"+str(i))
                clicked_reject = placeholder_reject.button("Reject", key="REJ-"+str(i))

                if clicked_accept:
                    donation_id = donations_list[i]["_id"]
                    Admin.approve_donation(donation_id, "Approved")
                    placeholder_accept.empty()
                    placeholder_reject.empty()
                    placeholder_accept.write("Approved")

                if clicked_reject:
                    donation_id = donations_list[i]["_id"]
                    Admin.approve_donation(donation_id, "Rejected")
                    placeholder_accept.empty()
                    placeholder_reject.empty()
                    placeholder_accept.write("Rejected")

            st.markdown("---")
