import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pymongo
from PIL import Image
from datetime import date

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
omds = myclient["omds"]
users = omds["users"]
admins = omds["admins"]
medicines = omds["medicines"]
donations = omds["donations"]