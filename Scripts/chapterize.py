## This script intakes a text file (usually a transcript), extract the title of the chapters for Youtube videos.
## The headers look in this format hh:mm:ss $CHAPTER_NAME


import sys, re

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = 'final_'+infile

    with open(infile, 'r') as file:
        text = file.read()

    header_patterns = r'\[\d{2}:\d{2}:\d{2}\] .*'
    headers = re.findall(header_patterns, text)

    square_bracket_pattern = r'\[|\]'
    for header in headers:
        header = re.sub(square_bracket_pattern, '', header)

        with open(outfile, 'a') as file:
            file.write(header + '\n')

    print(outfile)
