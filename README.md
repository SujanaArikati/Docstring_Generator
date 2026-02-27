🤖 Automated Python Docstring Generator

📌 Overview

The Automated Python Docstring Generator is an AI-powered documentation tool that automatically generates professional and standardized docstrings for Python functions and classes using Google's Gemini AI.

The system analyzes Python source code using Abstract Syntax Tree (AST) parsing and generates documentation that follows PEP 257 standards. It also validates docstring quality and provides coverage metrics through an interactive Streamlit dashboard.

This tool helps improve code readability, maintainability, and developer productivity.

✨ Features

🤖 AI-powered docstring generation using Gemini AI

📂 Supports functions, classes, and async functions

🔍 AST-based code analysis

📝 Multiple docstring formats:

Google style

NumPy style

reStructuredText (reST) style

✅ Automatic docstring validation

📊 Documentation coverage analysis

🌐 Interactive Streamlit web interface

⚡ Real-time docstring generation and validation

🧩 Works with any Python source file

⚙️ How It Works

The system follows this workflow:

📤 Upload Python file

🔎 Parse code using AST

📌 Extract functions and classes

🤖 Send code to Gemini AI

📝 Generate professional docstrings

✅ Validate docstring quality

📊 Display coverage and validation results

🛠️ Technologies Used

🐍 Python

🌐 Streamlit

🤖 Google Gemini AI API

🌳 Abstract Syntax Tree (AST)

📊 Pandas

🔧 Google Generative AI SDK

📥 Installation
1️⃣ Clone the repository
git clone https://github.com/SujanaArikati/Docstring_Generator.git
cd Docstring_Generator
2️⃣ Install dependencies
pip install streamlit pandas google-generativeai
3️⃣ Configure Gemini API Key

Get API key from:

https://aistudio.google.com/app/apikey

Add your API key:

genai.configure(api_key="YOUR_API_KEY")
▶️ Running the Application

Start Streamlit server:

streamlit run streamlit_app.py

Open browser:

http://localhost:8501
🧑‍💻 Usage

📂 Upload Python (.py) file

🎨 Select docstring style

🤖 View AI-generated docstrings

✅ Run validation

📊 View documentation coverage

📌 Example

Input:

def add(a, b):
    return a + b

Output:

"""
Adds two numbers.

Args:
    a (int): First number.
    b (int): Second number.

Returns:
    int: Sum of the numbers.
"""
📁 Project Structure
Docstring_Generator/
│
├── streamlit_app.py
├── README.md
└── requirements.txt
🎯 Applications

📚 Automated documentation generation

🧑‍💻 Software development workflows

🧪 Code quality improvement

🎓 Educational and learning tools

📦 Open-source project documentation

🚀 Advantages

⏱️ Saves documentation time

📖 Improves code readability

📏 Ensures standard documentation format

🤖 Uses advanced AI generation

🧩 Supports real-world Python code

🔮 Future Improvements

✏️ Auto insert docstrings into code

🌍 Multi-language support

📂 Batch file processing

💾 Export updated files

🔌 IDE integration

📜 License

This project is licensed under the MIT License.
