# Telegram Bot System

This project implements a simple Telegram bot that receives messages, stores them in a SQLite database, performs basic processing, and sends an instant response back to the user.

## 🎯 Objective

- Real-time message reception from users.
- Storage of messages in a database.
- Basic message processing logic.
- Instant response to users.

## ⚙️ Technical Details

- **Language**: Python 3.x
- **Telegram Bot Library**: `python-telegram-bot`
- **Database**: SQLite (local), structured for easy upgrade to PostgreSQL.
- **Environment Management**: `venv` (Python virtual environment)
- **Configuration**: `.env` file for sensitive information like the bot token.

## 🚀 Setup Instructions

Follow these steps to get your Telegram bot up and running:

### 1. Clone the Repository (if applicable)

If you received this project as a repository, clone it to your local machine:

```bash
git clone <repository_url>
cd telegram_bot
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies. This prevents conflicts with other Python projects.

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

- **On macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

- **On Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

### 4. Install Dependencies

Install all required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 5. Obtain Your Bot Token

1. Open Telegram and search for `@BotFather`.
2. Start a chat with BotFather and send the `/newbot` command.
3. Follow the instructions to choose a name and a username for your bot.
4. BotFather will provide you with an API token (e.g., `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`). Copy this token.

### 6. Configure Environment Variables

1. Create a new file named `.env` in the root directory of the project (where `main.py` is located).
2. Open `.env` and add your bot token as follows:

   ```
   TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
   DATABASE_NAME="messages.db"
   ```

   Replace `YOUR_BOT_TOKEN_HERE` with the actual token you obtained from BotFather.
   You can also change `DATABASE_NAME` if you want a different name for your SQLite database file.

### 7. Run the Bot

With the virtual environment activated and dependencies installed, you can now run the bot:

```bash
python main.py
```

The bot will start polling for updates, and you should see log messages in your terminal.

## 🧪 How to Test the Bot

1. **Start a chat with your bot on Telegram.**
2. Send the `/start` command. You should receive a welcome message.
3. Send the `/help` command. You should receive instructions on how to use the bot.
4. Send the message `hello`. The bot should reply with "Message saved! Hi there!"
5. Send any other text message (e.g., "How are you?"). The bot should reply with "Message saved! You said: 'How are you?'"

All messages you send to the bot will be stored in the `messages.db` file (or whatever you named your database) in the project directory.

## 📁 Project Structure

```
telegram_bot/
├── venv/                   # Python virtual environment
├── .env                    # Environment variables (ignored by git)
├── .env.example            # Example for .env file
├── requirements.txt        # Python dependencies
├── main.py                 # Entry point of the bot
├── config.py               # Configuration loading
├── bot/
│   ├── __init__.py
│   └── handlers.py         # Telegram bot command and message handlers
└── database/
    ├── __init__.py
    └── db.py               # Database connection and operations
```

## 📝 Additional Notes

- **Error Handling**: Basic error handling is implemented for database operations and bot token availability.
- **Logging**: Important events (bot startup, message reception, database operations) are logged to the console.
- **Modularity**: The code is structured into separate modules (`config`, `database`, `handlers`) for better organization and future expansion.
- **Database Upgrade**: The database interaction is encapsulated in `database/db.py`, making it easier to switch to a different database system (e.g., PostgreSQL) by modifying only that module.

## 🐳 Docker Deployment

To deploy your bot using Docker for 24/7 operation, follow these steps:

### 1. Ensure Docker and Docker Compose are Installed

Make sure you have Docker and Docker Compose installed on your server. You can find installation instructions on the [official Docker website](https://docs.docker.com/get-docker/).

### 2. Configure Environment Variables

Ensure your `.env` file is correctly configured with your `TELEGRAM_BOT_TOKEN` and `DATABASE_NAME` (as described in "Setup Instructions" above).

### 3. Build and Run with Docker Compose

Navigate to the root directory of your project (where `docker-compose.yml` is located) and run the following command:

```bash
docker compose up -d --build
```

- `docker compose up`: Starts the services defined in `docker-compose.yml`.
- `-d`: Runs the containers in detached mode (in the background).
- `--build`: Builds the Docker image before starting the containers (useful for the first run or after code changes).

Your bot will now be running in a Docker container, restarting automatically if it crashes or the server reboots.

### 4. Stop the Bot (Optional)

To stop the running bot container:

```bash
docker compose down
```

This will stop and remove the containers, but it will preserve your `messages.db` file due to the volume mapping in `docker-compose.yml`.

## 📝 Additional Notes (Docker Specific)

- **Database Persistence**: The `messages.db` file is mounted as a volume, ensuring your data persists even if the Docker container is removed or updated.
- **Automatic Restart**: The `restart: always` policy in `docker-compose.yml` ensures the bot automatically restarts if it stops for any reason.
- **Logging**: Container logs can be viewed using `docker compose logs -f telegram_bot`.
