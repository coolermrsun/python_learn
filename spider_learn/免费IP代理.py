import requests
from bs4 import BeautifulSoup
import pandas as pd

# 设置请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}

# 初始化数据列表
data_list = []

# 循环处理多个页面
for page in range(1, 3):  # 这里设置页面范围，例如从第1页到第2页
    url = f'https://www.kuaidaili.com/free/inha/{page}/'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有的表格行
    rows = soup.select('.table-section table tbody tr')

    for row in rows:
        # 提取每一行中的数据
        ip = row.select_one('td[data-title="IP"]').text
        port = row.select_one('td[data-title="PORT"]').text
        anonymity = row.select_one('td[data-title="匿名度"]').text
        proxy_type = row.select_one('td[data-title="类型"]').text
        location = row.select_one('td[data-title="位置"]').text
        response_time = row.select_one('td[data-title="响应速度"]').text
        last_verify_time = row.select_one('td[data-title="最后验证时间"]').text
        payment_method = row.select_one('td[data-title="付费方式"]').text

        # 添加到数据列表中
        data_list.append([ip, port, anonymity, proxy_type, location, response_time, last_verify_time, payment_method])

# 创建 DataFrame 对象
df = pd.DataFrame(data_list, columns=['IP', 'PORT', '匿名度', '类型', '位置', '响应速度', '最后验证时间', '付费方式'])

# 将 DataFrame 写入 Excel 文件
excel_path = r'D:\spider_learn\proxy_list.xlsx'
df.to_excel(excel_path, index=False)

print(f"数据已保存到 Excel 文件：{excel_path}")
