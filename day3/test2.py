import requests
from lxml import etree
import os
from urllib.parse import urljoin


def download_images():
    # 目标网站URL
    base_url = "http://pic.netbian.com/"

    # 创建保存图片的目录
    save_dir = "d:/images/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    try:
        # 向目标网站发送请求并获取网页源码
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        # 指定字符集
        response.encoding = "gbk"

        # 解析网页
        html = etree.HTML(response.text)

        # 获取图片URL列表
        img_elements = html.xpath("//ul[@class='clearfix']/li/a/span/img")
        img_urls = [img.get('src') for img in img_elements if img.get('src')]

        print(f"找到 {len(img_urls)} 张图片")

        # 下载图片
        for i, img_url in enumerate(img_urls, 1):
            try:
                # 拼接完整的图片URL
                full_url = urljoin(base_url, img_url)

                # 获取图片响应
                img_response = requests.get(full_url, headers=headers, timeout=10)
                img_response.raise_for_status()

                # 从URL中提取文件名
                filename = os.path.basename(img_url)
                # 如果没有扩展名，则添加.jpg
                if not os.path.splitext(filename)[1]:
                    filename += ".jpg"

                # 保存路径
                save_path = os.path.join(save_dir, filename)

                # 写入文件
                with open(save_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"已下载第 {i} 张图片: {filename}")

            except Exception as e:
                print(f"下载第 {i} 张图片时出错: {e}")
                continue

    except Exception as e:
        print(f"爬取过程中出错: {e}")
    finally:
        print("下载任务完成")

# 下载到D盘的images
if __name__ == "__main__":
    download_images()