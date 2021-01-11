# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

home_url = "https://hnwledu.ls365.net/"
name = ""
password = ""
# 时间延迟
_init_page = 2
_to_login = 3
_to_my = 5
_to_play_page = 10
_click_play_button = 10
_show_view = False
logo = " ___ _          ___ _            \n" \
       "| _ ) |_  _ ___/ __| |_ __ _ _ _ \n" \
       "| _ \\ | || / -_)__ \\  _/ _` | '_|\n" \
       "|___/_|\\_,_\\___|___/\\__\\__,_|_|  \n"

init_text = """
此脚本不会泄露你的信息，制作不易，微信：cacode
"""


def get_browser():
    """
    获取浏览器对象
    :return:
    """
    chrome_options = Options()
    chrome_options.add_argument("--mute-audio")  # 静音
    chrome_options.add_argument('window-size=1920x1080')
    if _show_view == "False":
        chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    return browser


def login(browser, name, password):
    """
    登录
    :param browser:浏览器对象
    :param name:登录名
    :param password:密码
    :return:
    """
    login_text = browser.find_element_by_link_text("登录")
    login_text.click()
    time.sleep(_to_login)
    login_name_input = browser.find_element_by_id("LoginName")
    login_password_input = browser.find_element_by_id("LoginPwd")
    login_name_input.send_keys(name)
    login_password_input.send_keys(password)
    login_button = browser.find_element_by_id("loginbtn")
    login_button.click()
    time.sleep(2)
    try:
        error = browser.find_element_by_class_name("error").text
        return error
    except Exception as err:
        return ""


def get_schedules(browser):
    """
    schedule：浏览器课程进度
    :param browser:浏览器对象
    :return:
    """
    schedules = []
    props = browser.find_elements_by_class_name("lsPercents")
    buttons = browser.find_elements_by_class_name("keepLearning")
    index = 0
    for pro in props:
        text = pro.text
        schedules.append({
            "text": text,
            "element": buttons[index]
        })
        index += 1
    print("elements:", schedules)
    return schedules


def re_calculation_browser(browser):
    """
    重新绑定浏览器对象，用户页面跳转后不在一个窗口
    :param browser:浏览器对象
    :return:
    """
    currentWin = browser.current_window_handle
    handles = browser.window_handles
    print(handles)
    for i in handles:
        print("handles id:", i)
        if currentWin == i:
            continue
        else:
            # 将driver与新的页面绑定起来
            browser.switch_to.window(i)
            break
    return browser


def calculation_class_size(browser):
    """
    计算课程数量,返回：
        data = {
        "class_sum": class_sum,
        "read_ed": read_ed,
        "un_read": un_read
    }
    :param browser:浏览器对象
    :return:
    """
    percent_tags = browser.find_elements_by_class_name("percentTags")
    # 课程数量
    class_sum = len(percent_tags)
    read_ed = 0
    un_read = 0
    for tag in percent_tags:
        img = tag.find_element_by_tag_name("img")
        src = img.get_attribute("title")
        if src == "100%":
            read_ed += 1
        else:
            un_read += 1
    data = {
        "class_sum": class_sum,
        "read_ed": read_ed,
        "un_read": un_read
    }
    return data


def read(browser, element):
    """
    修改进度条的js：document.getElementsByTagName('video')[0].currentTime = document.getElementsByTagName('video')[0].currentTime + 6000
    :param browser: 浏览器对象
    :param element:单击的节点
    :return:
    """
    js = "document.getElementsByTagName('video')[0].currentTime = document.getElementsByTagName('video')[0].currentTime + 6000"
    # 进入播放
    element.click()

    browser = re_calculation_browser(browser)
    while True:
        # 开始干活
        time.sleep(_to_play_page)
        # 重新绑定对象
        # 返回课程信息
        class_info = calculation_class_size(browser)
        class_sum = class_info.get("class_sum")
        read_ed = class_info.get("read_ed")
        un_read = class_info.get("un_read")
        print(class_info)
        print("课程总数：", class_sum)
        print("已读：", read_ed)
        print("未读：", un_read)
        if un_read == 0:
            break
        # 开始播放按钮
        play_button = browser.find_element_by_class_name("prism-big-play-btn")
        play_button.click()
        time.sleep(_click_play_button)

        browser.execute_script(js)
        time.sleep(1)
        # 下一个
        next_button = browser.find_element_by_id("learnNextSection")
        if next_button is None:
            # 如果没有这个下一个按钮，表示已经学完了
            break
        else:
            next_button.click()
            time.sleep(1)
    return browser


def init():
    global _init_page, _to_login, _to_my, _to_play_page, _click_play_button, _show_view, name, password
    config = configparser.RawConfigParser()
    config.read("prop.ini", "utf-8")

    print(config.sections())
    _init_page = int(config.get('Init', '_init_page'))
    _to_login = int(config.get('Init', '_to_login'))
    _to_my = int(config.get('baseConfig', '_to_my'))
    _to_play_page = int(config.get('baseConfig', '_to_play_page'))
    _click_play_button = int(config.get('baseConfig', '_click_play_button'))
    _show_view = config.get('baseConfig', '_show_view')
    name = config.get('YouInfo', 'name')
    password = config.get('YouInfo', 'password')


if __name__ == '__main__':
    print(logo)
    print("正在初始化，请稍后")
    init()
    print(_init_page, _to_login, _to_my, _to_play_page, _click_play_button, _show_view, name, password)
    bro = get_browser()
    bro.get(home_url)
    print("\r\n初始化完成")
    time.sleep(_init_page)
    error = login(bro, name, password)
    if error != "":
        print("错误信息：", error)
        bro.close()
        exit(1)
    time.sleep(_to_my)
    schedules = get_schedules(bro)
    for schedule in schedules:
        text = schedule.get("text")
        print("schedules:", text)
        if text == "100%":
            continue
        else:
            bro = read(bro, schedule.get("element"))
            print("课时已完结")
            # 课时完结，关闭当前标签
            bro.close()
            # 重启并刷新当前浏览器对象的指针
            bro = re_calculation_browser(bro)
            bro.refresh()
            time.sleep(5)
