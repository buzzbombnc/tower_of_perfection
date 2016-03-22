# Markdown and the extension requirements.
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

class TOPTree(Treeprocessor):
    def update_class(self, element, class_list):
        "Adds 'class_list' to 'element's existing classes."
        cls = element.get('class') or ''
        cls += ' '.join(class_list)
        element.set('class', cls)

    def run(self, root):
        # Set TABLE classes.
        for e in root.findall('.//table'):
            self.update_class(e, ['table', 'table-condensed',])
        # Set IMG class.
        for e in root.findall('.//img'):
            self.update_class(e, ['img-responsive', 'center-block',])
        # Set the first paragraph to the lead.
        e = root.find('.//p')
        if e is not None:
            self.update_class(e, ['lead',])
        # Migrate any H5/H6 elements to H4.
        for e in root.findall('.//h5') + root.findall('.//h6'):
            e.tag = 'h4'


class TOPExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.add('TOPTree', TOPTree(), '_end')


markdown_defaults = {
    'extensions': [
        'markdown.extensions.extra',
        'markdown.extensions.sane_lists',
        'markdown_checklist.extension',
        TOPExtension(),
    ],
    'output_format': 'html5',
    'lazy_ol': False,
}

def format(data):
    return markdown.markdown(data, **markdown_defaults)
