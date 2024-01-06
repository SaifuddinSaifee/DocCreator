import ast
import json


# This class is used to parse python code and extract useful information such as functions, classes, variables and imports.
class PythonCodeParser:
    # Initialize the parser with the file path of the python code
    def __init__(self, file_path):
        self.file_path = file_path

    # Parse the python code and return a dictionary containing the parsed data
    def parse(self):
        # Open the python file and parse the source code into an AST
        with open(self.file_path, "r") as source:
            tree = ast.parse(source.read())

        # Initialize the parsed data dictionary
        parsed_data = {
            "functions": [],
            "classes": [],
            "variables": [],
            "imports": []
        }

        # Walk through the AST and extract information
        for node in ast.walk(tree):
            # Extract function definitions
            if isinstance(node, ast.FunctionDef):
                parsed_data["functions"].append(self._parse_function(node))
            # Extract class definitions
            elif isinstance(node, ast.ClassDef):
                parsed_data["classes"].append(self._parse_class(node))
            # Extract variable assignments
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                parsed_data["variables"].extend(self._parse_variables(node))
            # Extract import statements
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                parsed_data["imports"].append(self._parse_imports(node))

        # Return the parsed data
        return parsed_data

    # Parse a function definition node and return a dictionary containing the function details
    def _parse_function(self, node):
        func_details = {
            "name": node.name,
            "args": [arg.arg for arg in node.args.args],
            "docstring": ast.get_docstring(node),
            "body": [self._get_node_repr(child) for child in node.body]
        }
        return func_details

    # Parse a class definition node and return a dictionary containing the class details
    def _parse_class(self, node):
        class_details = {
            "name": node.name,
            "docstring": ast.get_docstring(node),
            "methods": [self._parse_function(method) for method in node.body if isinstance(method, ast.FunctionDef)]
        }
        return class_details

    # Parse a variable assignment node and return a list of dictionaries containing the variable details
    def _parse_variables(self, node):
        variables = []
        # Handle annotated assignments
        if isinstance(node, ast.AnnAssign):
            target = node.target
            if isinstance(target, ast.Name):
                variable_detail = {"name": target.id, "type": self._get_node_repr(node.annotation), "value": self._get_node_repr(node.value)}
                variables.append(variable_detail)
        else: # Handle normal assignments
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variable_detail = {"name": target.id, "value": self._get_node_repr(node.value)}
                    variables.append(variable_detail)
        return variables

    # Parse an import statement node and return a list of dictionaries containing the import details
    def _parse_imports(self, node):
        if isinstance(node, ast.Import):
            names = [{"name": alias.name, "alias": alias.asname} for alias in node.names]
        else:  # Handle from-import statements
            names = [{"from": node.module, "name": alias.name, "alias": alias.asname} for alias in node.names]
        return names

    # Get a string representation of an AST node
    def _get_node_repr(self, node):
        if isinstance(node, ast.Constant):
            return repr(node.value)
        elif isinstance(node, ast.Name):
            return node.id
        # Handle other node types as needed
        return ast.dump(node)

# Usage Example

if __name__ == "__main__":
    parser = PythonCodeParser("app.py")
    
    parsed_data = parser.parse()

    json_data = json.dumps(parsed_data, indent=4)

    # Print the JSON string
    print(json_data)


