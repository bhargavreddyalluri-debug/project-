import streamlit as st
import requests

BACKEND_URL = "https://project-bgre.onrender.com"

email = st.text_input(
    "Email",
    placeholder="Enter email to update"
)

name = st.text_input(
    "Name",
    placeholder="Enter new name"
)

password = st.text_input(
    "Password",
    placeholder="Enter new password",
    type="password"
)

if st.button("Confirm Update"):

    if not email or not name or not password:
        st.warning("Please fill all fields")

    else:
        update_data = {
            "name": name,
            "password": password
        }

        try:
            res = requests.put(
                f"{BACKEND_URL}/update_user/{email}",
                json=update_data
            )

            if res.status_code == 200:
                res_json = res.json()
                st.success(res_json)
            else:
                st.error(
                    f"Update failed. Status code: {res.status_code}"
                )

        except requests.exceptions.RequestException as error:
            st.error(f"Could not connect to backend: {error}")