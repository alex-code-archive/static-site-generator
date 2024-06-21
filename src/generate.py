import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    split = markdown.split("\n")
    if split[0].startswith("# "):
        return split[0]
    raise Exception("Invalid format, no title detected.")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")
    with open(from_path) as f:
        md = f.read()
    with open(template_path) as t:
        template = t.read()

    title = extract_title(md)
    html = markdown_to_html_node(md).to_html()
    temp = template.replace("{{ Title }}", title)
    replaced = temp.replace(" {{ Content }}", html)

    destination_path = os.path.dirname(dest_path)
    file_name = dest_path.split("/")[-1]
    os.makedirs(destination_path, exist_ok=True)
    with open(f"{destination_path}/{file_name}", "w") as f:
        f.write(replaced)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)
    print(dirs)
    for dir in dirs:
        generate_page(f"content/{dir}", template_path, f"{dest_dir_path}/{dir[:-3]}.md")
