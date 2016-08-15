
# -*- coding: utf-8 -*-

import unicodedata

def makeunicode(s, srcencoding="utf-8", normalizer="NFC"):
    """Convert to a normalized unicode string assuming UTF-8 encoding and NFC normalizer."""
    if type(s) != unicode:
        s = unicode(s, srcencoding)
    s = unicodedata.normalize(normalizer, s)
    return s


if __name__ == '__main__':
    s = "äöüß"
    t = makeunicode( s )
    print t.encode("utf-8")