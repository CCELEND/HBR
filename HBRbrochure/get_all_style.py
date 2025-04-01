
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def list_newline(you_list, how_projects_newline):
    for i in range(0, len(you_list), how_projects_newline):
        print(", ".join(map(str, you_list[i:i+how_projects_newline])))


def dir_newline(you_dir, how_projects_newline):
    # 初始化计数器
    count = 0
    # 遍历字典的项
    for key, value in you_dir.items():
        # 输出键值对，格式为 "key: value"
        print(f"{key}: {value}", 
            end = ", " if count % how_projects_newline != 2 else "\n")
        count += 1

    # 如果最后一行不足 how_projects_newline 项，需要手动换行
    if count % how_projects_newline != 0:
        print()


# 获取风格 id
def get_style_id(style_item_card_element):
    style_id = ""
    try:
        # 获取 data-id 属性值
        style_id = style_item_card_element.get_attribute('data-id')

    except Exception as e:
        print(f"[-] {e}")

    return style_id

try:
    # 设置 Chrome 选项以在后台运行
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # driver = webdriver.Chrome("./chromedriver-win64/chromedriver")
    # # 打开 game.bilibili.com
    # driver.get('https://game.bilibili.com/tool/hbr/#/')

    # 设置 ChromeDriver 的服务
    chromedriver_path = "./chromedriver-win64/chromedriver.exe"
    # service = Service(executable_path=ChromeDriverManager().install())
    service = Service(executable_path=chromedriver_path)
    # 初始化 Chrome WebDriver
    driver = webdriver.Chrome(service=service)

    # 打开 game.bilibili.com
    driver.get('https://game.bilibili.com/tool/hbr/#/')

    time.sleep(2)
    

    # 等待元素加载完成并可见
    filter_SS_element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-id="SS"]')))
    # 点击元素
    filter_SS_element.click()

    # 定位到 content_element
    content_element = driver.find_element(By.CSS_SELECTOR, "[data-v-f8b6e8b1].content")
    # 元素的滑动效果通过 CSS 的 transform 属性
    driver.execute_script(
        "arguments[0].style.transform = 'translateX(0px) translateY(-120px) translateZ(1px)';", 
        content_element
    )


    # 等待 class 为 role-box 的元素加载完成
    role_box_element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "role-box"))
    )

    # 查找类名为 role-icon 的 <div> 元素
    role_icon_elements = role_box_element.find_elements(
        By.XPATH, ".//div[contains(@class, 'role-icon')]"
    )


    style_num = 0
    style_ids = []
    # 获取风格数据
    for role_icon_element in role_icon_elements:

        # 风格元素是动态加载的，需要判断元素是否可见，不可见就滚动到该元素
        if not role_icon_element.is_displayed():
            role_icon_element.location_once_scrolled_into_view

        # 获取风格 id
        style_id = get_style_id(role_icon_element)
        style_ids.append(style_id)

        style_num += 1

    print(f"[+] 全部 SS 风格数: {len(style_ids)}")
    print("[+] 全部 SS 风格 ID:")
    list_newline(style_ids, 6)

    
    # # 获取页面源代码
    # html = driver.page_source
    # # 打印HTML
    # # print(html)

    input()
    # # 关闭浏览器
    # driver.quit()

except Exception as e:
    print(f"[-] {e}")


