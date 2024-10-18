from flask import Flask, request
import subprocess
import sys

app = Flask(__name__)

chat_bot_process = None

def start_chat_bot():
    global chat_bot_process
    if chat_bot_process is None or chat_bot_process.poll() is not None:
        print("Starting chat bot application...")
        try:
            chat_bot_process = subprocess.Popen([sys.executable, "shadow.py"])
            print("Chat bot application started.")
        except Exception as e:
            print("Error starting chat bot application:", e)
    else:
        print("Chat bot application is already running.")

def stop_chat_bot():
    global chat_bot_process
    if chat_bot_process is not None and chat_bot_process.poll() is None:
        print("Stopping chat bot application...")
        try:
            chat_bot_process.terminate()
            chat_bot_process = None
            print("Chat bot application stopped.")
        except Exception as e:
            print("Error stopping chat bot application:", e)
    else:
        print("Chat bot application is not running.")

@app.route('/start_chat_bot', methods=['POST'])
def start_chat_bot_route():
    start_chat_bot()
    return '', 204

@app.route('/stop_chat_bot', methods=['POST'])
def stop_chat_bot_route():
    stop_chat_bot()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)  # You can change debug=True to debug=False for production
