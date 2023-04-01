import datetime
import time
import configparser
config = configparser.ConfigParser()
config.read('data.ini')
# 最大树脂
RESIN_MAX = 160
# 树脂恢复时间
RESIN_RECOVER_TIME = 480

# 剩余树脂计算
def remain_resin_(current_resin):
    return RESIN_MAX - current_resin

# 剩余时间计算
def remain_time_(remain_resin):
    return datetime.timedelta(seconds=remain_resin * RESIN_RECOVER_TIME)

# 计算剩余树脂&剩余时间
def calculate(current_resin):
    remain_resin = remain_resin_(current_resin)
    remain_time = remain_time_(remain_resin)
    return remain_resin, remain_time

# 主程序
def done(current_time):
    print('体力已于{}回满，开原！'.format(current_time.strftime('%H:%M:%S')))
def app(current_resin):
    
    data = calculate(current_resin)
    # 计算剩余时间
    remain_time = remain_time_(data[0])
    # 当前时间&回满时间
    current_time = datetime.datetime.now()
    object_time = datetime.datetime.now() + remain_time
    print('当前时间：', current_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('回满时间：', object_time.strftime('%Y-%m-%d %H:%M:%S'))
    while True:
        print('体力面板：{}/{},回满剩余时间：{}/{}'.format(current_resin, RESIN_MAX, remain_time,object_time.strftime('%H:%M:%S')),end='\r')
        if current_resin == RESIN_MAX:
            done(current_time)
            break
        time.sleep(1)
        remain_time = remain_time - datetime.timedelta(seconds=1)
        if int(remain_time.total_seconds())%RESIN_RECOVER_TIME == 0:
            current_resin += 1
            config.set('USER', 'resin', str(current_resin))
            config.write(open('data.ini', 'w'))
if __name__ == '__main__':
    print('树脂计算器')
    # 读取历史树脂
    current_resin = config.getint('USER', 'resin')
    # 树脂数量输入
    current_resin_str = input('请输入当前体力值：')
    if current_resin_str != '':
        current_resin = int(current_resin_str)
        config.set('USER', 'resin', str(current_resin))
        config.write(open('data.ini', 'w'))
    app(current_resin)
