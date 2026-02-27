Automated Python Docstring Generator using Gemini AI
Overview

The Automated Python Docstring Generator is an AI-powered tool that automatically generates professional, standardized docstrings for Python functions and classes using Google's Gemini AI. The system analyzes Python source code using Abstract Syntax Tree (AST) parsing and produces high-quality documentation following PEP 257 conventions.

The application also validates docstring quality and provides documentation coverage metrics through an interactive Streamlit web interface. This tool helps developers improve code readability, maintainability, and documentation efficiency.

Features

Automatic docstring generation using Gemini AI

Supports functions, classes, and async functions

AST-based static code analysis

Multiple docstring styles:

Google style

NumPy style

reStructuredText (reST) style

Automatic docstring validation

Documentation coverage calculation

Interactive Streamlit dashboard

Real-time validation and visualization

Works with any Python source file

How It Works

The system follows this workflow:

Upload Python source file

Parse code using AST parser

Extract functions and classes

Send code to Gemini AI

Generate professional docstrings

Validate docstrings using PEP 257 standards

Display results and documentation metrics

Technologies Used

Python

Streamlit

Google Gemini AI API

Abstract Syntax Tree (AST)

Pandas

Google Generative AI SDK

Installation
Step 1: Clone the repository
git clone https://github.com/SujanaArikati/Docstring_Generator.git
cd Docstring_Generator
Step 2: Install dependencies
pip install streamlit pandas google-generativeai
Step 3: Configure Gemini API Key

Get your API key from:

https://aistudio.google.com/app/apikey

Add it in the code:

genai.configure(api_key="YOUR_API_KEY")
Running the Application

Start the Streamlit server:

streamlit run streamlit_app.py

Open in browser:

http://localhost:8501
Usage

Upload a Python (.py) file

Select preferred docstring style

View existing and generated docstrings

Run validation to check documentation quality

View coverage percentage and validation results

Example

Input:

def add(a, b):
    return a + b

Generated output:

"""
Adds two numbers.

Args:
    a (int): First number.
    b (int): Second number.

Returns:
    int: Sum of the numbers.
"""
Project Structure
Docstring_Generator/
│
├── streamlit_app.py
├── README.md
└── requirements.txt
Applications

Software documentation automation

Code quality improvement

Development workflow enhancement

Educational and learning tools

Automated documentation generation

Advantages

Reduces manual documentation effort

Improves code readability and maintainability

Ensures consistent documentation standards

Fast and efficient AI-powered generation

Supports real-world Python projects

Future Improvements

Automatic insertion of generated docstrings into source code

Support for multiple programming languages

Batch file processing

Export updated files

IDE integration support

License

This project is licensed under the MIT License. See the LICENSE file for details.
