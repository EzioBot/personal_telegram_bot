# 🤖 Personal Telegram Bot

A simple yet powerful **personal Telegram bot** built using Python, designed to automate messaging, store user input, and provide real-time responses.  
This project was developed as a learning + productivity tool using **ChatGPT, Manus AI, and Python Telegram Bot API**.

---

## 🚀 Features

- ⚡ Real-time message response (no manual refresh needed)
- 💾 Stores user messages/data locally or in file/database (based on configuration)
- 🔁 Continuous polling for instant interaction
- 🧠 AI-assisted logic (optional integration with ChatGPT / Manus AI)
- 🧩 Easy to extend with new commands and features
- 🔐 Secure token handling using `.env`

---

## 🛠️ Tech Stack

- Python 3.x
- `python-telegram-bot` library
- dotenv (`.env` support)
- Manus AI (for logic/automation ideas)
- ChatGPT (for development, debugging, and architecture design)

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/EzioBot/personal_telegram_bot.git
cd personal_telegram_bot
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / Mac:**
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root directory:

```env
BOT_TOKEN=your_telegram_bot_token_here
```

You can get your token from 👉 @BotFather on Telegram.

---

## ▶️ Run the Bot

```bash
python main.py
```

Once running, your bot will be active and respond instantly on Telegram.

---

## 💡 How This Project Was Built

This project was developed step-by-step using a combination of:

### 1. Telegram Bot Setup
- Created bot using **@BotFather**
- Retrieved API token
- Connected using `python-telegram-bot`

### 2. Core Development
- Built message handlers (start, echo, custom commands)
- Implemented real-time polling system
- Added message storage system (file/database optional)

### 3. AI Assistance
- Used **ChatGPT** for:
  - Code structure design
  - Debugging errors
  - Feature planning
- Used **Manus AI** for:
  - Automation ideas
  - Workflow optimization
  - Bot logic improvement

### 4. Testing
- Tested locally on Windows machine
- Verified real-time Telegram responses
- Iteratively improved stability and speed

---

## 📁 Project Structure

```
personal_telegram_bot/
│── main.py
│── bot.py (or handlers.py)
│── requirements.txt
│── .env
│── README.md
│
├── data/
│   └── stored_messages.json (optional)
│
└── utils/
    └── helper_functions.py
```

---

## 📌 Example Commands

- `/start` → Start the bot
- `/help` → Show available commands
- Any message → Bot stores/replies automatically

---

## 🧠 Future Improvements

- 🌐 Deploy to cloud (Railway / Render / VPS)
- 🗄️ Add database support (SQLite / PostgreSQL)
- 🤖 Integrate full ChatGPT API replies
- 📊 Add analytics dashboard
- 👥 Multi-user role system

---

## ☁️ Deployment (Free Options)

If you're a student looking for free hosting:

- Render (free tier available)
- Railway (limited free credits)
- PythonAnywhere (basic free plan)
- Replit (easy but sleeps after inactivity)

---

## 📚 Resources Used

- https://core.telegram.org/bots/api
- https://github.com/python-telegram-bot/python-telegram-bot
- https://docs.python.org/3/
- OpenAI ChatGPT for development support
- Manus AI for workflow assistance

---

## 👨‍💻 Author

**Ezio**  
Student & Developer  
Focused on AI, automation, and practical software projects.

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub and feel free to fork it for your own bot ideas.