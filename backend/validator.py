import ast
from .parser import parse_file


def validate_pep257(filename):
    tree = parse_file(filename)

    issues = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            doc = ast.get_docstring(node)
            if doc:
                if not doc.strip().endswith("."):
                    issues.append(f"{node.name}: Summary should end with period.")

    return issues
