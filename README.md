# 🏦 Bank Management System (The Bank of AK)

A simple prototype banking application built using **Streamlit**. This app allows users to:

- Create and manage bank accounts
- Deposit and withdraw funds
- Update account information
- View and delete account details

---

## 🚀 Features

- ✅ Create a new bank account with a 4-digit PIN
- 💰 Deposit or withdraw money with validation
- 👁️ View account details securely
- 🔄 Update account name, email, or PIN
- ❌ Delete an existing account

---

## 📂 Project Structure

```bash
.
├── backend.py         # Handles all the banking logic and data storage
├── frontend.py        # Streamlit app (main UI)
├── data.json          # Stores account data (auto-created)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
````

---

## 🧑‍💻 How to Use the App

1. Launch the app with Streamlit.
2. Use the sidebar to navigate between:

   * Create Account
   * Deposit Money
   * Withdraw Money
   * View/Update/Delete Account
3. All data is stored in a local JSON file (`data.json`).

---

## 🛠️ Installation Instructions

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/7hecoder/bank-management-system.git
cd bank-management-system
```

### 🐍 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🚀 4. Run the App

```bash
streamlit run frontend.py
```

This will open the app in your browser at `http://localhost:8501`.

---

## 📋 Dependencies

Only installable packages are included in `requirements.txt`. Sample content:

```
streamlit==1.15.0
```

---

## ⚠️ Disclaimer

This is a **prototype app** that stores data **locally** and is **not secure** for production or real banking use. Do not use real personal data or credentials.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**AK**
GitHub: [@7hecoder](https://github.com/7hecoder)
