from .parser import parse_file, extract_functions
from .generator import generate_docstring


def analyze_and_generate(filename, style="google"):

    tree = parse_file(filename)
    functions = extract_functions(tree)

    generated = []

    for func in functions:
        if not func["docstring"]:
            doc = generate_docstring(func, style)
            generated.append((func["name"], doc))

    return generated
