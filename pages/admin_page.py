from ..dependencies import st, switch_page, users
from ..classes.donation import *

st.header("Approve Donations")

cols = st.columns(7)
fields = ["Sr No.", "User ID", "Medicine name",
          "Expiry date", "Quantity", "Collection time", "Actions"]
for col, field in zip(cols, fields):
    col.write("**"+field+"**")

for i in range(len(donations)):
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.write(i)
    col2.write(donations["user_id"][i])
    col3.write(donations["medicine_name"][i])
    col4.write(donations["expiry_date"][i])
    col5.write(donations["quantity"][i])
    col6.write(donations["collection_time"][i])
    placeholder = col7.empty()
    clicked = placeholder.button("Accept", key=i, type="primary")
