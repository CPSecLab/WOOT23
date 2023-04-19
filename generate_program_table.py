#!/usr/bin/env python3

# Usage: ./generate_program_table.py > index.html

import string
import sys

with open('index.html.template') as f:
    index_template = f.read()

with open('program.txt') as f:
    lines = f.read().split('\n')

out = ''
out += """
<table class="table table-striped">
    <tbody>
        <tr>
                <th style="width: 100px;">Time</th>
                <th style="width: 961px;">Title &amp; Authors</th>
        </tr>
"""

for line in lines:
    line = line.strip()
    if line == '': continue
    if line.startswith('#'): continue

    if line[0] in string.digits:
        # entry with time, e.g., <time>, <title>, <authors>
        elems = line.split(', ')
        time = elems[0]
        if len(elems) == 2:
            title = elems[1]
            authors = None
        else:
            title = elems[1]
            authors = ', '.join(elems[2:])
        if authors is not None:
            out += f"""
                <tr>
                    <td style="width:100px">{time}</td>
                    <td style="width:961px"><strong>{title}</strong>, <em>{authors}</em></td>
                </tr>
            """
        else:
            out += f"""
                <tr>
                    <td style="width:100px">{time}</td>
                    <td style="width:961px"><strong>{title}</strong></td>
                </tr>
            """
    else:
        # paper title + authors
        title, authors = line.split(', ', 1)
        out += f"""
            <tr>
                <td style="width:100px"></td>
                <td style="width:961px"><strong>{title}</strong>, <em>{authors}</em></td>
            </tr>
        """

out += """
    </tbody>
</table>
"""

out = out.replace('&', '&amp;')

index = index_template.replace('{{PROGRAM_TABLE}}', out)

print(index)
