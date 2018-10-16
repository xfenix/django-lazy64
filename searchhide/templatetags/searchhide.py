from base64 import b64encode

from django import template


CSS_CLASS = 'dj-special-block'
KEY_PREFIX = 'dj-special-{}'
block_count = 0
register = template.Library()


class ShideNode(template.Node):
    template = "<div class=\"%s\" id=\"{key_name}\"></div>"\
               "<script>localStorage.setItem('{key_name}', '{data}');</script>" % CSS_CLASS

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        prepared_output = self.template.format(
            key_name=KEY_PREFIX.format(block_count), data=b64encode(output))
        block_count += 1
        return prepared_output


def do_shide(parser, token):
    nodelist = parser.parse(('endshide',))
    parser.delete_first_token()
    return ShideNode(nodelist)


@register.simple_tag
def post_shide():
    """ This is just minified version of repo root file unhide.js
    """
    return """<script>(function(){'use strict';let $blocks=document.querySelectorAll('.{}');$blocks.forEach(function($oneBlock){$oneBlock.innerHTML=window.atob(localStorage.getItem($oneBlock.getAttribute('id')))})})();</script>""".format(CSS_CLASS)
