环境：anaconda+pycharm
- anaconda使用
  - conda list:显示当前环境安装的包
  - conda env list：显示安装的虚拟环境列表
  - conda create -n env_name python=3.6
  - 激活conda的虚拟环境
    - （linux）source activate env_name
    -  (win) activate env_name
    - pip intall django=1.8
请求-解包-路由-views(视图)-model(和数据打交道)-temple（模型）
后台需要的流程

#创建一个django程序
命令行启动：
 - django-admin startproject tuling01
 - cd tulingxueyuan
 - python manage.py runserver
 pycharm启动：
 - 需要配置
 #路由系统-urls
 - 创建app 
    - app:负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp teacher
 -路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能
    - django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射