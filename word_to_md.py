import os

import pypandoc


def word_to_markdown(input_file, output_file):
    """

    Converts a Word document to Markdown using Pandoc.



    Args:

        input_file (str): Path to the Word document (.docx).

        output_file (str): Path to save the converted Markdown file (.md).

    """

    pypandoc.convert_file(input_file, 'md', outputfile=output_file,
                          format='docx')


# Usage


dir = "C:/Users/grey/Documents/AIM-II/docs"
output = "./word_to_mds"

for file in os.listdir(dir):
    if file.endswith(".docx"):
        word_to_markdown(
            os.path.join(dir, file),
            os.path.join(output, file.replace(".docx", ".md"))
        )