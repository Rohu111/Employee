import streamlit as st

employ = {
    "101": {
        "name": "Rohan",
        "designation": "CEO"
    },
    "102": {
        "name": "Yoga",
        "designation": "Co-Founder"
    },
    "103": {
        "name": "Lahari",
        "designation": "Head"
    }
}

st.title("Employee Search System")
ID = st.number_input("Enter Employee ID: ")

if st.button("Search"):
    if ID in employ:
        st.write("\nEmployee Found!")
        st.write("ID: ",ID)
        st.write("Name: ",employ[ID]["name"])
        st.write("Designation: ",employ[ID]["designation"])
