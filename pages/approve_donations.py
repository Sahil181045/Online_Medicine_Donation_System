from dependencies import st
from classes.donation import *
from classes.admin import Admin

donations_list = list(donations.find())
n = len(donations_list)

st.set_page_config(layout="wide")


def perform_action(idx, approval_response):
	donation_id = donations_list[idx]["_id"]
	Admin.approve_donation(donation_id, approval_response)
	st.success("Donation status successfully updated!")


st.header("Approve Donations")

cols = st.columns(8)
fields = ["Sr No.", "User ID", "Medicine name",
		  "Expiry date", "Quantity", "Collection time", "Actions"]
st.markdown("---")
for col, field in zip(cols, fields):
	col.write("**"+field+"**")

for i in range(n):
	col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
	col1.write(str(i+1))
	col2.write(donations_list[i]["user_id"])
	col3.write(donations_list[i]["medicine_name"])
	col4.write(donations_list[i]["expiry_date"])
	col5.write(donations_list[i]["quantity"])
	col6.write(donations_list[i]["collection_time"])
	placeholder_accept = col7.empty()
	placeholder_reject = col8.empty()
	clicked_accept = placeholder_accept.button(
		"Approve", key="ACC-"+str(i), on_click=perform_action, args=[i, "Approved"])
	clicked_reject = placeholder_reject.button(
		"Reject", key="REJ-"+str(i), on_click=perform_action, args=[i, "Rejected"])
	st.markdown("---")
