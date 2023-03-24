def parse(markdown):
    """
    Convert markdown-formatted text to HTML.

    Args:
    markdown (str): The markdown-formatted text to convert.

    Returns:
    str: The HTML-formatted text.

    The `parse` function converts markdown-formatted text to HTML. It recognizes the
    following markdown syntax:

    All other text is treated as paragraphs.
    """

    lines = markdown.split("\n")
    html = ""
    in_list = False
    in_list_append = False
    for line in lines:
        if line.startswith("#"):
            header_level = len(line.split()[0])
            if header_level > 6:
                line = f"<p>{line}</p>"
            else:
                header_text = line[header_level + 1:]
                line = f"<h{header_level}>{header_text}</h{header_level}>"
        elif line.startswith("* "):
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = line[2:]
                if "__" in curr:
                    parts = curr.split("__")
                    curr = parts[0] + "<strong>" + parts[1] + "</strong>" + parts[2]
                    is_bold = True
                if "_" in curr:
                    parts = curr.split("_")
                    curr = parts[0] + "<em>" + parts[1] + "</em>" + parts[2]
                    is_italic = True
                line = "<ul><li>" + curr + "</li>"
            else:
                is_bold = False
                is_italic = False
                curr = line[2:]
                if "__" in curr:
                    is_bold = True
                if "_" in curr:
                    is_italic = True
                if is_bold:
                    parts = curr.split("__")
                    curr = parts[0] + "<strong>" + parts[1] + "</strong>" + parts[2]
                if is_italic:
                    parts = curr.split("_")
                    curr = parts[0] + "<em>" + parts[1] + "</em>" + parts[2]
                line = "<li>" + curr + "</li>"
        else:
            if in_list:
                in_list_append = True
                in_list = False
        if not (
            line.startswith("<h")
            or line.startswith("<ul")
            or line.startswith("<p")
            or line.startswith("<li")
        ):
            line = "<p>" + line + "</p>"
        if "__" in line:
            parts = line.split("__")
            line = parts[0] + "<strong>" + parts[1] + "</strong>" + parts[2]
        if "_" in line:
            parts = line.split("_")
            line = parts[0] + "<em>" + parts[1] + "</em>" + parts[2]
        if in_list_append:
            line = "</ul>" + line
            in_list_append = False
        html += line
    if in_list:
        html += "</ul>"
    return html
