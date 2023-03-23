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
    res = ""
    in_list = False
    in_list_append = False
    for i in lines:
        if i.startswith("###### "):
            i = "<h6>" + i[7:] + "</h6>"
        elif i.startswith("##### "):
            i = "<h5>" + i[6:] + "</h5>"
        elif i.startswith("#### "):
            i = "<h4>" + i[5:] + "</h4>"
        elif i.startswith("### "):
            i = "<h3>" + i[4:] + "</h3>"
        elif i.startswith("## "):
            i = "<h2>" + i[3:] + "</h2>"
        elif i.startswith("# "):
            i = "<h1>" + i[2:] + "</h1>"

        elif i.startswith("* "):
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = i[2:]
                if "__" in curr:
                    parts = curr.split("__")
                    curr = parts[0] + "<strong>" + parts[1] + "</strong>" + parts[2]
                    is_bold = True
                if "_" in curr:
                    parts = curr.split("_")
                    curr = parts[0] + "<em>" + parts[1] + "</em>" + parts[2]
                    is_italic = True
                i = "<ul><li>" + curr + "</li>"
            else:
                is_bold = False
                is_italic = False
                curr = i[2:]
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
                i = "<li>" + curr + "</li>"
        else:
            if in_list:
                in_list_append = True
                in_list = False
        if not (
            i.startswith("<h")
            or i.startswith("<ul")
            or i.startswith("<p")
            or i.startswith("<li")
        ):
            i = "<p>" + i + "</p>"
        if "__" in i:
            parts = i.split("__")
            i = parts[0] + "<strong>" + parts[1] + "</strong>" + parts[2]
        if "_" in i:
            parts = i.split("_")
            i = parts[0] + "<em>" + parts[1] + "</em>" + parts[2]
        if in_list_append:
            i = "</ul>" + i
            in_list_append = False
        res += i
    if in_list:
        res += "</ul>"
    return res
