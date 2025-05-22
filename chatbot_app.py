import streamlit as st
import openai
from pymongo import MongoClient

st.set_page_config(page_title="Conny", layout="centered")

# Centered title using markdown and HTML
st.markdown("""
    <h1 style='text-align: center;'>Conny</h1>
""", unsafe_allow_html=True)

# Load OpenAI API key from Streamlit secrets
oai_key = st.secrets["openai"]["api_key"]
openai.api_key = oai_key

# Load MongoDB credentials from Streamlit secrets
mongo_uri = st.secrets["mongo_db"]["url"]
mongo_db = st.secrets["mongo_db"]["db"]
mongo_collection = st.secrets["mongo_db"]["collection"]

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

def get_vcons():
    return list(collection.find())

# Button to display vcons
def display_vcons():
    vcons = get_vcons()
    if not vcons:
        st.info("No vcons found.")
    for vcon in vcons:
        st.json(vcon)

if st.button("Show all vcons"):
    display_vcons()

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