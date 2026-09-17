import streamlit as st
import requests

# Deployed FastAPI backend
BACKEND_URL = "https://project-bgre.onrender.com"


if st.button("Createuser"):
    st.switch_page("pages/create_user.py")


if st.button("GetUsers"):
    res = requests.get(f"{BACKEND_URL}/get_all_users")

    if res.status_code == 200:
        res_json = res.json()
        st.dataframe(res_json)
    else:
        st.error(f"Failed to get users: {res.status_code}")


if st.button("DeleteUser"):
    st.switch_page("pages/delete_user.py")


if st.button("UpdateUser"):
    st.switch_page("pages/update_user.py")