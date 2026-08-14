#!/usr/bin/env python3
"""Simple HTTP server to serve the Party Cone PFP app."""
import http.server
import os
import webbrowser

PORT = 8000
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

if __name__ == '__main__':
    print(f'Starting server on http://localhost:{PORT}')
    print(f'Serving from: {DIR}')
    webbrowser.open(f'http://localhost:{PORT}')
    http.server.HTTPServer(('localhost', PORT), Handler).serve_forever()
