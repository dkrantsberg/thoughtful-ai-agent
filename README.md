# Thoughtful AI Customer Support Agent

## Features

- **Knowledge Base Search**: Retrieves relevant answers from a predefined dataset using fuzzy string matching
- **LLM Fallback**: Uses mlvoca TinyLlama LLM for questions not covered in the knowledge base
- **Web-based Chat Interface**: Built with Gradio

## Tech Stack

- **Python+**
- **Gradio** - Web-based chat interface
- **Free LLM API - mlvoca.com** - LLM fallback for unknown questions

## Prerequisites

- Python 3.9 or higher
- mlvoca free LLM https://mlvoca.github.io/free-llm-api/ with TinyLlama model

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

## Running the Application

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Access the interface**:
   - The Gradio interface will launch automatically
   - Open your browser and navigate to the provided local URL (typically `http://127.0.0.1:7860`)

