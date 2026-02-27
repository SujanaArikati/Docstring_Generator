Automated Python Docstring Generator using Gemini AI
Overview

The Automated Python Docstring Generator is an AI-powered documentation tool that automatically generates professional docstrings for Python functions and classes using Google's Gemini AI. The system analyzes Python source code using Abstract Syntax Tree (AST) parsing and generates standardized docstrings that follow PEP 257 documentation conventions.

The application also validates documentation quality and provides metrics such as coverage percentage, missing docstrings, and validation status through an interactive Streamlit interface.

This tool improves code readability, reduces manual documentation effort, and ensures consistent documentation standards.

Features

Automatic docstring generation using Gemini AI

Supports functions, classes, and async functions

AST-based static code analysis

Multiple docstring styles:

Google style

NumPy style

reStructuredText (reST) style

Docstring validation based on PEP 257 standards

Documentation coverage analysis

Interactive web interface using Streamlit

Real-time validation results and visualization

Compatible with all Python source files

System Architecture

The system workflow consists of the following steps:

Upload Python source file

Parse code using AST parser

Extract functions and classes

Send code segments to Gemini AI

Generate professional docstrings

Validate docstrings for compliance

Display results and metrics in Streamlit dashboard

Technologies Used

Python

Streamlit

Google Gemini AI API

Abstract Syntax Tree (AST)

Pandas

Google Generative AI SDK

Installation
1. Install Python

Recommended version: Python 3.9 or higher

Download from: https://www.python.org/downloads/

2. Install Dependencies
pip install streamlit pandas google-generativeai
3. Configure Gemini API Key

Obtain an API key from:

https://aistudio.google.com/app/apikey

Set the API key in the application:

genai.configure(api_key="YOUR_API_KEY")
Running the Application

Start the Streamlit server:

streamlit run streamlit_app.py

Open in browser:

http://localhost:8501
Usage

Upload a Python (.py) file

Select the desired docstring style

View existing and AI-generated docstrings

Run validation to check documentation quality

Review coverage metrics and validation results

Validation Criteria

Docstrings are validated based on:

Presence of documentation

Minimum documentation length

Proper summary format

Compliance with PEP 257 standards

Validation results include:

Passed

Warning

Error

Example

Input:

def add(a, b):
    return a + b

Generated docstring:

"""
Adds two numbers.

Args:
    a (int): First number.
    b (int): Second number.

Returns:
    int: Sum of the numbers.
"""
Project Structure
project/
│
├── streamlit_app.py
├── README.md
└── requirements.txt
Applications

Software documentation automation

Code quality improvement

Development workflow enhancement

Educational and learning tools

Documentation standardization

License

MIT License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.