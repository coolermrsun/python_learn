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

def get_novel_links(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'

    soup = BeautifulSoup(response.text, 'html.parser')

    links = [f'https://www.ddyueshu.com{a["href"]}' for a in soup.select('dd a')]

    return links

if __name__ == "__main__":
    # 绝对路径
    file_path = r'D:\spider_learn\newfanren.txt'

    base_url = 'https://www.ddyueshu.com/1_1562/'

    # 获取链接
    links = get_novel_links(base_url)

    # 测试调用
    with open(file_path, 'a', encoding='utf-8') as file:
        for link in links[6:]:
            title, content = spider_novel(link)

            if title is not None and content is not None:
                file.write(f'章节标题: {title}\n\n章节内容:\n{content}\n\n')


    print(f'已将内容输出到文件 {file_path}')
