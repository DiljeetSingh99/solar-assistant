# Solar Industry AI Assistant - Setup Guide

## Prerequisites
- Python 3.8 or higher
- OpenRouter API key

## Installation

1. Clone the repository:
   ```bash
git clone https://github.com/DiljeetSingh99/solar-assistant.git

   cd solar-assistant
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4.Add Your Key in `.env` your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```


## Running the Application

Start the application:
```bash
python "Solar Energy Source.py"
```

The application will launch a local web interface. You can access it at:
```
http://localhost:7860
```

## Deployment

To deploy the application:
1. Create a Hugging Face Space
2. Upload all project files
3. Set environment variables in the Space settings
4. Launch the Space

## Troubleshooting

- If you encounter API errors, verify your OpenRouter API key
- Check the logs in `solar_assistant.log` for detailed error information
