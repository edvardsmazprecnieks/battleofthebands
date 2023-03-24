def parse(markdown):
    """
    Convert markdown-formatted text to HTML.

    Args:
    markdown (str): The markdown-formatted text to convert.

    Returns:
    html: The HTML-formatted text.

    The `parse` function converts markdown-formatted text to HTML. It recognizes the
    following markdown syntax:
    # h1 header
    ## h2 header
    ### h3 header
    #### h4 header
    ##### h5 header
    ###### h6 header
    * unordered list item

    All other text is treated as paragraphs.

    In paragraphs, text marked as _text_ will be made italic and __text__ will be make bold.
    """

    lines = markdown.split("\n")
    html = ""
    in_list = False

    for line in lines:

        if line.startswith("#"):
            line = parse_header(line)

        elif line.startswith("* "):
            if not in_list:
                in_list = True
                html += "<ul>"
            line = parse_unordered_list_item(line)

        else:
            if in_list:
                html += "</ul>"
                in_list = False

        if not (
            line.startswith("<h") or line.startswith("<ul")
            or line.startswith("<p") or line.startswith("<li")
        ):
            line = make_line_into_paragraph(line)

        if "__" in line:
            line = make_line_into_bold(line)

        if "_" in line:
            line = make_line_into_italic(line)

        html += line

    if in_list:
        html += "</ul>"

    return html


def parse_header(line):
    header_level = len(line.split()[0])
    if header_level > 6:
        return make_line_into_paragraph(line)
    header_text = line[header_level + 1:]
    return f"<h{header_level}>{header_text}</h{header_level}>"


def make_line_into_paragraph(line):
    return f"<p>{line}</p>"


def parse_unordered_list_item(line):
    line = line[2:]
    return "<li>" + line + "</li>"


def make_line_into_bold(line):
    parts = line.split("__")
    return parts[0] + "<strong>" + parts[1] + "</strong>" + parts[2]


def make_line_into_italic(line):
    parts = line.split("_")
    return parts[0] + "<em>" + parts[1] + "</em>" + parts[2]
