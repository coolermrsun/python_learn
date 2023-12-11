import time
import requests
from bs4 import BeautifulSoup

def spider_novel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"无法获取页面 {url}，状态码：{response.status_code}")
        return None, None

    response.encoding = 'gbk'
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    chapter_title = soup.find('h1').text

    content = soup.find('div', id='content')

    if content is not None:
        cleaned_content = content.get_text(separator='\n', strip=True)
    else:
        cleaned_content = "内容未找到"

    return chapter_title, cleaned_content

if __name__ == "__main__":
    # 绝对路径
    file_path = r'D:\spider_learn\fanren.txt'

    # 测试调用
    with open(file_path, 'a', encoding='utf-8') as file:
        for i in range(507240, 6068945):
            url = f'https://www.ddyueshu.com/1_1562/{i}.html'

            title, content = spider_novel(url)

            if title is not None and content is not None:
                file.write(f'章节标题: {title}\n\n章节内容:\n{content}\n\n')

    print(f'已将内容输出到文件 {file_path}')