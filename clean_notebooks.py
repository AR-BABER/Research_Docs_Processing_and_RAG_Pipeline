import json
import re
import glob
import nbformat

def clean_api_keys(notebook_path):
    """
    Clean API keys (and other secrets) from a Jupyter notebook and replace with env vars.
    This version uses broader regex patterns to catch more potential secrets.
    """
    
    # Patterns for lines that might contain secret strings or keys. 
    # The replacement will set them to environment variables.
    # You can expand, combine, or tweak patterns to suit your needs.
    # 
    # Explanation for each pattern:
    #  1) Anything with "api_key", "secret", "token", or "password", 
    #     followed by = or : (Python or YAML style), then a quoted string.
    #  2) Captures anything with authorization/bearer tokens. 
    #  3) Looks for "sk-" style secrets (OpenAI keys) specifically.
    secrets_patterns = [
        (r'(api_key|secret|token|password)\s*[=:]\s*[\'"]([^\'"]+)[\'"]',
         r'\1 = os.getenv("REPLACED_ENV_VAR")'),
        (r'("Authorization":\s*"Bearer\s+)([^"]+)"',
         r'\1" + os.getenv("REPLACED_ENV_VAR") + "'),
        (r'["\'](sk-[a-zA-Z0-9]{48})["\']',
         r'os.getenv("OPENAI_API_KEY")')
    ]
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    changes_made = False
    env_vars_imported = False

    for cell in notebook.cells:
        if cell.cell_type == "code":
            original_source = cell.source
            modified_source = original_source

            # Apply each pattern to the cell's source
            for pattern, replacement in secrets_patterns:
                if re.search(pattern, modified_source):
                    modified_source = re.sub(pattern, replacement, modified_source)
                    changes_made = True

            # If we made changes, ensure environment variables are imported and loaded
            if changes_made and not env_vars_imported:
                # We'll prepend the imports so the user sees them at the top of the cell
                imports = (
                    "import os\n"
                    "from dotenv import load_dotenv\n\n"
                    "load_dotenv()  # Load environment variables from .env if present\n\n"
                )
                modified_source = imports + modified_source
                env_vars_imported = True

            cell.source = modified_source

    if changes_made:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        print(f"Cleaned secrets from {notebook_path}")
        return True

    print(f"No secrets or API keys found in {notebook_path}")
    return False

def process_all_notebooks(directory="."):
    """Process all notebooks in the given directory."""
    notebooks = glob.glob(f"{directory}/**/*.ipynb", recursive=True)
    cleaned_count = 0
    
    for notebook_path in notebooks:
        if clean_api_keys(notebook_path):
            cleaned_count += 1
    
    print(f"\nProcessed {len(notebooks)} notebooks, cleaned {cleaned_count} files")

# Run the script
if __name__ == "__main__":
    print("Starting API key cleanup...")
    process_all_notebooks()
    print("\nDone! Don't forget to:")
    print("1. Create a .env file with your API keys")
    print("2. Add .env to your .gitignore")