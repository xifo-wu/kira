import requests
from bs4 import BeautifulSoup


def get_primary_color(url):
    if url is None:
        return None

    # 发送 HTTP GET 请求，获取页面内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)


    # 使用 BeautifulSoup 解析页面内容，并提取出 CSS 变量值
    soup = BeautifulSoup(response.text, 'html.parser')
    style_tag = soup.select_one('#main > section > style')

    # 提取出 --primaryColor 和 --primaryColorContrast 变量值
    css_text = style_tag.string.strip()
    css_lines = css_text.split('\n')
    primary_color = ''
    primary_color_contrast = ''

    print(css_text, "responseresponse")

    for line in css_lines:
        if '--primaryColor:' in line:
            primary_color = line.split(':')[1].strip()[:-1]
        elif '--primaryColorContrast:' in line:
            primary_color_contrast = line.split(':')[1].strip()[:-1]

    return {"primary_color": primary_color, "primary_color_contrast": primary_color_contrast}
