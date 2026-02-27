import streamlit as st
import ast
import pandas as pd
import google.generativeai as genai

# ==================================================
# GEMINI CONFIGURATION
# ==================================================

genai.configure(api_key="AIzaSyCh_XK12N8n1zcRZDcg9-YzV1WAyi7NgF4")

model = genai.GenerativeModel("gemini-2.5-pro")

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Automated Python Docstring Generator (Gemini AI)",
    layout="wide"
)

# ==================================================
# STYLING
# ==================================================

st.markdown("""
<style>
html, body {
    background-color: #0f172a;
    color: white;
}
.metric-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}
.section-title {
    background-color: #1e40af;
    padding: 10px;
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HELPER FUNCTIONS
# ==================================================

def parse_file(code):
    return ast.parse(code)


def extract_elements(tree):

    elements = []

    for node in ast.walk(tree):

        if isinstance(node, (
            ast.FunctionDef,
            ast.AsyncFunctionDef,
            ast.ClassDef
        )):

            elements.append(node)

    return elements


def get_source_code(node, full_code):

    lines = full_code.split("\n")

    return "\n".join(
        lines[node.lineno - 1: node.end_lineno]
    )


# ==================================================
# GEMINI DOCSTRING GENERATOR
# ==================================================

def generate_docstring_with_gemini(source_code, style):

    prompt = f"""
Generate a professional Python docstring in {style} style.

Follow PEP 257 strictly.

Include:
- Summary ending with period.
- Args
- Returns
- Raises (if applicable)

Code:
{source_code}

Return only docstring.
"""

    try:

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception:

        return None


# ==================================================
# UNIVERSAL VALIDATION FUNCTION
# ==================================================

def validate_docstring(docstring):

    if not docstring:

        return "error", "Missing docstring"

    clean = docstring.strip().strip('"').strip("'").strip()

    if len(clean) < 10:

        return "warning", "Docstring too short"

    lines = [
        line.strip()
        for line in clean.split("\n")
        if line.strip()
    ]

    if not lines:

        return "error", "Empty docstring"

    first_line = lines[0]

    if not first_line.endswith("."):

        return "warning", "Summary must end with period"

    return "passed", "Valid docstring"


# ==================================================
# UI
# ==================================================

st.title("Automated Python Docstring Generator using Gemini AI")

uploaded_file = st.file_uploader(
    "Upload Python File",
    type="py"
)

style = st.selectbox(
    "Select Style",
    ["Google", "NumPy", "reST"]
)

# ==================================================
# MAIN PROCESS
# ==================================================

if uploaded_file:

    code = uploaded_file.read().decode("utf-8")

    tree = parse_file(code)

    elements = extract_elements(tree)

    total = len(elements)

    existing_doc_count = sum(
        1 for e in elements
        if ast.get_docstring(e)
    )

    coverage = round(
        (existing_doc_count / total) * 100,
        2
    ) if total else 0

    missing = total - existing_doc_count

    # ==============================================
    # OVERVIEW METRICS
    # ==============================================

    st.markdown('<div class="section-title">Project Overview</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Existing Coverage", f"{coverage}%")
    col2.metric("Total Elements", total)
    col3.metric("Missing Docstrings", missing)

    st.markdown("---")

    # ==============================================
    # DOCSTRING COMPARISON
    # ==============================================

    st.markdown('<div class="section-title">Docstring Comparison</div>', unsafe_allow_html=True)

    for element in elements:

        st.subheader(element.name)

        existing_doc = ast.get_docstring(element)

        st.write("Existing Docstring:")

        if existing_doc:
            st.code(existing_doc)
        else:
            st.write("None")

        source = get_source_code(element, code)

        with st.spinner("Generating with Gemini..."):

            gemini_doc = generate_docstring_with_gemini(
                source,
                style
            )

        element.gemini_doc = gemini_doc

        st.write("Gemini Generated Docstring:")

        if gemini_doc:
            st.code(gemini_doc)
        else:
            st.write("Generation failed")

        st.markdown("---")

    # ==============================================
    # SINGLE VALIDATION SECTION
    # ==============================================

    if st.button("Run Validation"):

        st.markdown(
            '<div class="section-title">Validation Results</div>',
            unsafe_allow_html=True
        )

        passed = 0
        warnings = 0
        errors = 0

        for element in elements:

            existing_doc = ast.get_docstring(element)
            gemini_doc = getattr(element, "gemini_doc", None)

            # Prefer Gemini docstring if available
            doc_to_validate = gemini_doc if gemini_doc else existing_doc

            status, message = validate_docstring(doc_to_validate)

            if status == "passed":

                passed += 1

                st.success(f"{element.name}: Valid docstring")

            elif status == "warning":

                warnings += 1

                st.warning(f"{element.name}: {message}")

            else:

                errors += 1

                st.error(f"{element.name}: {message}")

        # Summary chart

        df = pd.DataFrame({

            "Status": ["Passed", "Warnings", "Errors"],

            "Count": [passed, warnings, errors]

        })

        st.bar_chart(df.set_index("Status"))

        success_rate = round((passed / total) * 100, 2) if total else 100

        st.metric("Documentation Success Rate", f"{success_rate}%")