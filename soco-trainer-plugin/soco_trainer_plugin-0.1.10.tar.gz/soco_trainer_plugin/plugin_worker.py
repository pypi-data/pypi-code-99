# -*- coding: utf-8 -*-
# Author: Kyusong Lee
# Date: 9/22/21

from .core.utils import get_queue
import redis
from rq import Connection, Worker


class PluginWorker(object):
    def __init__(self, redis_url):
        self.redis_url = redis_url

    def run_worker(self):
        redis_connection = redis.from_url(self.redis_url)
        with Connection(redis_connection):
            worker = Worker(get_queue("trainer"))
            worker.work()

