# scrapy_freepeople
运行这个程序需要先安装python2,scrapy
1.安装pip
    $ sudo apt-get install python-pip python-dev build-essential

    $ sudo pip install --upgrade pip

    $ sudo pip install --upgrade virtualenv
    
2.安装scrapy
    sudo pip install scrapy
    
3.安装twisted
    sudo apt-get install python-setuptools

    Sudo apt-get install python-dev

    Sudo easy_install twisted
运行：进入cookies.us同级目录下
  scrapy crawl freepeople -o freepeople.json
freepeople.json 就是最终生成的结果文件
