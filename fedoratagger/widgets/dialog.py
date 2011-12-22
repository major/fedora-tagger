from tw2.jqplugins.ui import DialogWidget
import codecs
import docutils.examples


def hotkeys_readme():
    root = '/'.join(__file__.split('/')[:-2])
    fname = root + '/README.rst'
    with codecs.open(fname, 'r', 'utf-8') as f:
        rst = f.read()
        hotkeys = rst.split('.. hotkeys')[1]
        return docutils.examples.html_body(hotkeys)


class HotkeysDialog(DialogWidget):
    id = 'hotkeys_dialog'
    options = {
        'title': 'Hotkeys',
        'autoOpen': False,
        'width': 600,
        'modal': True,
    }
    value = hotkeys_readme()