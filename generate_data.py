import peewee
from peewee import MySQLDatabase

db = MySQLDatabase('exp_data', user='root', passwd='root')


class User(peewee.Model):
    id = peewee.PrimaryKeyField()
    birthday = peewee.DateTimeField()
    gender = peewee.BooleanField()
    city_id = peewee.IntegerField()

    class Meta:
        database = db


if __name__ == '__main__':
    # User.create_table()

    from datetime import datetime
    import random
    import time
    # for i in range(1, 1000000):
    total_s = time.time()
    for i in range(1, 10):
        # start = time.time()
        year = random.choice(range(1940, 2016))
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 29))
        birth_date = datetime(year, month, day)
        gender_ = random.choice(range(0, 2))
        city_id_ = random.choice(range(1, 2000))
        user = User.create(birthday=birth_date, gender=gender_, city_id=city_id_)
        user.save()
        end = time.time()
        # res = end - start
        # print("save: {}".format(res))
    total_e = time.time()
    total = total_e - total_s
    print("total: {}".format(total))
