
# MobilePing - Telegram Notification on Program Launch

**MobilePing** is a Python project that sends an instant and customizable notification to a Telegram bot every time the program is launched. This is a simple way to track app starts, log activity, or trigger remote alerts via Telegram.

## Features

- **Instant notifications** to a Telegram bot upon program launch.
- Easy setup process with clear steps for configuring the Telegram bot.
- Option to package your script as an executable for convenience.

## Requirements

- Python 3.x
- Telegram bot and chat ID (steps outlined below).
- auto-py-to-exe (*Optional*)

## Setup

### 1. Set up Telegram Bot

To send notifications to your Telegram bot, follow these steps to get your API token and chat ID.

#### API Token:
1. Find the Telegram bot named `@botfather`. This bot helps you create and manage your Telegram bots.
2. To create a new bot, type `/newbot` or click on it, and follow the instructions to create your bot.
3. Once created, you will receive a new API token. Example: `12442114:AAHfsqhsKH8WeS2zSpoQ7_r5TMLOroHm9B0`.

#### Chat ID:
1. Search for the bot called `@getidsbot` on Telegram.
2. Press the "Start" button or type `/start`.
3. Copy the ID displayed in the chat (Example: `337125646`).

### 2. Configure Your Script

In your `mobileping.py` file, define the following variables with your API token and chat ID:

```python
apiToken = 'YOUR_BOT_API_TOKEN'
chatID = 'YOUR_CHAT_ID'
```

Replace `'YOUR_BOT_API_TOKEN'` and `'YOUR_CHAT_ID'` with the actual values you obtained in the previous steps.

### 3. Run the Script

To run the script, execute the following command in your terminal:

```bash
python mobileping.py
```

Alternatively, to make the script easier to run, you can convert it into an executable using **auto-py-to-exe**.

---

## Packaging the Script into an Executable

### 1. Install `auto-py-to-exe`

You can install `auto-py-to-exe` via PyPI:

```bash
$ pip install auto-py-to-exe
```

### 2. Convert the Script

To package your script into an executable, follow these steps:

1. Open a terminal and execute the following command:

    ```bash
    $ auto-py-to-exe
    ```

2. The application window will appear. Follow these steps:
    - Select the location of your script (use a file explorer or paste the path).
    - The outline will turn blue if the file exists.
    - Customize additional options like adding an icon or including extra files.
    - Click the large blue button at the bottom to convert the script.

3. After conversion, find your executable in the `/output` folder.

---

## Contributing

Feel free to fork this repository and contribute by creating a pull request. If you have any suggestions or improvements, open an issue or submit a pull request.
