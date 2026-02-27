import ast
from .parser import parse_file


def docstring_coverage(filename):
    tree = parse_file(filename)

    total = 0
    documented = 0

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
            total += 1
            if ast.get_docstring(node):
                documented += 1

    if total == 0:
        return 0

    return round((documented / total) * 100, 2)
