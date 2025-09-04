# Chatbot with LangChain & Groq
A chatbot built in Python that can analyze and converse about content from websites, PDF files, and YouTube videos.

---

## 🚀 Features

* 🌐 **Website Loader** → fetch and analyze text content from any URL.
* 📄 **PDF Loader** → load and read PDF documents from your local machine.
* ▶️ **YouTube Loader** → extract transcripts from YouTube videos (with `youtube-transcript-api`).
* 💬 **Conversational Memory** → maintains context during the chat session.
* 🔗 **LangChain Integration** → prompt templates and chaining with LLMs.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* [LangChain](https://www.langchain.com/)
* [Groq](https://groq.com/) LLaMA 3.3 model
* [langchain-community loaders](https://python.langchain.com/)
* [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

---

## ⚙️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/multimodal-chatbot.git
   cd multimodal-chatbot
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Variables

Before running, set your **Groq API key**:

```bash
export GROQ_API_KEY="your_api_key_here"   # Linux/Mac
setx GROQ_API_KEY "your_api_key_here"     # Windows (PowerShell)
```

## 🔑 How to Get Your Groq API Key

### 📝 1. Create a Groq Account
* Go to [https://console.groq.com](https://console.groq.com)
* Click **Sign up** (or **Log in** if you already have an account).
* You can sign up using **Google**, **GitHub**, or with your **email**.
---
### 📧 2. Verify Your Email
* Check your inbox.
* Confirm your email address if Groq asks for verification.
---
### 📊 3. Access the Dashboard

* After logging in, you’ll be redirected to the **Groq Console Dashboard**.

---

### 🔐 4. Create an API Key

1. On the **left sidebar**, click on **API Keys**.
2. Click **Create API Key**.
3. Give your key a descriptive name (e.g., `chatbot-project`).
4. Copy the generated key (it will start with `gsk_...`).

⚠️ **Important:** Store this key securely. Groq will not show it again once you leave the page.

---

## ▶️ Usage

Run the chatbot:

```bash
python main.py
```

Choose an input source:

```
1 - analyze website
2 - analyze PDF
3 - analyze YouTube video
4 - exit
```

Then interact:

```
User: What is the summary of this document?
Bot: ...
```

Exit the conversation anytime with `x`.

---

## 📌 Example

* **Input:** PDF of a travel itinerary.
* **User asks:** “Summarize the main destinations.”
* **Bot responds:** with a coherent summary based on the PDF content.

---

* The course *“Python para IA: do zero ao primeiro chatbot”* by Asimov Academy inspired this project.

---
