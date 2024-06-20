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
    html_nodes = markdown_to_html_node(md).to_html()
    print(html_nodes)
