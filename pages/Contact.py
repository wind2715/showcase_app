import streamlit as st
from sendmail import send_mail

st.title("Contact me")
form = st.form(key="form_mails")
with form:
    user_mail = st.text_input("Your email", placeholder="example@gmail.com", key="input_email")
    text_message = st.text_area("Content")
    button = st.form_submit_button("Submit")
    message = f"""\
Subject: HI!
{text_message}
From: {user_mail}
"""
if button:
    send_mail(message)
    st._rerun()

