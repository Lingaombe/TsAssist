# 📄 T'sAssist

**T'sAssist** is a role-based web application system that streamlines the creation and management of dynamic question papers. Designed for educational institutions, it allows teachers to upload questions, generate exams, and manage question banks; all while giving HoDs and examiners administrative control.

---

## 🚀 Features

* 🧑‍🏫 **Teachers**

  * Upload questions manually or via Excel
  * Generate question papers based on course, pattern, and marks
  * Manage and edit own question bank

* 👩‍💼 **HoD (Head of Department)**

  * Manage courses and department-level teachers
  * Review and delete used or flagged questions
  * Receive alerts when questions are running low

* 🧑‍⚖️ **Examiner**

  * Cross-department access to all papers
  * Print and review generated question papers

* ⚙️ **Question Management**

  * Separate handling for different question types (MCQ, SA, LA, etc.)
  * Duplicate prevention via `used` status
  * Flagging and deletion workflows

---

## 📚 Tech Stack

* **Frontend:** HTML, CSS, JavaScript with Jinja templating (Flask)
* **Backend:** Flask (Python)
* **Database:** MySQL
* **Auth:** JWT / Session-based
* **File Upload:** Excel (.xlsx) parser
* **APIs:** RESTful endpoints for role-based actions

---

## 🖼️ Pages

| Role     | Pages                                                         |
| -------- | ------------------------------------------------------------- |
| All      | Login                                                         |
| Teacher  | Dashboard, Upload Questions, Manage Questions, Generate Paper |
| HoD      | Dashboard, Add Courses, Manage Teachers, Delete Questions     |
| Examiner | Dashboard, Generate & Print Papers                            |

---

## 📂 Folder Structure (Suggested)

```
T'sAssist/
├── app.py                  # Flask entry point
├── config.py               # App configuration
├── models/                 # SQLAlchemy models
├── routes/                 # Flask route handlers
├── controllers/            # Business logic
├── templates/              # Jinja2 templates (HTML pages)
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   └── js/
├── utils/                  # Helper functions, file parsers, etc.
├── requirements.txt        # Python dependencies pip freeze>requirements.txt
├── README.md
└── .env                    # Environment configuration (.gitignore this)
```
---

## 🛠️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/Lingaombe/TsAssist.git
cd TsAssist
````

### 2. Install Dependencies

* Backend (Flask + MySQL)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file with necessary variables. Remember to `.gitignore` it.

```env
# Example (.env)
FLASK_APP=app.py
FLASK_ENV=development
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=paperforge
JWT_SECRET=your-secret-key
```

### 4. Run the App

```bash
flask run
```

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

[MIT](LICENSE)

---

## ✨ Acknowledgements

Thanks to educators and curriculum designers who inspired this tool.
