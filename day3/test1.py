import requests
from bs4 import BeautifulSoup


def get_douban_chart_top_movies():
    # 豆瓣电影排行榜URL
    url = 'https://movie.douban.com/chart'

    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://movie.douban.com/'
    }

    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找排行榜中的电影项目
        movies = []
        items = soup.find_all('div', class_='pl2', limit=10)  # 限制获取前10个

        for item in items:
            # 提取电影名称（去除多余空格和换行）
            name = item.a.text.strip().replace('\n', '').replace(' ', '')
            # 提取详情页链接
            link = item.a['href']
            # 提取评分
            rating = item.find('span', class_='rating_nums').text if item.find('span', class_='rating_nums') else '暂无评分'

            movies.append({
                'name': name,
                'link': link,
                'rating': rating
            })

        return movies

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None
    except Exception as e:
        print(f"解析出错: {e}")
        return None


# 获取并打印结果
top_movies = get_douban_chart_top_movies()
if top_movies:
    print("豆瓣电影排行榜Top10:")
    for i, movie in enumerate(top_movies, 1):
        print(f"{i}. {movie['name']} | 评分: {movie['rating']} | 链接: {movie['link']}")
else:
    print("未能获取电影列表")