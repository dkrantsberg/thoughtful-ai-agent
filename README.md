# Thoughtful AI Customer Support Agent

## Features

- **Knowledge Base Search**: Retrieves relevant answers from a predefined dataset using fuzzy string matching
- **LLM Fallback**: Uses OpenAI's GPT-4o-mini for questions not covered in the knowledge base
- **Web-based Chat Interface**: Built with Gradio for easy interaction

## Tech Stack

- **Python+**
- **Gradio** - Web-based chat interface
- **OpenAI API 1.0+** - LLM fallback for unknown questions

## Prerequisites

- Python 3.9 or higher
- OpenAI API key (optional, but recommended for full functionality)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd thoughtful-ai-agent
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional):
   ```bash
   # Create a .env file in the project root
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

## Running the Application

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Access the interface**:
   - The Gradio interface will launch automatically
   - Open your browser and navigate to the provided local URL (typically `http://127.0.0.1:7860`)

