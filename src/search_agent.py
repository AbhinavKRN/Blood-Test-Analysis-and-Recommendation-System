import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SearchAgent:
    def __init__(self, summary):
        self.summary = summary
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def search(self):
        prompt = f"Provide a list of articles that are relevant to the following health summary:\n\n{self.summary}\n\nList them with brief descriptions."
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
            )
            articles = response['choices'][0]['message']['content'].strip().split("\n")
        except Exception as e:
            articles = [f"Failed to retrieve articles: {str(e)}"]

        return articles
