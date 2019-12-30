import os
import re
import pprint

def process_lines(lines, command):
    new_lines = ['<pre>']
    new_lines.extend(lines)
    new_lines.append('</pre>')
    return new_lines

input_file = 'template.html'
output_file = 'index.html'

include_pattern = re.compile(r'^\s*\{\%\s+include\s+(\S+)\s+\%\}\s*$')
begin_pattern = re.compile(r'^\s*\{\%\s+begin\s+(\S+)\s+\%\}\s*$')
end_pattern = re.compile(r'^\s*\{\%\s+end\s+(\S+)\s+\%\}\s*$')

lines_to_process = []
processing_lines = False
with open(output_file, 'w') as outfile:
    with open(input_file) as infile:
        for line in infile.readlines():
            m = include_pattern.match(line)
            if m:
                include_file = m.group(1)
                with open(include_file) as incfile:
                    outfile.writelines(incfile.readlines())
                continue
            m = begin_pattern.match(line)
            if m:
                command = m.group(1)
                processing_lines = True
                lines_to_process = []
                continue
            m = end_pattern.match(line)
            if m:
                processing_lines = False
                processed_lines = process_lines(lines_to_process,
                                                command)
                pprint.pprint(processed_lines)
                outfile.writelines(processed_lines)
                continue
            if processing_lines:
                lines_to_process.append(line)
                continue

            outfile.write(line)

        
