import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pymongo
import certifi
from PIL import Image
from datetime import date
import unittest

USER_NAME = st.secrets["db_username"]
PASSWORD = st.secrets["db_password"]
myclient = pymongo.MongoClient(
    f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.1zktl9j.mongodb.net/test", tlsCAFile=certifi.where())
omds = myclient["omds"]
users = omds["users"]
admins = omds["admins"]
medicines = omds["medicines"]
donations = omds["donations"]


def hide_icons():
    hide_st_style = """
				<style>
				#MainMenu {visibility: hidden;}
				footer {visibility: hidden;}
				</style>"""
    st.markdown(hide_st_style, unsafe_allow_html=True)


def hide_sidebar():
    no_sidebar_style = """
    			<style>
        		div[data-testid="stSidebarNav"] {visibility: hidden;}
    			</style>"""
    st.markdown(no_sidebar_style, unsafe_allow_html=True)


def remove_whitespaces():
    st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>""", unsafe_allow_html=True)
