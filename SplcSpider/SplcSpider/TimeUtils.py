# coding=utf-8
import datetime
import time


def get_today():
    """
    获取当前日期
    :return: 格式化的日期
    :rtype: str
    """
    return str(datetime.date.today())


def date_add(original, delta):
    # print type(time.strptime(original, '%Y-%m-%d'))
    return str(datetime.datetime.fromtimestamp(time.mktime(time.strptime(original, '%Y-%m-%d'))) + datetime.timedelta(days=delta))[:10]


def get_yesterday():
    """
    获取昨天的日期
    :return:
    """
    return date_add(get_today(), -1)


def get_cur_ts_sec():
    """
    获取当前时间戳,单位:秒
    :return: 秒为单位的当前时间戳
    :rtype: str
    """
    return str(int(time.time()))


def get_cur_ts_mil():
    """
    获取当前时间戳,单位:毫秒
    :return: 毫秒为单位的当前时间戳
    :rtype: str
    """
    return str((time.time()*1000))


def get_cur_time():
    """
    获取当前格式化时间
    :return: 格式化的时间
    :rtype: str
    """
    return time.strftime('%Y-%m-%d %X', time.localtime())


def get_time(ts):
    """
    将时间戳转换为格式化的时间字符串，时间戳为秒
    :param ts:
    :return:
    """

    try:
        return time.strftime('%Y-%m-%d %X', time.localtime(ts))
    except ValueError:
        return None


def get_time_mil(ts_mil):
    """
    将时间戳转换为格式化的时间字符串，时间戳为毫秒
    :param ts_mil:
    :return:
    """
    try:
        return time.strftime('%Y-%m-%d %X', time.localtime(ts_mil/1000))
    except ValueError:
        return None


def get_date(ts):
    try:
        return time.strftime('%Y-%m-%d', time.localtime(ts / 1000))
    except ValueError:
        return None


# Sun Aug 28 2016 14:33:53 GMT+0800 (CST)
def get_cur_time_jiangsu():
    return time.strftime('%a %b %d %Y %X GMT+0800 (CST)',
                         time.localtime())


def format_nei_meng_gu(time_original):
    dt = datetime.datetime.strptime(time_original, '%b %d, %Y %I:%M:%S %p')
    return str(dt)


def get_ts(time_original):
    return time.mktime(time.strptime(time_original, '%Y-%m-%d'))


def convert_dt1(dt1):
    """
    日期格式转换
    :param dt1: 2019年1月1日
    :return:
    """
    return str(datetime.datetime.strptime(dt1, '%Y年%m月%d日'))[:10]


def add_days(start, delta):
    start_dt = datetime.datetime.strptime(start, '%Y-%m-%d')
    res_dt = start_dt + datetime.timedelta(days=delta)
    return str(res_dt)[:10]


def get_middle_dt(start, stop):
    start_dt = datetime.datetime.strptime(start, '%Y-%m-%d')
    stop_dt = datetime.datetime.strptime(stop, '%Y-%m-%d')
    if int((stop_dt - start_dt).days) <= 1:
        return None
    else:
        middle_dt = start_dt + (stop_dt - start_dt)/2
        middle = str(middle_dt)[:10]
        return middle


def split_dt(start, stop):
    start_dt = datetime.datetime.strptime(start, '%Y-%m-%d')
    stop_dt = datetime.datetime.strptime(stop, '%Y-%m-%d')

    if int((stop_dt - start_dt).days) == 0:
        return None
    elif int((stop_dt - start_dt).days) == 1:
        return [start, start, stop, stop]
    else:
        middle_dt1 = start_dt + (stop_dt - start_dt) / 2
        middle_dt2 = middle_dt1 + datetime.timedelta(days=1)
        middle1 = str(middle_dt1)[:10]
        middle2 = str(middle_dt2)[:10]
        return [start, middle1, middle2, stop]


class RangeDt(object):

    def __init__(self, start, stop):
        self.start_dt = datetime.datetime.strptime(start, '%Y-%m-%d')
        self.stop_dt = datetime.datetime.strptime(stop, '%Y-%m-%d')

    def __iter__(self):
        return self

    def next(self):
        if self.start_dt < self.stop_dt:
            res = str(self.start_dt)[:10]
            self.start_dt += datetime.timedelta(days=1)
            return res
        else:
            raise StopIteration()

if __name__ == '__main__':
    # print get_today()
    # print get_cur_ts_sec()
    # print get_cur_ts_mil()
    # print get_cur_time()
    # print get_cur_time_jiangsu()
    # print format_nei_meng_gu('Apr 15, 2010 12:00:00 AM')
    # print format_nei_meng_gu("Apr 21, 2016 12:00:00 AM")
    # print get_date(-2209190400000)
    #
    # print split_dt('2019-01-02', '2019-01-04')

    print(get_time_mil(1570291200000))
    # print convert_dt1('2019年1月12日')
