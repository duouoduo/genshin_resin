import datetime
import time
# 最大树脂
RESIN_MAX = 160
# 树脂恢复时间
RESIN_RECOVER_TIME = 1

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
# 数据输入
def inputs():
    pass
# 主程序
def app():
    # 获取当前树脂
    current_resin_str = input('请输入当前体力值：')
    current_resin = int(current_resin_str)if current_resin_str else 0
    data = calculate(current_resin)
    # 计算剩余时间
    remain_time = remain_time_(data[0])
    # 当前时间&回满时间
    current_time = datetime.datetime.now()
    object_time = datetime.datetime.now() + remain_time
    print('树脂计算器')
    print('当前时间：', current_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('回满时间：', object_time.strftime('%Y-%m-%d %H:%M:%S'))
    while True:
        print('体力面板：{}/{},剩余时间：{}/{}'.format(current_resin, RESIN_MAX, remain_time,object_time.strftime('%H:%M:%S')),end='\r')
        if current_resin == RESIN_MAX:
            print('体力已于{}回满，开原！'.format(current_time.strftime('%H:%M:%S')))
            break
        time.sleep(1)
        remain_time = remain_time - datetime.timedelta(seconds=1)
        if int(remain_time.total_seconds())%RESIN_RECOVER_TIME == 0:
            current_resin += 1
if __name__ == '__main__':
    app()
