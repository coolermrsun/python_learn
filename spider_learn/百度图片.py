import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
w = 0
for page in range(0,240,30):
    url = f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10396256610956082189&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%B0%8F%E5%A7%90%E5%A7%90%E5%9B%BE%E7%89%87&queryWord=%E5%B0%8F%E5%A7%90%E5%A7%90%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn={page}&rn=30&gsm=5a&1702440639092="
    response = requests.get(url=url, headers=headers)
    # response.encoding = 'utf-8'
    # html = response.json
    data = response.json()['data']
    p_urls = [item['hoverURL'].replace('_s', '') for item in data if 'hoverURL' in item]

    save_folder = 'D:\\spider_learn\\demo_jpg'
    os.makedirs(save_folder, exist_ok=True)

    for i, image_url in enumerate(p_urls):
        w = w + 1
        image_response = requests.get(url=image_url, headers=headers)

        # 从URL中提取图片文件名
        file_name = os.path.join(save_folder, f'image_{w}.jpg')

        with open(file_name, 'wb') as image_file:
            image_file.write(image_response.content)

print(f'{w} 张图片已下载并保存至 {save_folder}')
