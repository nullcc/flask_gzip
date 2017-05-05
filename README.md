# Flask_Gzip

requirements:
1. python3.0+

Python3.0+ doesn't has StringIO module, use [Flask_Gzip for py2](https://github.com/closeio/Flask-gzip)
will cause errors.
In py3, use gzip.compress() to gzip data.

