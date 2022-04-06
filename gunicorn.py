"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ, getcwd
from os.path import join


def max_workers():
    return cpu_count()


bind = "localhost:" + environ.get("PORT", "8000")

max_requests = 1024

workers = max_workers()

errorlog = join(getcwd(), "NCGR.err")
accesslog = join(getcwd(), "NCGR.log")
pid = join(getcwd(), "NCGR.pid")
loglevel = "debug"
