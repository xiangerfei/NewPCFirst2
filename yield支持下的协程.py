

from gevent import monkey
monkey.patch_all()
import gevent
from urllib.request import urlopen
import time

def f(url):
    print("GET:%s" %url)
    resp = urlopen(url)
    data = resp.read()
    print("%d bytes received from %s."%(len(data), url))

begin = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org'),
    gevent.spawn(f, 'https://www.yahoo.com'),
    gevent.spawn(f, 'https://www.github.com')
])

print(time.time() - begin)


