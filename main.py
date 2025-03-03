# Import necessary libraries
import streamlit as st  # For building the web app interface
import string  # For character sets (letters, digits, symbols)
import secrets  # For secure password generation (cryptographically safe)

# Configure the Streamlit page settings
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# Display the main title and welcome message
st.title("Password Generator 🔐")
st.write(
    "Welcome to the Password Generator! Please enter the length of the password you would like to generate."
)

# Get password length from user input (number between 1 and 100, default 12)
length = st.number_input(
    "Password Length", min_value=1, max_value=100, value=12, step=1
)

# Display checkboxes for character type customization
st.write(
    "Please select the character types you would like to include in your password."
)
use_uppercase = st.checkbox("Uppercase Letters")  # Checkbox for uppercase letters
use_numbers = st.checkbox("Numbers")  # Checkbox for numbers
use_special = st.checkbox("Special Characters")  # Checkbox for special symbols

# Button section
st.write("Click the button below to generate your password.")

# When the "Generate Password" button is clicked
if st.button("Generate Password"):
    # Initialize the character set with lowercase AND uppercase letters (default)
    characters = (
        string.ascii_letters
    )  # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Add uppercase letters again if checkbox is selected (note: redundant since they're already included)
    if use_uppercase:
        characters += string.ascii_uppercase  # Adds "ABCDEFGHIJKLMNOPQRSTUVWXYZ" again

    # Add numbers (0-9) if checkbox is selected
    if use_numbers:
        characters += string.digits  # "0123456789"

    # Add special symbols if checkbox is selected
    if use_special:
        characters += string.punctuation  # "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Generate password using cryptographically secure random choices
    password = "".join(secrets.choice(characters) for i in range(length))

    # Display the generated password in a code block for emphasis
    st.title("Your Password")
    st.code(password)  # Shows password in a formatted code box

# Footer message with contact link
st.write(
    "Thank you for using the Password Generator! If you have any feedback or suggestions, please feel free to reach out to me on [LinkedIn](www.linkedin.com/in/aliyan-aftab-b95b962b4)."
)
