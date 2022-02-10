import site
import sys

sys.path.insert(0, '/var/www/www-root/data/www/kamasutra')
site.addsitedir('/var/www/www-root/data/www/kamasutra/env/lib/python3.8/site-packages')

from flup.server.fcgi import WSGIServer
from main import app

if __name__ == '__main__':
    WSGIServer(app).run()
