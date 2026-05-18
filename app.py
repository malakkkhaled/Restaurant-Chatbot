import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Model display names
MODEL_DISPLAY_NAMES = {
    "openai/gpt-4o-mini": "GPT-4o Mini",
    "openai/gpt-4o": "GPT-4o",
    "anthropic/claude-3-haiku": "Claude 3 Haiku"
}

# Get API key from .env
def get_api_key():
    api_key = os.getenv("OPENROUTER_KEY")
    return api_key

# Call the LLM via OpenRouter
def call_llm(messages, model="openai/gpt-4o-mini", temperature=0.3, max_tokens=800):
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError("OPENROUTER_KEY is missing in .env file")

    url = "https://openrouter.ai/api/v1/chat/completions"

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=40)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]

# System prompt specialized for restaurant Q&A
def build_system_prompt():
    return (
        "You are a friendly AI assistant specialized in restaurants. "
        "Answer all questions about restaurants, menus, dishes, cuisines, ratings, reservations, payments, health & safety, and miscellaneous queries. "
        "Use the following information as reference:\n\n"
        "General Information:\n"
        "- Hours: 11:00 AM to 10:00 PM on weekdays, 9:00 AM to 11:00 PM on weekends.\n"
        "- Location: 123 Main Street, Hometown, HT 12345, near Central Park entrance.\n"
        "- Parking: Complimentary parking available.\n\n"
        "Reservations:\n"
        "- Make reservations via phone (123-456-7890) or website.\n"
        "- Modifications/cancellations up to 24 hours in advance.\n\n"
        "Menu:\n"
        "- Vegetarian/vegan options available.\n"
        "- Children’s menu available.\n"
        "- Food allergies accommodated, inform server.\n\n"
        "Specials:\n"
        "- Daily specials include seasonal dishes and chef selections.\n"
        "- Happy hour: 4:00 PM to 6:00 PM weekdays, discounted drinks/appetizers.\n\n"
        "Payments:\n"
        "- Accepts major credit/debit cards and cash. No personal checks.\n"
        "- Gift cards available online and in-restaurant.\n\n"
        "Health & Safety:\n"
        "- COVID-19 precautions: sanitization, masks, social distancing.\n"
        "- Outdoor seating available in spring/summer.\n\n"
        "Miscellaneous:\n"
        "- Private events can be booked (birthdays, weddings, corporate).\n"
        "- Free Wi-Fi available.\n\n"
        "Use simple language and short paragraphs."
    )

# Generate answer from the model
def generate_answer(user_input, model, temperature):
    system_message = {
        "role": "system",
        "content": build_system_prompt()
    }
    user_message = {
        "role": "user",
        "content": user_input
    }
    messages = [system_message, user_message]
    answer = call_llm(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=800
    )
    return answer

# Initialize session state in Streamlit
def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

# Streamlit interface
def main():
    st.set_page_config(
        page_title="Restaurant Chatbot 🍽️",
        page_icon="🍔",
        layout="centered"
    )

    init_session_state()

    st.title("Restaurant Chatbot 🍽️")
    st.write("Ask anything about restaurants, menus, or table reservations!")

    with st.sidebar:
        st.header("Settings")
        model = st.selectbox(
            "Model",
            options=list(MODEL_DISPLAY_NAMES.keys()),
            format_func=lambda m: MODEL_DISPLAY_NAMES[m]
        )
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.3,
            step=0.1
        )
        st.markdown("---")
        st.caption("Developer: Eng. Malak Khaled Abdellatif")

    # Display previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    user_input = st.chat_input("Type your question about restaurants here...")

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )
        with st.chat_message("user"):
            st.markdown(user_input)

        try:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    answer = generate_answer(
                        user_input=user_input,
                        model=model,
                        temperature=temperature
                    )
                    st.markdown(answer)
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )
        except Exception as e:
            error_message = f"Error: {str(e)}"
            st.error(error_message)
            st.session_state.messages.append(
                {"role": "assistant", "content": error_message}
            )

if __name__ == "__main__":
    main()
