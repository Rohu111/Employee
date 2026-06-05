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

emp_id = st.text_input("Enter Employee ID:")

if st.button("Search"):

    if emp_id in employ:

        st.success("Employee Found!")

        st.write("### Employee Details")
        st.write("**ID:**", emp_id)
        st.write("**Name:**", employ[emp_id]["name"])
        st.write("**Designation:**", employ[emp_id]["designation"])

    else:

        st.error("Employee Not Found!")
