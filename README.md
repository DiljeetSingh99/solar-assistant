# Solar Industry AI Assistant

## Overview
This project implements an AI-powered assistant specializing in solar industry consulting. It provides accurate, helpful information about solar energy to both technical and non-technical users.

## Features
- Expert solar panel technology information
- Installation process guidance
- Maintenance requirements
- Cost & ROI analysis
- Industry regulations
- Market trends

## Setup
1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the environment:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```
6. Run the application: `python "Solar Energy Source.py"`

## Usage
The application will launch a web interface where you can ask questions about solar energy. Example queries:
- "Best solar panels for home?"
- "How to maintain solar panels?"
- "Solar ROI calculation?"

## Documentation
- [Implementation Details](IMPLEMENTATION_DOCS.md)
- [Setup Guide](SETUP_GUIDE.md)
- [Example Use Cases](EXAMPLE_USE_CASES.md)

## License
MIT License
