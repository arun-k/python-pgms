import re

def make_slug(name):
    temp_slug=re.sub(r'\s+\W*|-+\W+',"-",name)
    return re.sub(r'^\W+|\W+$',"",temp_slug)
