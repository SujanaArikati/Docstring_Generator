import sys
from backend.engine import analyze_and_generate
from backend.coverage import docstring_coverage
from backend.validator import validate_pep257


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python cli.py <filename> <style>")
        sys.exit()

    filename = sys.argv[1]
    style = sys.argv[2]

    print("Initial Coverage:", docstring_coverage(filename), "%")

    generated = analyze_and_generate(filename, style)

    print("\nGenerated Docstrings:\n")
    for name, doc in generated:
        print(f"Function: {name}")
        print(doc)
        print("-" * 40)

    issues = validate_pep257(filename)

    print("\nPEP257 Validation:")
    for issue in issues:
        print(issue)

    print("\nFinal Coverage:", docstring_coverage(filename), "%")
