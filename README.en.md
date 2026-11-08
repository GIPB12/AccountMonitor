# AccountMonitor

**Account expiration and access monitoring system developed in Python.**

[🇧🇷 Português](README.md) | [🇺🇸 English](README.en.md)

## About the project

**AccountMonitor** is a Python automation tool designed to monitor account expiration dates recorded in an Excel spreadsheet.

The system reads the records, checks expiration dates, and automatically identifies accounts that are approaching expiration or have already expired.

When records meet the alert criteria, the system sends a single consolidated email containing all identified occurrences.

## Features

- Automatic reading of Excel spreadsheet records
- Identification of accounts approaching expiration
- Identification of expired accounts
- Alerts up to 7 days before expiration
- Consolidated email reports
- Gmail integration via SMTP
- Secure storage of credentials and settings using environment variables

## Monitoring rules

The system identifies three situations:

| Situation | Behavior |
|---|---|
| Approaching expiration | Alerts for accounts expiring within the next 7 days |
| Expires today | Identifies accounts expiring on the current date |
| Expired | Identifies all accounts with an expiration date earlier than the current date |

The report includes the **account login**, expiration date, and the number of days remaining or elapsed since expiration.

For security reasons, account passwords are not included in the email.

## Technologies

- **Python** — automation development
- **OpenPyXL** — Excel spreadsheet reading
- **Python-dotenv** — environment variable management
- **SMTP / Gmail** — email report delivery

## Project structure

```text
AccountMonitor/
│
├── main.py
├── config.py
├── planilha.py
├── email_service.py
│
├── modelos/
│   └── molde.xlsx
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup and execution

### 1. Clone the repository

```bash
git clone REPOSITORY_URL
cd AccountMonitor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory, using `.env.example` as a reference.

Configure the following variables:

```dotenv
# Email Server
SERVER=
PORT=

# Sender Email
EMAIL_SENDER=
APP_PASSWORD=

# Recipient Email
EMAIL_RECIPIENT=

# Spreadsheet
SHEET_FILE=
```

**Important:** Gmail requires an App Password for this SMTP integration. Do not use your regular Google account password.

### 5. Configure the spreadsheet

The spreadsheet must contain the following columns, in this order:

| Column | Description |
|---|---|
| login | Account identifier |
| senha | Account password |
| usuário | User information |
| data criação | Account creation date |
| data expiração | Account expiration date |

Dates must use a format supported by the system.

### 6. Run the application

```bash
python main.py
```

## Security

- Email credentials are stored in a `.env` file
- The `.env` file is excluded from version control
- Account passwords are not included in email reports
- Using fictional data in testing environments is recommended

## Purpose

AccountMonitor was developed to automate expiration monitoring, reduce manual checks, and simplify account and access management through centralized email notifications.

---

Developed with Python.