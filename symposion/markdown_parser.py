from html5lib import html5parser, sanitizer, getTreeBuilder

import markdown


def parse(text):

    # First run through the Markdown parser
    text = markdown.markdown(text, extensions=["extra"], safe_mode=False)

    # Sanitize using html5lib
    bits = []
    parser = html5parser.HTMLParser(tokenizer=sanitizer.HTMLSanitizer,
                                    tree=getTreeBuilder("dom"))
    for token in parser.parseFragment(text).childNodes:
        bits.append(token.toxml())
    return "".join(bits)
