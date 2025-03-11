# AI Data Science Tutor 🤖📊

Welcome to **AI Data Science Tutor**! 🎓 Your interactive Data Science guide powered by **Google Gemini AI** and **Streamlit**. This app allows you to ask any Data Science-related questions and get intelligent, concise, and accurate answers. Whether you're a beginner or expert, ChatDS has your back.

## 🚀 Features
✅ **AI-Powered Data Science Tutor** – Get accurate and easy-to-understand answers to your Data Science queries.  
✅ **Session Management** – Save your session and restore it for later.  
✅ **Customizable Background** – Add a personal touch with your custom image for the chat interface.  
✅ **Beginner-Friendly Interface** – Uses **Streamlit** for an easy-to-use, interactive experience.

## 📌 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-repo/AI_Data_Science_Tutor.git
cd AI_Data_Science_Tutor
```  
### 2️⃣ Create a Virtual Environment (Optional but Recommended)  

#### ➤ **Run the following command to create a virtual environment:**  
```sh
python -m venv venv
```
### ➤ Activate the Virtual Environment  

#### 🖥️ **On macOS/Linux:**  
```sh
source venv/bin/activate
```
### ➤ Activate the Virtual Environment  

#### 🖥️ **On Windows:**  
```sh
venv\Scripts\activate
```
### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```
### 4️⃣ Set Up API Key  

#### ➤ **Create a `.env` file in the project folder**  
1. Inside your project directory, create a new file named `.env`.  
2. Open the `.env` file and add your **Google Gemini API Key** in the following format:  

```sh
GEMINI_API_KEY=your_api_key_here
```
## ▶️ Run the Application  

Run the following command to start the Streamlit app:  

```sh
streamlit run app.py
```
## 🛠 Technologies Used

- **Python** 🐍  
  Core programming language used to develop the application.
  
- **Google Gemini AI** 🤖  
  AI model used for providing accurate and intelligent Data Science tutoring responses.
  
- **Streamlit** 🎨  
  Web framework for building the interactive user interface of the application.
  
- **dotenv** 🛠  
  Used for managing environment variables such as API keys securely.
  
- **langchain** 💬  
  Library used for handling prompts and processing model output.
  
## 🏆 How It Works  

1️⃣ **Start a Session**  
   - If you have a previous session, enter your **Session ID** to restore it.  
   - If not, a new session will be created automatically with a unique **Session ID**.  

2️⃣ **Ask a Question**  
   - Type your **data science-related** question in the chat input box.  

3️⃣ **AI Processing**  
   - The AI, powered by **Google Gemini** and **LangChain**, will analyze your question.  
   - It retrieves **chat history** using an **SQLite database** for context-aware responses.  

4️⃣ **Receive an Answer**  
   - The AI provides **clear and concise** data science explanations.  
   - Responses are formatted in a structured chat interface with user-friendly design.  

5️⃣ **Continue the Conversation**  
   - Ask **follow-up questions** to keep the session interactive.  
   - Your chat history is maintained within the session for context-aware discussions.  

6️⃣ **Enjoy Learning!**  
   - Get **detailed, easy-to-understand** explanations for your **Data Science queries**.  
   - Use the **session restoration feature** to revisit previous chats anytime.  

## 📜 License  

This project is **open-source**. Feel free to **use, modify, and contribute**! 🚀  
