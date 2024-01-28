from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load our env variables
load_dotenv()

# OpenAI initialisation
openai.api_key = os.environ["APP_OPENAI_API_KEY"]

# Setup Flask app
app = Flask(__name__)

# Define the home page route
@app.route("/")
def home():
    return render_template("index.html")

# Define the chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # pass

    # Get the message from the user input
    user_input = request.form["message"]
    # Use OpenAI to generate a response
    prompt = f'User: {user_input}\nChatbot: '
    chat_history = []
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        stop=["\nUser: ", "\nChatbot: "]
    )

    # Extract text from the OpenAI response:
    bot_response = response.choices[0].text.strip()

    # Add chat response and user input to the chat history:
    chat_history.append(f"User: {user_input}\nChatbot: {bot_response}")

    return render_template(
        "chatbot.html",
        user_input=user_input,
        bot_response=bot_response
    )