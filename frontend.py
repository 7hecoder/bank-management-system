import streamlit as st
from backend import Bank

# Load existing data from backend
Bank.load_data()

# Initialize Streamlit interface
st.title("The Bank Of AK")

# Sidebar for navigation
option = st.sidebar.selectbox(
    "Select Action",
    ["Create Account", "Deposit Money", "Withdraw Money", "Account Details", "Update Account", "Delete Account"]
)

# Create Account
if option == "Create Account":
    st.header("Create a New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=120)
    email = st.text_input("Email")
    pin = st.number_input("Pin (4 digits)", min_value=1000, max_value=9999)

    if st.button("Create Account"):
        bank = Bank()
        try:
            account_info = bank.create_account(name, age, email, pin)
            st.success("Account has been created successfully!")
            st.write(account_info)
        except ValueError as e:
            st.warning(str(e))

# Deposit Money
elif option == "Deposit Money":
    st.header("Deposit Money")
    accno = st.text_input("Account Number")
    pin = st.number_input("Pin")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        bank = Bank()
        try:
            result = bank.deposit(accno, pin, amount)
            st.success(result)
        except ValueError as e:
            st.warning(str(e))

# Withdraw Money
elif option == "Withdraw Money":
    st.header("Withdraw Money")
    accno = st.text_input("Account Number")
    pin = st.number_input("Pin")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        bank = Bank()
        try:
            result = bank.withdraw(accno, pin, amount)
            st.success(result)
        except ValueError as e:
            st.warning(str(e))

# Show Account Details
elif option == "Account Details":
    st.header("View Account Details")
    accno = st.text_input("Account Number")
    pin = st.number_input("Pin")

    if st.button("Show Details"):
        bank = Bank()
        try:
            account_info = bank.show_details(accno, pin)
            st.write(account_info)
        except ValueError as e:
            st.warning(str(e))

# Update Account Details
elif option == "Update Account":
    st.header("Update Account Details")
    accno = st.text_input("Account Number")
    pin = st.number_input("Pin")
    new_name = st.text_input("New Name (leave blank to keep same)")
    new_email = st.text_input("New Email (leave blank to keep same)")
    new_pin = st.text_input("New Pin (leave blank to keep same)")

    if st.button("Update Details"):
        bank = Bank()
        try:
            result = bank.update_details(accno, pin, new_name, new_email, new_pin)
            st.success(result)
        except ValueError as e:
            st.warning(str(e))

# Delete Account
elif option == "Delete Account":
    st.header("Delete Account")
    accno = st.text_input("Account Number")
    pin = st.number_input("Pin")

    if st.button("Delete Account"):
        bank = Bank()
        try:
            result = bank.delete_account(accno, pin)
            st.success(result)
        except ValueError as e:
            st.warning(str(e))
