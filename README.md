# hnwl

湖南文理学院自动刷课

# 必要

需要翻墙  
推荐翻墙：  
[佛跳墙](https://github.com/getfotiaoqiang/fotiaoqiang)  
需要下载谷歌浏览器和谷歌浏览器驱动  
推荐 Chrome:  
[Chrome](https://www.google.com/intl/zh-CN/chrome/)  
ChromeDriver:  
[ChromeDriver](https://chromedriver.chromium.org/downloads)

    根据自身谷歌版本下载谷歌驱动
    查看谷歌浏览器版本,在谷歌浏览器输入：
    chrome-version://
    我的是：87.0.4280.141
    所以下载的谷歌驱动也要是	87.0.4280.141
    下载完驱动之后将驱动配置到环境变量PATH,一定要用全路径，如：
    C:\chromedriver\chromedriver.exe

需要下载 python3.7 以上版本，推荐 python3.9  
下载链接：  
[python3.9](https://www.python.org/downloads/release/python-390/)  
[python3.8](https://www.python.org/downloads/release/python-380/)  
[python3.7](https://www.python.org/downloads/release/python-370/)  
制作不易  
微信：cacode，邮箱：cacode@163.com，捐献可以加，提 bug 在 git 就好了

# 配置文件介绍（prop.ini）：

宽带：100M

    [Init]
    # 初始化打开主页面的延迟时间
    _init_page = 5
    # 打开登录页面的时间
    _to_login = 5
    [baseConfig]
    # 到个人中心的时间
    _to_my = 5
    # 到播放页面的时间
    _to_play_page = 10
    # 开始播放广告的时间
    _click_play_button = 15
    # 是否显示页面 False:不显示 True:显示
    _show_view = False
    [YouInfo]
    name = 你的身份证
    password = 你的密码

# init.bat

    启动脚本
    启动时自动下载依赖的selenium
    务必先修改好配置文件再启动

根据自身网速调节

# 本项目由【广东蓝星灯塔科技有限公司】提供支持

    ██████      ██                        ████████     ██
    ░█░░░░██    ░██                       ██░░░░░░     ░██
    ░█   ░██    ░██   ██   ██    █████   ░██          ██████    ██████     ██████
    ░██████     ░██  ░██  ░██   ██░░░██  ░█████████  ░░░██░    ░░░░░░██   ░░██░░█
    ░█░░░░ ██   ░██  ░██  ░██  ░███████  ░░░░░░░░██    ░██      ███████    ░██ ░
    ░█    ░██   ░██  ░██  ░██  ░██░░░░          ░██    ░██     ██░░░░██    ░██
    ░███████    ███  ░░██████  ░░██████   ████████     ░░██   ░░████████  ░███
    ░░░░░░░    ░░░    ░░░░░░    ░░░░░░   ░░░░░░░░       ░░     ░░░░░░░░   ░░░
