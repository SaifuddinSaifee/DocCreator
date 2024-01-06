# DocCreator

DocCreator is a tool designed to simplify code documentation and streamline onboarding for new contributors in open-source GitHub repositories. It leverages GPT API and LangChain to provide an intuitive interface for generating comprehensive documentation and interactive guidance. Whether you're a beginner navigating a complex codebase or a project maintainer looking to enhance collaboration, CodeDocFlow aims to make the process more accessible and efficient for everyone involved.

## Overview

- **app.py:** Entry point of the tool
- **code_parser.py:** Contains logic to create AST for the provided python code
- **assembler.py:** Contains logic to assemble the distributed docs created by LLM
- **llm_interface.py:** Contains logic for Code to md doc
- **embedding_generator.py:** Contains logic to generate embedding for the code if required

## Limitation

Exploring the limitation of this application. Encouraging contributions to resolve the limitations.

### Code Parser

Here are the notable limitations along with a gist of resolution of limitations in the code parser logic (refer code_parser.py) file:

1. **Limited Node Handling**:
   - **Limitation**: The parser handles a basic set of AST nodes, excluding constructs like decorators.
   - **Resolution**: Extend the parser to include additional AST node types as required, ensuring a more comprehensive parsing of the Python code.

2. **Simplified Node Representation**:
   - **Limitation**: Node representations are basic and might not capture complex structures effectively.
   - **Resolution**: Enhance the `_get_node_repr` method to handle complex expressions and structures, providing a more detailed representation of the code.

3. **Comment Parsing**:
   - **Limitation**: Python's AST does not include comments, and they are currently not parsed.
   - **Resolution**: Implement a separate mechanism for comment extraction, such as using tokenization or regex-based methods alongside AST parsing.

4. **Error Handling**:
   - **Limitation**: The parser lacks comprehensive error handling for unexpected code structures or syntax errors.
   - **Resolution**: Add robust error handling and logging to manage and debug issues with parsing different types of code.

5. **Scalability**:
   - **Limitation**: Performance and memory usage are not optimized for large code bases.
   - **Resolution**: Optimize the parser for efficiency, possibly by implementing lazy loading or parallel processing techniques for handling large repositories.

## Contribution

I encourage you to contribute to this repository or create issue if you feel so, I am open to feedbacks and suggestion upon how to make this a better and more efficient project.
For any queries, feel free to reach out at (@SaifSaifee_dev)[https://twitter.com/SaifSaifee_dev]