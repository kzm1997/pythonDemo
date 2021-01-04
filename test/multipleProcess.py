from random import randint
from time import time,sleep

def download_task(filename):
    print('开始下载%s'% filename)
    time_todownload=randint(5,10)
    sleep(time_todownload)
    print('%s下载完成,耗费了%d秒'%(filename,time_todownload))

def main():
    start=time()
    download_task('xxx.pdf')
    download_task('嘻嘻嘻.pd')
    end=time()
    print('耗费了%.2f秒'%(end-start))


if __name__=='__main__':
    main()    