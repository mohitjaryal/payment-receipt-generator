# 🧾 Payment Receipt Generator (Python + GUI)

A professional and beginner-friendly **Python-based GUI application** to generate clean and structured **payment receipts in PDF format**. Built using **Tkinter** for the interface and **ReportLab** for PDF generation.

---

## 🚀 Features

* 🪟 Simple and user-friendly GUI
* 📄 Generates PDF receipts instantly
* 🧾 Includes:

  * Customer Name
  * Product Name
  * Quantity
  * Price
  * Payment Method
  * Auto-generated Date & Time
* 📂 Saves receipts automatically in the `output/` folder
* ⚡ Lightweight and fast

---

## 🛠️ Tech Stack

* **Python 3**
* **Tkinter** (GUI)
* **ReportLab** (PDF generation)

---

## 📁 Project Structure

```
payment-receipt-generator/
│
├── src/
│   ├── gui.py
│   ├── receipt.py
│
├── output/
│   └── recipt_*.pdf
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/payment-receipt-generator.git
cd payment-receipt-generator
```

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install reportlab
```

---

## ▶️ Run the Application

```bash
python3 src/gui.py
```

---

## 📄 Output

* Generated receipts are saved in:

```
output/
```

* File format:

```
recipt_<timestamp>.pdf
```

---

## 💡 Future Improvements

* Dropdown for Payment Method (Cash / UPI / Card)
* Auto calculation of total price
* Multiple items support (cart system)
* Logo & branding in PDF
* Export to Excel

---

## 👨‍💻 Author

**Mohit Jaryal**
🌐 Website: https://mohitjaryal.online

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
