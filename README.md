# Conny

A standard way to get/use vcons.

## Usage

1. Clone the repository.
2. Install dependencies (if any).
3. Run the main script:

```bash
python main.py
```

## License

MIT

# ChatGPT Clone with Streamlit

This is a simple chatbot web app using Streamlit and OpenAI's GPT-4.1, mimicking the ChatGPT interface.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure your `.secrets.toml` contains your OpenAI API key in the `[openai]` section:
   ```toml
   [openai]
   api_key = "sk-..."
   ```

## Run the app

```bash
streamlit run chatbot_app.py
```