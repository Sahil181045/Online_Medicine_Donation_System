import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
omds = myclient["omds"]
users = omds["users"]
medicines = omds["medicines"]
donations = omds["donations"]
