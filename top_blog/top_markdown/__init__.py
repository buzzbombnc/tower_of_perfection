# Markdown and the extension requirements.
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

class TOPTree(Treeprocessor):
    def __init__(self, *args, **kwargs):
        # Get the Blog instance.
        self.instance = kwargs['instance']
        del kwargs['instance']

        super(TOPTree, self).__init__(*args, **kwargs)
        
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
            # Add the CSS classes.
            self.update_class(e, ['img-responsive', 'center-block',])
            
            # If the image src doesn't contain slashes, check the database for a blogimage that meets the criteria.
            src = e.get('src')
            if '/' not in src:
                images = self.instance.blogimages_set.filter(image__endswith=src)
                if images:
                    e.set('src', images[0].image.url)
        # Set the first paragraph to the lead.
        e = root.find('.//p')
        if e is not None:
            self.update_class(e, ['lead',])
        # Migrate any H5/H6 elements to H4.
        for e in root.findall('.//h5') + root.findall('.//h6'):
            e.tag = 'h4'


class TOPExtension(Extension):
    def __init__(self, **kwargs):
        # Passing None makes the config value a Boolean, which is not the intention.
        self.config = {'instance': ['', 'Blog instance to use.']}
        super(TOPExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        md.treeprocessors.add('TOPTree', TOPTree(instance=self.getConfig('instance')), '_end')


markdown_defaults = {
    'extensions': [
        'markdown.extensions.extra',
        'markdown.extensions.sane_lists',
        'markdown_checklist.extension',
    ],
    'output_format': 'html5',
    'lazy_ol': False,
}

def format(blog_instance, data=None):
    """Returns the Markdown formatted 'data' using 'blog_instance'.
    
    If 'data' is None, the blog_instance.article is used for data."""
    if not data:
        data = blog_instance.article

    # Use the markdown defaults, but load the instance into the Extension.
    options = dict(markdown_defaults)
    options['extensions'].append(TOPExtension(instance=blog_instance))
    return markdown.markdown(data, **options)
