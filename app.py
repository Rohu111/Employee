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
        print("\nEmployee Found!")
        print("ID: ",ID)
        print("Name: ",employ[ID]["name"])
        print("Designation: ",employ[ID]["designation"])
