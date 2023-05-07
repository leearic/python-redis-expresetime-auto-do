# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import redis
from telegram.ext import Updater
import telegram

class RedisJobs():
    def __init__(self):
        pool = redis.ConnectionPool(host='192.168.31.230', port=6379, password='123123', decode_responses=True)
        try:
            self.r = redis.Redis(connection_pool=pool, decode_responses=True)

            self.pub = self.r.pubsub()
            self.pub.psubscribe('__keyevent@*__:expired')
            # self.pub.subscribe('__keyevent@*__:expired')

        except Exception as e:
            print(e)


    def create_products(self, product_name, value):
        redis_task_key = 'product_' + product_name
        redis_task_value = value
        try:
            self.r.set(redis_task_key, redis_task_value, ex=5)
        except Exception as e:
            print(e)

    def del_key(self, key):
        self.r.delete(key)

    def subscrb(self):
        for i in self.pub.listen():
            # msg = self.pub.get_message()
            # print(self.pub.parse_response())
            # print(self.pub)
            ab = TG()
            ab.chat(job='a', res=i)
            print(i)
            # print(msg)



class TG():
    def __init__(self):
        self.updater = Updater(token='123123 : adfgadfgadgfadfg', use_context=True)
    def chat(self, job, res):

        msg2 = res

        try:
            self.updater.bot.send_message(chat_id= 123123123 , text=msg2, parse_mode=telegram.ParseMode.HTML)

        except Exception as e:
            pass





if __name__ == '__main__':
    aa = RedisJobs()
    # aa.create_products(product_name='a', value='b')
    aa.subscrb()



