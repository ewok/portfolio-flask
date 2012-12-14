#!/usr/bin/env python2

import config
from flask import Flask
from urls import provide_urls
from db import provide_db

app = Flask(__name__)
app.config.from_object(config)

provide_urls(app)
provide_db(app)

if __name__ == '__main__':
    import sys

    if 'init-db' in sys.argv:
        from db import init_db

        init_db()
    else:
        # Run the server
        app.run(port=8000)

