import os
import html2text

def html_to_markdown(file_path, output_path="output/output.md"):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' doesn't exist.")
        return
    
    try:
        with open(file_path, "r", encoding="utf-8") as html_file:
            html_content = html_file.read()

        converter = html2text.HTML2Text()
        converter.ignore_links = False
        converter.ignore_images = False
        markdown_content = converter.handle(html_content)

        with open(output_path, "w", encoding="utf-8") as markdown_file:
            markdown_file.write(markdown_content)

        print(f"Markdown file has been saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("HTML to Markdown Converter")
    print("===========================")

    html_file_path = input("Enter the path of the HTML file (e.g., html_files/example.html): ")
    output_file_path = input("Enter the path to save the Markdown file (default: output/output.md): ") or "output/output.md"

    html_to_markdown(html_file_path, output_file_path)


if __name__ == "__main__":
    main()