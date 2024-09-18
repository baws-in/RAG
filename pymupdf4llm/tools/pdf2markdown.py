import pymupdf4llm
import sys
import os
import fnmatch
import re
import pathlib

    

def file_iterator(parent_directory, pattern=None):
    """
    A generator that yields tuples of (filepath, filename)
    from the given parent directory, optionally filtered by a filename pattern.
    
    Args:
    parent_directory (str): The path to the parent directory to search.
    pattern (str, optional): A filename pattern to filter results. Defaults to None.
    
    Yields:
    tuple: (filepath, filename) for each matching file.
    """
    for root, dirs, files in os.walk(parent_directory):
        for file in files:
            if pattern is None or fnmatch.fnmatch(file, pattern):
                yield (os.path.join(root, file), file)

def store_text_values(array_of_dicts, filename_prefix):
    # Ensure the directory exists
    if not os.path.exists(filename_prefix):
        os.makedirs(filename_prefix)
    for idx, item in enumerate(array_of_dicts):
        text_value = item.get('text', '').encode()
        if text_value:
            filename = f"{filename_prefix}\\{idx + 1}.md"
            pathlib.Path(filename).write_bytes(text_value)

for filepath, file in file_iterator(sys.argv[1], pattern = "Volume_25*.pdf"):
    md_text = pymupdf4llm.to_markdown(filepath, margins=(0,0,0,0), page_chunks=True, ignore_code = True, pages=[72])
    store_text_values(md_text,  os.path.splitext(filepath)[0])

#import pathlib
#pathlib.Path(sys.argv[2]).write_bytes(md_text.encode())