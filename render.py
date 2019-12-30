import os

from jinja2 import Environment, FileSystemLoader

# this tells jinja2 to look for templates
# in the templates subdirectory
env = Environment(
    loader = FileSystemLoader('templates'),
)

input_file = 'template_jinja.html'
output_file = 'index.html'

# reading the template
template = env.get_template(input_file)
# render the template
# in other words, we replace the template tag
# by the contents of the overfitting file
rendered = template.render()

# write the result to disk in index.html
with open(output_file, 'w') as ofile:
    ofile.write(rendered)
