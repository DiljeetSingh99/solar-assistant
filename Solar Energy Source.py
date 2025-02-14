import os
import requests
from dotenv import load_dotenv
import gradio as gr
import logging

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OpenRouter API key is missing. Please check your .env configuration")

logging.basicConfig(

    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='solar_assistant.log'
)

def get_solar_response(query):
    try:

            
        messages = [
            {"role": "system", "content": "Expert solar consultant with technical and practical knowledge"},
            {"role": "user", "content": query}
        ]
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",  # API key is securely loaded and validated

                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": messages,
                "max_tokens": 500,
                "temperature": 0.7
            },
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            error_msg = f"API error: {response.status_code} - {response.text}"
            logging.error(error_msg)
            return "Technical issue, please try again later"
            
    except requests.Timeout:
        logging.error("API request timed out")
        return "Request timeout, please try again"
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return "Something went wrong, please try again"

app = gr.Interface(
    fn=get_solar_response,
    inputs="text",
    outputs="text",
    title="Solar Expert",
    description="Ask about solar panels, installation, costs, and more",
    examples=[
        "Best solar panels for home?",
        "How to maintain solar panels?",
        "Solar ROI calculation?"
    ],
    allow_flagging="never"
)

if __name__ == "__main__":
    app.launch(share=True)
