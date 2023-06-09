
import streamlit as st

# Create a dictionary of hardcoded username-password pairs
credentials = {
    "user1": "password1",
    "user2": "password2"
}

# Add a title to your app
st.title("Login Page")

# Add input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Add a login button
if st.button("Login"):
    # Check if the entered credentials match
    if username in credentials and password == credentials[username]:
        st.success("Logged in as {}".format(username))
        st.write("Hello, World!")  # Display the greeting on successful login
    else:
        st.error("Invalid username or password")
