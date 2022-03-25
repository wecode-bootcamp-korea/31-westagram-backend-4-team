import re

from django.forms import ValidationError


REGEX_URL = "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?" 
def url_validate(url):
    if not re.match(REGEX_URL, url):
                raise ValidationError("URL format error.")