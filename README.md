# Restaurant Chatbot

A smart AI-powered chatbot for restaurant customer support, built with **Streamlit** and **OpenRouter API**.  
Answers customer questions about menus, reservations, hours, payments, and more — instantly and accurately.

---

## Features

-  **Multi-model support** — Switch between GPT-4o Mini, GPT-4o, and Claude 3 Haiku
-  **Conversational UI** — Clean chat interface powered by Streamlit
-  **Restaurant-specialized** — Trained on restaurant-specific knowledge (menu, hours, reservations, etc.)
-  **Adjustable settings** — Control model and temperature from the sidebar
-  **Fast responses** — Lightweight and optimized for quick answers

---

##  Demo

> Ask questions like:
> - *"What are your opening hours?"*
> - *"Do you have vegetarian options?"*
> - *"How can I make a reservation?"*
> - *"What payment methods do you accept?"*

---

##  Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [OpenRouter API](https://openrouter.ai/) | LLM gateway (GPT-4o, Claude, etc.) |
| [Python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/restaurant-chatbot.git
cd restaurant-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the root directory:

```env
OPENROUTER_KEY=your_openrouter_api_key_here
```

>  Get your free API key from [openrouter.ai](https://openrouter.ai/)

### 4. Run the app

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

##  Project Structure

```
restaurant-chatbot/
│
├── app.py              
├── requirements.txt    
├── .env                
├── .gitignore          
└── README.md           
```

---

##  Configuration

From the **sidebar** in the app, you can:

| Setting | Options |
|---|---|
| **Model** | GPT-4o Mini / GPT-4o / Claude 3 Haiku |
| **Temperature** | 0.0 (focused) → 1.0 (creative) |

---

##  Restaurant Knowledge Base

The chatbot is pre-loaded with the following information:

-  **Hours**: Weekdays 11AM–10PM / Weekends 9AM–11PM
-  **Location**: 123 Main Street, near Central Park entrance
-  **Parking**: Free complimentary parking
-  **Reservations**: Via phone (123-456-7890) or website
-  **Menu**: Vegetarian, vegan, and children's options available
-  **Happy Hour**: 4PM–6PM on weekdays
-  **Payments**: Credit/debit cards and cash accepted
-  **Private Events**: Available for birthdays, weddings, corporate events
-  **Wi-Fi**: Free for all customers

---

##  Security

- The `.env` file is listed in `.gitignore` and will **never** be pushed to GitHub
- Never share your `OPENROUTER_KEY` publicly

---

##  Developer

** Malak Khaled Abdellatif**

---

##  License

This project is for educational and personal use.
