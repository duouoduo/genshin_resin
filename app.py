import datetime
import time
STAMINA_MAX = 160
STAMINA_RECOVER_TIME = 480

# 体力计算
def stamina_calculate():
    pass
# 主程序
def app():
    
    current_stamina_str = input('请输入当前体力值：')
    current_stamina = int(current_stamina_str)if current_stamina_str else 0
    remain_time = datetime.timedelta(seconds=(STAMINA_MAX - current_stamina) * STAMINA_RECOVER_TIME)
    object_time = datetime.datetime.now() + remain_time
    print('体力计算器')
    current_time = datetime.datetime.now()
    print('当前时间：', current_time.strftime('%Y-%m-%d %H:%M:%S'))
    print('回满时间：', object_time.strftime('%Y-%m-%d %H:%M:%S'))
    reamain_time = (STAMINA_MAX - current_stamina)*STAMINA_RECOVER_TIME
    while True:
        print('体力面板：{}/{},剩余时间{}/{}'.format(current_stamina, STAMINA_MAX, remain_time,object_time.strftime('%H:%M:%S')),end='\r')
        if current_stamina == STAMINA_MAX:
            print('体力已于{}回满，开原！'.format(current_time))
            break
        time.sleep(1)
        remain_time = remain_time - datetime.timedelta(seconds=1)
        if int(remain_time.total_seconds())%STAMINA_RECOVER_TIME == 0:
            current_stamina += 1
if __name__ == '__main__':
    app()
