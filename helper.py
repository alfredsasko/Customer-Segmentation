'''
Module to support customer segmentation project includes:
- get_feature_details: Create mapping of short to long feature names
                       and levels in form of dictionary
'''

import io
import pypandoc
import panflute

def get_feature_details(elem, doc):
    if isinstance(elem, panflute.Header) and elem.level == 3:
        doc.images.append(elem)
    elif isinstance(elem, panflute.Link):
        doc.links.append(elem)

if __name__ == '__main__':
    data = pypandoc.convert_file('example.md', 'json')
    doc = panflute.load(io.StringIO(data))
    doc.images = []
    doc.links = []
    doc = panflute.run_filter(action, prepare=prepare, doc=doc)

    print("\nList of image URLs:")
    for image in doc.images:
        print(image.url)

# create mapping of short feature names to long feature names
def get_feature_details(path, short_names):
    '''
    Create mapping of short to long feature names and levels in form of dictionary
    Agrs:
        path: path to file with long feature names
        short_names: list of short names

    Returns:
        feature_details: mapping of short to long feature names and levels in form of dictionary
                         ex: {'short_name': ('long_name', {'level_code': 'level_name'})}
    '''

    with open()
