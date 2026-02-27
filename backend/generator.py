def generate_docstring(func, style="google"):

    name = func["name"]
    params = func["params"]
    returns = func["returns"]

    if style == "google":
        doc = f'"""{name} function.\n\nArgs:\n'
        for p, t in params:
            doc += f"    {p} ({t}): Description.\n"
        doc += f"\nReturns:\n    {returns}: Description.\n"
        doc += '"""'

    elif style == "numpy":
        doc = f'"""{name} function.\n\nParameters\n----------\n'
        for p, t in params:
            doc += f"{p} : {t}\n    Description\n"
        doc += "\nReturns\n-------\n"
        doc += f"{returns}\n    Description\n"
        doc += '"""'

    else:  # reST
        doc = f'"""{name} function.\n\n'
        for p, t in params:
            doc += f":param {p}: Description\n"
            doc += f":type {p}: {t}\n"
        doc += f":return: Description\n"
        doc += f":rtype: {returns}\n"
        doc += '"""'

    return doc
