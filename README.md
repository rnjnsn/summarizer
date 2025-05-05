# GPT-Powered Text Summarizer (Streamlit Demo)

This project was created to apply and reinforce key concepts from the [DeepLearning.AI Generative AI with LLMs](https://www.coursera.org/learn/generative-ai-with-llms) course, specifically:

- **Prompt engineering**: Structuring system and user messages to influence model behavior;
- **Using the Chat API**: Calling OpenAI's `gpt-3.5-turbo` via `openai.ChatCompletion.create()`;
- **Controlling model behavior**: Adjusting parameters like `temperature` and `max_token.

## Functionality

The app summarizes user-provided text using GPT. It's designed as a minimal, safe demo for portfolio purposes.

### Features:
- Clean and simple Streamlit UI
- Input character limit (3,000 characters)
- Session-based usage cap (3 summaries per session)
- OpenAI API key securely loaded via `.env`

## Technology

- Python
- Streamlit
- OpenAI API (`gpt-3.5-turbo`)
- `python-dotenv` for secrets management

## Run It Locally

```bash
git clone https://github.com/rnjnsn/summarizer.git
cd summarizer
