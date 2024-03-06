from os import environ

import gunicorn

from app import app


def main():
    # Configura Gunicorn
    options = {
        'workers': 1 ,
    }
    app.wsgi_app = gunicorn.gunicorn.wsgi_server.WSGIApplication (
        environ , app , options
    )
    return app


if __name__ == '__main__':
    main ()
