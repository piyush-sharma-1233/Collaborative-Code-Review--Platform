# Collaborative-Code-Review--Platformme

## Getting Started

Follow the steps below to set up and run the project locally:

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.10+
- pip (Python package manager)
- Virtual Environment support

---

### Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/piyush-sharma-1233/Collaborative-Code-Review--Platform.git
   cd Collaborative-Code-Review--Platform
   ```

2. **Create and Activate a Virtual Environment**:
   Create the virtual environment:

   ```bash
   python3.10 -m venv env
   ```

   Activate the virtual environment:

   - On **Windows**:
     ```bash
     . env\Scripts\activate
     ```
   - On **Linux/macOS**:
     ```bash
     source env/bin/activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**:

   - Create database migration files:
     ```bash
     python manage.py makemigrations
     ```
   - Apply the migrations to the database:
     ```bash
     python manage.py migrate
     ```

5. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up an admin account.

6. **Start the Development Server**:

   ```bash
   python manage.py runserver
   ```

   The server will start on `http://127.0.0.1:8000/` by default.

---

### Additional Information

- Navigate to the `master` directory for additional features or submodules.
- Use the Django admin panel to manage users, sessions, and other backend data at `http://127.0.0.1:8000/admin/`.

---
