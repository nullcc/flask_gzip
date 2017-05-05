import gzip
from flask import request


class Gzip(object):
    def __init__(self, app, compress_level=6):
        self.app = app
        self.compress_level = compress_level
        self.app.after_request(self.after_request)

    def after_request(self, response):
        accept_encoding = request.headers.get('Accept-Encoding', '')
        if not accept_encoding:
            return response

        encodings = accept_encoding.split(',')
        if 'gzip' not in encodings:
            return response

        if (200 > response.status_code >= 300) or len(response.data) < 500 or 'Content-Encoding' in response.headers:
            return response

        response.data = gzip.compress(response.data)
        response.headers['Content-Encoding'] = 'gzip'
        response.headers['Content-Length'] = len(response.data)

        return response