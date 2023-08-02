import requests
from lxml import html


def get_diary_entries(url):
    # 发起HTTP的GET请求，获取网页内容
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析网页内容
        tree = html.fromstring(response.content)

        # 使用XPath定位每天日志所在位置
        diary_entries = tree.xpath('//div[@class="entry-content"]')  # 核心部分  //表示从根节点开始搜索

        # 用于存储所有日志内容的列表
        entries_list = []

        # 遍历每天的日志，提取文本内容
        for entry in diary_entries:
            entry_text = entry.text_content().strip()
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
        for index, entry in enumerate(diary_entries, start=1):  # start=1 就是修改默认的起始点
            print(f"Entry {index}:")  # f是格式化字符串
            print(entry)
            print("-" * 100)
    else:
        print("No diary entries found.")
