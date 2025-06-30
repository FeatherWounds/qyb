import requests
from bs4 import BeautifulSoup


def get_douban_top10():
    # 豆瓣电影Top250的URL
    url = 'https://movie.douban.com/top250'

    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功

        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找所有电影标题（前10个）
        movie_items = soup.find_all('div', class_='hd', limit=10)

        # 提取电影名称
        top10_movies = []
        for index, item in enumerate(movie_items, 1):
            title = item.a.span.text.strip()
            top10_movies.append((index, title))

        return top10_movies

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None


# 获取并打印结果
top10 = get_douban_top10()
if top10:
    print("豆瓣电影Top10:")
    for rank, title in top10:
        print(f"{rank}. {title}")
else:
    print("未能获取电影列表")