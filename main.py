import streamlit as st  # For building the web app interface
import string  # For character sets (letters, digits, symbols)
import secrets  # For secure password generation (cryptographically safe)

# Configure the Streamlit page settings
st.set_page_config(page_title="Password Tools", page_icon="🔐", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a page",["Password Strength Checker", "Password Generator"],
)

# Password Strength Checker Page
if page == "Password Strength Checker":
    st.title("Password Strength Checker 💪")
    st.write("Enter a password to check its strength.")

    # Get password input from the user
    password = st.text_input("Enter your password", type="password")
    if st.button("Check"):
        if password:
            st.title("Password Strength")

            # Password strength criteria
            strength = {
                "length": "Minimum 8 characters",
                "uppercase": "At least one uppercase letter",
                "lowercase": "At least one lowercase letter",
                "numbers": "At least one number",
                "special": "At least one special character",
            }

            # Check password strength based on criteria
            if len(password) >= 8:
                st.write(f"✅ {strength['length']}")
            else:
                st.write(f"❌ {strength['length']}")
            if any(char.isupper() for char in password):
                st.write(f"✅ {strength['uppercase']}")
            else:
                st.write(f"❌ {strength['uppercase']}")
            if any(char.islower() for char in password):
                st.write(f"✅ {strength['lowercase']}")
            else:
                st.write(f"❌ {strength['lowercase']}")
            if any(char.isdigit() for char in password):
                st.write(f"✅ {strength['numbers']}")
            else:
                st.write(f"❌ {strength['numbers']}")
            if any(char in string.punctuation for char in password):
                st.write(f"✅ {strength['special']}")
            else:
                st.write(f"❌ {strength['special']}")

# Password Generator Page
elif page == "Password Generator":
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
        # Initialize the character set with lowercase letters
        characters = string.ascii_lowercase

        # Add uppercase letters if checkbox is selected
        if use_uppercase:
            characters += string.ascii_uppercase

        # Add numbers (0-9) if checkbox is selected
        if use_numbers:
            characters += string.digits

        # Add special symbols if checkbox is selected
        if use_special:
            characters += string.punctuation

        # Generate password using cryptographically secure random choices
        password = "".join(secrets.choice(characters) for i in range(length))

        # Display the generated password in a code block for emphasis
        st.title("Your Password")
        st.code(password)  # Shows password in a formatted code box

        # Display a success message
        st.success("Password generated successfully!")


# Footer message with contact link
st.write(
    "Thank you for using the Password Tools! If you have any feedback or suggestions, please feel free to reach out to me on [LinkedIn](www.linkedin.com/in/aliyan-aftab-b95b962b4)."
)
