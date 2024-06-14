def markdown_to_blocks(markdown):
    stripped = []
    for line in markdown.split("\n\n"):
        stripped.append([line.strip()])
    return stripped
