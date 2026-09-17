import streamlit as st
import requests

BACKEND_URL = "https://project-bgre.onrender.com"

st.title("Create User Form")

with st.form("Create_user"):
    n = st.text_input("Name", placeholder="Enter name here")
    e = st.text_input("Email", placeholder="Enter email here")
    p = st.text_input("Password", placeholder="Enter password here", type="password")
    c_p = st.text_input(
        "Confirm Password",
        placeholder="Enter password again",
        type="password"
    )

    r = st.selectbox(
        "Choose role :- ",
        ["Recruiter", "JobSeeker"]
    )

    btn = st.form_submit_button("Create User")

    if btn:

        if p != c_p:
            st.error("Passwords do not match")

        elif not n or not e or not p:
            st.error("Please fill all required fields")

        else:
            new_user = {
                "name": n,
                "email": e,
                "password": p,
                "role": r
            }

            try:
                res = requests.post(
                    f"{BACKEND_URL}/create_user",
                    json=new_user
                )

                if res.status_code == 200:
                    st.success(res.json()["msg"])
                else:
                    st.error(
                        f"Something went wrong. Status code: {res.status_code}"
                    )

            except requests.exceptions.RequestException as error:
                st.error(f"Could not connect to backend: {error}")