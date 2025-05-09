# myLibraryApp

**myLibraryApp** is a Python-based command-line tool designed to manage a personal library of code snippets stored in a private GitHub repository. It simplifies storing, retrieving, modifying, deleting, and copying code snippets, making it easier to reuse code across projects. Snippets are saved as `.mli` files (short for "my library"), which are JSON files containing the code and metadata such as keywords, input parameters, return types, and modification dates.

## Features

- **Search**: Find snippets by entering keywords.
- **View**: Display snippet details, including code, inputs, and metadata.
- **Edit**: Modify existing snippets field-by-field.
- **Delete**: Remove snippets from the repository.
- **Copy**: Copy snippet code to the clipboard.
- **Append**: Add new snippets with custom metadata.

## Prerequisites

- A GitHub account with a private repository for storing `.mli` files.
- A GitHub personal access token with the `repo` scope (for full repository access).
- Python 3.x installed.
- Required libraries: `PyGithub` and `tkinter`.
- A GUI environment (since `tkinter` is used for clipboard functionality).

## Setup

1. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install PyGithub
   ```
   Note: `tkinter` is typically included with Python. If not, install it (e.g., `sudo apt-get install python3-tk` on Ubuntu).

2. **Configure GitHub Access**:
   - Open `my_library_app.py`.
   - Replace `GITHUB_TOKEN` with your personal access token.
   - Update `REPO_NAME` with your repository name (e.g., "username/repo").

## Usage

1. **Run the App**:
   Start the application by running:
   ```bash
   python my_library_app.py
   ```

2. **Main Menu**:
   - **1) Search in library**: Search for existing snippets.
   - **2) Append to library**: Add a new snippet.

3. **Searching for Snippets**:
   - Select option 1.
   - Enter keywords one at a time. Use `EOF` to finish or `SHOW` to see matching files early.
   - View a list of matching `.mli` files.
   - Enter the file number to see its details.
   - Options after viewing:
     - `SEARCH`: Start a new search.
     - `EDIT`: Modify the snippet.
     - `DELETE`: Remove the snippet (confirm with `Y`).
     - `COPY`: Copy the code to the clipboard.

4. **Appending a Snippet**:
   - Select option 2.
   - Provide:
     - File name (`.mli` added automatically).
     - Family (category).
     - Code (the snippet itself).
     - Inputs (list parameters; end with `EOF`).
     - Return type.
     - Description.
     - Keys (search keywords; end with `EOF`).
   - Confirm with `Y` to save.

5. **Exiting**:
   - Type `EXIT` at any input prompt to quit.

## File Format

`.mli` files are JSON files with this structure:
```json
{
    "family": "category",
    "keys": ["keyword1", "keyword2"],
    "code": "def example():\n    pass",
    "inputs": ["param1: description", "param2: description"],
    "returnValue": "return type",
    "description": "Snippet description",
    "date": "2023-01-01 12:00:00",
    "lastEdit": "2023-01-01 12:00:00"
}
```

## Notes

- **Repository Structure**: The app assumes `.mli` files are in the repository root. For subdirectories, modify the `list_files` function.
- **Token Permissions**: Your GitHub token needs the `repo` scope.
- **GUI Requirement**: A graphical environment is needed for clipboard operations via `tkinter`.
- **Error Handling**: Ensure a stable internet connection and valid inputs to avoid errors.

## Contributing

This is a personal project, but feedback and improvements are welcome! Fork the repo and submit pull requests with your suggestions.
