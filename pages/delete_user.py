import streamlit as st
import requests

BACKEND_URL = "https://project-bgre.onrender.com"

email = st.text_input(
    "Email",
    placeholder="Enter email to delete"
)

if st.button("Confirm Delete"):

    if not email:
        st.warning("Please enter an email")

    else:
        try:
            res = requests.delete(
                f"{BACKEND_URL}/delete_user/{email}"
            )

            if res.status_code == 200:
                st.success(res.json())
            else:
                st.error(
                    f"Delete failed. Status code: {res.status_code}"
                )

        except requests.exceptions.RequestException as error:
            st.error(f"Could not connect to backend: {error}")