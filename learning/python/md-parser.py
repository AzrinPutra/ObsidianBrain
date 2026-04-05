import re

def extract_headings(filepath):
    """
    Reads a markdown file and returns a list of all headings.

    Parameters
    ----------
    filepath : str
        Path to the markdown file.

    Returns
    -------
    list of tuples
        A list where each element is a tuple (level, text).
        e.g., [(1, 'Main Title'), (2, 'Section'), (3, 'Subsection')]
    """
    headings = []
    # Regex pattern: Start of line, 1-6 hashes, optional space, and the rest of the line
    pattern = r'^(#{1,6})\s+(.*)$'

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(pattern, line.strip())
            if match:
                hashes, text = match.groups()
                level = len(hashes)
                headings.append((level, text))

    return headings


# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        file_to_parse = sys.argv[1]
        print(f"Parsing headings from: {file_to_parse}")
        headings = extract_headings(file_to_parse)
        for level, text in headings:
            print(f"{'#' * level} {text}")
    else:
        print("Usage: python md-parser.py <markdown_file>")