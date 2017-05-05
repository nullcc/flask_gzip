# Flask_Gzip

requirements:

1. python3.0+

Python3.0+ doesn't has StringIO module, use [Flask_Gzip for py2](https://github.com/closeio/Flask-gzip)
will cause errors.
In py3, use gzip.compress() to gzip data.

Usage:
    
    import Flask
    from flask_gzip import Gzip
    
    app = Flask(__name__)
    gzip = Gzip(app)
    
or

in exts.py:

    from flask_gzip import Gzip
    
    gzip = Gzip()
    
in app.py:

    gzip.init_app(app)
    
    
parameters:

1. app
2. compress_level

<br >

    gzip = Gzip(compress_level=9)  # compress_level range 0-9