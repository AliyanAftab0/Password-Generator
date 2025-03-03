# Password Generator 🔐

## Overview
The **Password Generator** is a simple yet powerful web application built using **Streamlit**. It allows users to generate secure, random passwords based on customizable options such as length, uppercase letters, numbers, and special characters.

## Features
- Select password length (1-100 characters)
- Include uppercase letters
- Include numbers
- Include special characters
- Secure password generation using the `secrets` module
- User-friendly interface built with Streamlit

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/AliyanAftab0/password-generator.git
   cd password-generator
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the Streamlit app using the following command:
```sh
streamlit run app.py
```

This will open the password generator in your web browser.

## Technologies Used
- **Python**: Backend logic
- **Streamlit**: Web application framework
- **Secrets**: Secure password generation
- **String Module**: Character sets for password customization

## Screenshots
![Password Generator UI](screenshot.png)  

## Contributing
If you have ideas for improvements, feel free to **fork this repository** and submit a pull request.

## Contact
Developed by **Aliyan Aftab**  
[LinkedIn](www.linkedin.com/in/aliyan-aftab-b95b962b4)

## License
This project is licensed under the **MIT License**.

