import dbm
import random
import string

def shorten_url(inpt, url):
    """
    takes an input, and a base url and generates a link at the base url
    that will redirect to the inpt link
    TODO: add check to make sure the generated string isn't already in use
          add check to see if inpt is real url
    """
    urls = dbm.open('urls.db','c')
    shortened_url = ''.join(random.choice(string.ascii_letters) for _ in range(10)) 
    urls[shortened_url] = inpt
    urls.close()
    return f"{ url }{ shortened_url }"

def lengthen_url(inpt):
    """
    takes a shortened url and returns the original url
    or an empty string if it doesn't exist  
    """
    try:
        urls = dbm.open('urls.db','c')
        url = urls[inpt]
        urls.close()
        return url
    except KeyError:
        return ""
 
