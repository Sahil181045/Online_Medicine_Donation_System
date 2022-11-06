def view_donations():
    from dependencies import st
    from dependencies import donations, users

    donations_list = list(donations.find())
    n = len(donations_list)

    st.header("Donations")

    cols = st.columns(8)
    fields = ["Sr No.", "Username", "Phone No.", "Medicine name",
              "Expiry date", "Quantity", "Collection time", "Approval status"]

    st.markdown("---")

    for col, field in zip(cols, fields):
        col.write("**"+field+"**")

    for i in range(n):
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        col1.write(str(i+1))
        user = users.find_one({"_id": donations_list[i]["user_id"]})
        col2.write(user["first_name"]+" "+user["last_name"])
        col3.write(user["phone"])
        col4.write(donations_list[i]["medicine_name"])
        col5.write(donations_list[i]["expiry_date"])
        col6.write(donations_list[i]["quantity"])
        col7.write(donations_list[i]["collection_time"])
        col8.write(donations_list[i]["approval_status"])
        st.markdown("---")
