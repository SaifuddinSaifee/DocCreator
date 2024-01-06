import streamlit as st
import os
import subprocess
from code_parser import PythonCodeParser  # Assuming code_parser.py contains PythonCodeParser class
from llm_interface import LLMInterface  # Placeholder for LLMInterface class
from assembler import DocumentationAssembler  # Placeholder for DocumentationAssembler class
import json



# Function to clone a git repository
def clone_repo(repo_url):
    local_dir = os.path.basename(repo_url)
    if not os.path.exists(local_dir):
        subprocess.run(["git", "clone", repo_url, local_dir])
    return local_dir

# Function to analyze the repository and generate documentation
def generate_documentation(repo_path):
    # Step 1: Parse the code
    parser = PythonCodeParser(repo_path)
    parsed_data = parser.parse()
    parsed_data = json.dumps(parsed_data, indent=4)

    # Step 2: Generate documentation text using LLM (placeholder)


    # Step 3: Assemble the final documentation (placeholder)
    assembler = DocumentationAssembler(documentation_text)
    final_documentation = assembler.assemble_documentation()

    return final_documentation

# Streamlit app
def main():
    st.title("Code Repository to Documentation Converter")

    repo_url = st.text_input("Enter the URL of a Git repository")

    if st.button("Generate Documentation"):
        if repo_url:
            repo_path = clone_repo(repo_url)
            documentation = generate_documentation(repo_path)
            st.text_area("Generated Documentation", documentation, height=300)
        else:
            st.error("Please enter a valid repository URL.")

if __name__ == "__main__":
    main()
