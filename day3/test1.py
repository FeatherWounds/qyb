import requests
import re


def get_douban_chart_top_movies():
    # 豆瓣电影排行榜URL
    url = 'https://movie.douban.com/chart'

    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # 获取网页内容
        html = response.text

        # 定义正则表达式模式
        movie_pattern = re.compile(
            r'<div class="pl2">\s*<a href="(.*?)".*?>(.*?)</a>.*?'
            r'<span class="rating_nums">(.*?)</span>',
            re.DOTALL
        )

        # 查找所有匹配项
        matches = movie_pattern.findall(html)

        # 处理结果
        movies = []
        for i, match in enumerate(matches[:10], 1):  # 只取前10个
            link = match[0].strip()
            name = re.sub(r'\s+', '', match[1])  # 去除所有空白字符
            name = re.sub(r'<.*?>', '', name)  # 去除HTML标签
            rating = match[2].strip()

            movies.append({
                'rank': i,
                'name': name,
                'rating': rating,
                'link': link
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
    for movie in top_movies:
        print(f"{movie['rank']}. {movie['name']} | 评分: {movie['rating']} | 链接: {movie['link']}")
else:
    print("未能获取电影列表")