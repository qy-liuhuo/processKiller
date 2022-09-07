import os

# 设置端口号
#PORT = 1080

PORT = int(input())

result = os.popen('netstat -aon|findstr "%d"' % PORT)
res = result.read()
res = res.split('\n')[0]
pid = res.split(' ')[-1]

os.popen("taskkill -pid %d -f" % int(pid))
