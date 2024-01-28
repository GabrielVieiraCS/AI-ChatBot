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
    pass
