import multiprocessing

bind = 'localhost:5000'

workers = multiprocessing.cpu_count()  # a little overkill
timeout = 30
keepalive = 5

pidfile = '/tmp/test_service.pid'

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = None
