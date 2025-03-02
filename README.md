# HTML to Markdown Converter
HTML to Markdown Converter is a Python-based tool that converts HTML files into Markdown format.

It supports converting individual HTML files into structured, readable Markdown files while maintaining compatibility and isolation using virtual environments.

## Features
- Convert HTML content to Markdown format with ease.
- Accepts file paths for input and output to process HTML files.
- Easy-to-use setup scripts for Windows, Linux, and macOS.

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation
1. **Clone the Repository**
```bash
git clone https://github.com/pulkitgarg04/html-to-markdown-converter.git
cd html-to-markdown-converter
```

2. **Install Dependencies**
Dependencies are automatically installed when running the setup script. However, if needed, manually install them:
```bash
pip install -r requirements.txt
```

## Usage
1. **Run the converter script**:
```bash
python main.py
```

2. Enter the required paths:
- Input File: Path to the HTML file (e.g., html_files/example.html).
- Output File: Path to save the Markdown file (default: output/output.md).

3. The converted Markdown file will be saved to the specified location.

## Troubleshooting
#### File Not Found Error
Ensure the file path entered is correct and does not include quotes. For example:

```
Correct: D:\Projects\html-to-markdown-converter\html_files\example.html
Incorrect: "D:\Projects\html-to-markdown-converter\html_files\example.html"
```

#### Dependencies Not Installed
Run the following command to manually install dependencies:
```bash
pip install -r requirements.txt
```

## Contribution
Feel free to fork the repository and submit pull requests to enhance the functionality of the script.

#### Steps to Contribute
1. Fork the Repository:
    - Click the Fork button at the top right of the repository page to create a copy of the repository in your GitHub account.

2. Clone Your Fork:
    - Clone your forked repository to your local machine:

    ```bash
    git clone https://github.com/pulkitgarg04/html-to-markdown-converter.git
    cd html-to-markdown-converter
    ```

3. Create a New Branch:
    - Create a new branch for your changes:
    ```bash
    git checkout -b feature/your-feature-name
    ```

4. Make Your Changes:
    - Edit the script or add new features. Make sure your changes are well-tested.

5. Commit Your Changes:
    - After making changes, commit them with a clear and descriptive message:
    ```bash
    git add .
    git commit -m "Add a detailed description of your changes"
    ```

6. Push Your Changes:
- Push the changes to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```

7. Open a Pull Request (PR):
- Go to the original repository on GitHub.
- Click on the Pull Requests tab.
- Click New Pull Request and choose your branch from your fork as the source.
- Provide a descriptive title and explanation of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.