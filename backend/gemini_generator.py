import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyCh_XK12N8n1zcRZDcg9-YzV1WAyi7NgF4")

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_docstring_with_gemini(function_code, style="Google"):

    prompt = f"""
Generate a professional Python docstring in {style} style for the following function.

Include:
- Summary
- Args
- Returns
- Raises (if applicable)

Function code:
{function_code}

Only return the docstring.
"""

    response = model.generate_content(prompt)

    return response.text.strip()