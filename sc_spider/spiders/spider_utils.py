from urllib.parse import urlparse


def page_name_from_url(url, suffix='.txt'):
    parsed = urlparse(url)
    path = '.'.join(parsed.path.replace('/', '_').split('.')[0:-1])

    return path + suffix
