from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load our env variables
load_dotenv()

# OpenAI initialisation
client = OpenAI(api_key=os.environ["APP_OPENAI_API_KEY"])

# Setup Flask app
app = Flask(__name__)

# Define the home page route
@app.route("/")
def home():
    '''Default API route'''
    return render_template("index.html")

# Define the chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    '''Routes the user to a chat log after posting their initial question'''
    system_prompt = "You are a friendly assistant"
    # Get the message from the user input
    user_input = request.form["message"]
    
    # Generate the user and system prompts for the Chat Completions API
    messages = [
        {"role": "system", "content": f"{system_prompt}"},
        {"role": "user", "content": f"User: {user_input}\nChatbot: "}
    ]

    #Initialise an empty array to later append our chat history
    chat_history = []

    #Generate the response from OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        stop=["\nUser: ", "\nChatbot: "]
    )
    bot_response = response.choices[0].message.content.strip()
    # Add chat response and user input to the chat history:
    chat_history.append(f"User: {user_input}\nChatbot: {bot_response}")

    return render_template(
        "chatbot.html",
        user_input=user_input,
        bot_response=bot_response
    )

# Start Flask app
if __name__ == "__main__":
    app.run(debug=True)