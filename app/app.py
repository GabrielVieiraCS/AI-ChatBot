from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load our env variables
load_dotenv()

app = Flask(__name__)

@app.route("/")