from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

# --- Load API Key ---
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

# --- Summarization Function ---
def summarize_text(text, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Please summarize the following:\n\n{text}"}
        ],
        temperature=0.5,
        max_tokens=300
    )
    return response.choices[0].message.content

# --- Streamlit UI ---
if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

st.set_page_config(page_title="GPT Summarizer", layout="centered")
st.title("🧠 GPT-Powered Summarizer")
st.info("🚧 Demo version: Limited to 3000 characters per input to control API usage.")

text_input = st.text_area("Paste your text here:", height=250)
st.caption(f"🧪 You have {3 - st.session_state.usage_count} summaries left in this session.")

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text to summarize.")
    elif len(text_input) > 3000:
        st.warning("⚠️ Please limit your input to 3000 characters for this demo.")
    elif st.session_state.usage_count >= 3:
        st.error("🚫 You've reached the demo limit of 3 uses per session.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(text_input)
        st.session_state.usage_count += 1
        st.subheader("📄 Summary:")
        st.write(summary)
