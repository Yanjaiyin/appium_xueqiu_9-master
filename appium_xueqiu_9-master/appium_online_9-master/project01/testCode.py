import datetime


class D(object):

    def __str__(self):
        return "a __str__"

    def __repr__(self):
        return "a __repr__"

dr = D()
print(dr)
dr

"%s" % dr


t1=datetime.datetime.now()
print(t1)
print(repr(t1))
print(eval(repr(t1)))
print(str(t1))
