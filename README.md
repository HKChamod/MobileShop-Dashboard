# 📱 MobileShop-Dashboard

MobileShop-Dashboard is a **desktop admin dashboard** built with **Python (PyQt6)** and **Matplotlib**.  
It’s designed for managing a **mobile phone shop**, allowing the admin to manage products, customers, and view analytics in a clean, modern UI with **dark/light theme support**.

---

## ✨ Features

- **Dashboard Overview**
  - Quick stats on sales, orders, and customers.
- **Product Management**
  - Add, edit, delete products.
  - Data table with price & stock tracking.
- **Customer Management**
  - Search, filter, and manage customers.
  - Filter by name, email, phone, or purchase count.
- **Analytics**
  - Monthly sales bar chart.
  - Best-selling brand pie chart.
- **Theme Manager**
  - Toggle between **light** 🌞 and **dark** 🌙 modes.
  - Charts update styling automatically with theme changes.
- **Settings Page**
  - Manage app preferences.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MobileShop-Dashboard.git
   cd MobileShop-Dashboard
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt** should include:
   ```
   PyQt6
   matplotlib
   ```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📂 Project Structure

```
MobileShop-Dashboard/
│── main.py              # Entry point with UI and logic
│── README.md            # Project documentation
│── requirements.txt     # Dependencies
```

---

## 🚀 Roadmap / Next Steps

- [ ] Add database integration (SQLite or MongoDB).  
- [ ] Implement authentication system.  
- [ ] Export reports (PDF/Excel).  
- [ ] Improve analytics with more charts.  

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to improve UI/UX, optimize performance, or add new features, feel free to fork and submit.

