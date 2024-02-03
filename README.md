# Flask AI-ChatBot

A simple chatbot that leverages `ChatGPT-3.5` in a Flask application.

## Setup

1. Make an `OpenAI` account [here](https://openai.com/).
2. Generate a personal API key for your account.
3. At the `app` level, create a `.env` file an initialise an `APP_OPENAI_API_KEY` environment variable with your own key.
4. In your terminal, run: `flask --app app run`
5. Have fun!

## Helpful resources:

- OpenAI text generation [docs](https://platform.openai.com/docs/guides/text-generation/chat-completions-api).
- Youtube [guide](https://www.youtube.com/watch?v=rYEpXc6sMS4&ab_channel=RunThat) for a similar template.

  _However, double check the official OpenAI documentation as some videos may be using legacy APIs when initialising the OpenAI clients, and therefore are showing different parameters being used._

Gabriel 03/02/2024
