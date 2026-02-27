import ast


def parse_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    return tree


def extract_functions(tree):
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):

            params = []
            for arg in node.args.args:
                param_type = ast.unparse(arg.annotation) if arg.annotation else "Any"
                params.append((arg.arg, param_type))

            return_type = ast.unparse(node.returns) if node.returns else "Any"

            functions.append({
                "node": node,
                "name": node.name,
                "params": params,
                "returns": return_type,
                "docstring": ast.get_docstring(node)
            })

    return functions
