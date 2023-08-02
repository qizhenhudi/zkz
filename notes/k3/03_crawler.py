import requests
from bs4 import BeautifulSoup


def get_diary_entries(url):
    # 发起HTTP的GET请求，获取网页内容
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析网页内容
        soup = BeautifulSoup(response.content, 'html.parser')

        # 使用soup定位每天日志所在位置
        diary_entries = soup.find_all('div', class_='entry-content')  #  使用 soup.find_all('div', class_='entry-content') 来找到网页中所有 <div class="entry-content"> 的元素

        # 用于存储所有日志内容的列表
        entries_list = []

        # 遍历每天的日志，提取文本内容
        for entry in diary_entries:
            entry_text = entry.get_text().strip()
            entries_list.append(entry_text)

        return entries_list
    else:
        # 请求失败时返回空列表
        print(f"请求失败. 状态码: {response.status_code}")
        return []


if __name__ == "__main__":

    url = "http://www.ncku1897.net/diary/1936.html"

    diary_entries = get_diary_entries(url)

    if diary_entries:
        # 打印每个日志条目的内容
        for index, entry in enumerate(diary_entries, start=1):
            print(f"Entry {index}:")  # f是格式化字符串
            print(entry)
            print("-" * 100)
    else:
        print("No diary entries found.")
