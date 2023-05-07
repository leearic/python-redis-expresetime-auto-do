import redis
from telegram.ext import Updater
import telegram

class RedisJobs():
    def __init__(self):
        pool = redis.ConnectionPool(host='192.168.31.230', port=6379, password='123123', decode_responses=True)
        try:
            self.r = redis.Redis(connection_pool=pool, decode_responses=True)

        except Exception as e:
            print(e)


    def create_products(self, product_name, value):
        redis_task_key = 'product_' + product_name
        redis_task_value = value
        try:
            self.r.set(redis_task_key, redis_task_value, ex=3)
        except Exception as e:
            print(e)


    def pub(self):
        self.r.publish('adfgadfgadfg', 'adfgadfg')



if __name__ == '__main__':
    A = RedisJobs()
    A.create_products(product_name='product_name', value='bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
    # A.pub()