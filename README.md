# Fraud-Detictor
# 🏦 Bank Fraud Detection System

A simple CLI-based system to manage customers, handle transactions, and detect possible fraud based on predefined rules for each customer type.

---

## ✨ Features

- Register new customers with different subscription types:
  - Personal
  - Business
  - Foreign resident
- Save customer data automatically.
- Handle and save all transaction data individually.
- Detect potential fraudulent transactions based on specific business rules.
- Organized structure for easy expansion and GUI integration later.

---

## 📁 Project Structure

├── main.py                       ← الملف الأساسي لتشغيل البرنامج
├── data_manager.py              ← لتسجيل العملاء وحفظ بياناتهم ومعاملاتهم
├── user_types.py                ← الكلاسات الأربعة الخاصة بأنواع العملاء
│
├── customers.json               ← قاعدة بيانات العملاء (تُنشأ تلقائيًا)
├── transactions_101.json        ← ملف معاملات خاص بالعميل رقم 101 (تلقائي)


---

## 🛠 Technologies

- Python 3
- JSON (for data storage)
- Object-Oriented Programming (OOP)
- Abstract Classes
- (Optional future) GTK 3 for GUI

---

## 🚀 How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/fraud_detection_project.git
    cd fraud_detection_project
    ```

2. Run the program:
    ```bash
    python main.py
    ```

---

## 🧠 Future Improvements

- Add password management for user login.
- Implement a full graphical interface using GTK 3.
- Create a dashboard to view transactions history.
- Implement real-time fraud alert system.
