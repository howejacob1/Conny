import streamlit as st
import openai

st.set_page_config(page_title="Conny", layout="centered")

# Centered title using markdown and HTML
st.markdown("""
    <h1 style='text-align: center;'>Conny</h1>
""", unsafe_allow_html=True)

# Load OpenAI API key from Streamlit secrets
oai_key = st.secrets["openai"]["api_key"]
openai.api_key = oai_key

MODEL = "gpt-4-1106-preview"  # GPT-4.1 model name

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Send a message..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = openai.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state["messages"]],
                    stream=False
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"Error: {e}"
            st.markdown(reply)
            st.session_state["messages"].append({"role": "assistant", "content": reply}) 