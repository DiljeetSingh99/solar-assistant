# Environment Setup Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager

## Step 1: Create Virtual Environment
1. Open terminal/command prompt
2. Navigate to project directory
3. Run: `python -m venv .venv`

## Step 2: Activate Virtual Environment
- **Windows**: `.venv\Scripts\activate`
- **Mac/Linux**: `source .venv/bin/activate`

## Step 3: Install Dependencies
1. Ensure virtual environment is activated
2. Run: `pip install -r requirements.txt`

## Step 4: Configure Environment Variables
1. Create `.env` file in project root
2. Add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

## Step 5: Verify Installation
1. Run: `python "Solar Energy Source.py"`
2. Access the application at the provided local URL

## Troubleshooting
- If you encounter permission errors:
  - Windows: Run terminal as administrator
  - Mac/Linux: Use `sudo` for installation commands
- If dependencies fail to install:
  - Update pip: `python -m pip install --upgrade pip`
  - Try installing packages individually
