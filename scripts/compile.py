import codecs
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_FOLDER = '../prototyes/ai/'
TEMPLATE_FILE = 'home.tpl'
OUTPUT_FILE = os.path.join(TEMPLATE_FOLDER, TEMPLATE_FILE + '.html')

env = Environment(
        loader = FileSystemLoader(TEMPLATE_FOLDER),
        autoescape = select_autoescape(['html', 'xml']))

template = env.get_template(TEMPLATE_FILE)
content = template.render()

with codecs.open(OUTPUT_FILE, 'w', 'utf-8') as content_file:
    content_file.write(content)

#env.compile_templates(target='./inspirations/ai', extensions='tpl', zip=None)
