# coding=utf-8
import requests
import re
from lxml import etree
from contextlib import closing
import threading

class LessonSpider():
    def __init__(self):
        self.url = "https://edu.hellobi.com/course/157/lessons"
        self.path = "C:/Users/Administrator/Desktop/视频/"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "cookie": "pgv_pvi=5986036736; _ga=GA1.2.1350823578.1543295638; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjBjWVlnVWtVT21sWVVKUEhyM1VnTWc9PSIsInZhbHVlIjoibG9YaHBXS0ZEbEV5eklSK0M3YlVSdEloSlozd2hcL1wva1g0WjRUb0hkWmhIOTZiY294dDV1UFdSTkx5TmtZbHlWSDdYSmVOZ1BOM1diMUtFclNEZmdFQVBFRGZRT256KzZIcHhDRkp4Y093ZXJ1c3FVUER0TzVNRlU3U3dQNVVxOVY5MUJKd2JhdmJcL01Udk54cEVNeWlnPT0iLCJtYWMiOiJjOTE3MDliMjdkZTc2OTMyNzYyZTE3N2VkNjA2MWU4MjRhMjUzZTMyOTk2NDYxN2VkYWJjZjViMjg4N2MwOTIzIn0%3D; sqv__user_login=qJqYlMFkb25qcplTc16nqZnUxaKRz8iXwF-zS9kgSwrJIPC8SPPxHMXY31NzXqKXp9Xdo6LGwZaOl2vEYMObyWhqmm6Yb2ptlG_El2mTlG5nk8pklZvJbpU.; pgv_si=s420018176; Hm_lvt_2d2777148aa1618ef79baf55c005df84=1544146789,1544187056,1544250275,1544411306; poptimese=1; _gid=GA1.2.1021330376.1544521040; XSRF-TOKEN=eyJpdiI6IkZXcEl6SzJlaUdBY1JKc3NQM3lsQkE9PSIsInZhbHVlIjoiTVVGQmVLMkU0SmhWUGpXU29IMDlTMmtcL1lJdFExc3dJaFJcLzFEZVRIbGd5Z0FPbUdNdDBhdDQwZzZDS3FJMWMrS0VTQ2xORThlbkVzek1sYjFWUU5cL3c9PSIsIm1hYyI6IjFiOGI2NTg2NjFlMDQ4M2M3YTRjZTU4NzdhYmQ1MmEyODk1MTVkMzVkMzc3MzNhZTFmNDQ2MWU4ZWJiNDYyNGUifQ%3D%3D; laravel_session=eyJpdiI6ImpxN2lCb3hrNGVZbzdSbm4wUWgwMmc9PSIsInZhbHVlIjoiUU1Ta2tpeit1ZWJ4bzcrU2V4OGZ0UzlLVFwvUnpzTlJmNlVhbmlSUW1qZ1JUTHE4NHBXNVlcL2NkdHdnZVFydXRCTFRuNVEzd3pSVTRcL0dUMW1HS3dPWkE9PSIsIm1hYyI6IjdmYmNhZmQwNTU4ODk5NzAzNjQwMDNjYzI5NWFkZGZkMWFhNjI1NTVjNTQ5ZjY5N2FkYjQ4MDU2ZWUzYTZkMGYifQ%3D%3D; Hm_lpvt_2d2777148aa1618ef79baf55c005df84=1544522318"
        }

    def get_url_list(self):
        response = requests.get(self.url, headers=self.headers)
        html = etree.HTML(response.text)
        lesson_course = html.xpath("//ul[@class='period-list']/li[contains(@class,'period')]/a/@href")
        lesson_title = html.xpath("//ul[@class='period-list']/li[contains(@class,'period')]/a/span[1]/text()")
        return {
            "lesson_course": lesson_course,
            "lesson_title": lesson_title
        }

    def parse_url(self,url):
        response = requests.get(url, headers=self.headers)
        return response.text

    def get_content(self, html_list):
        pattern_video = re.compile('var config.*?url: \"(.*?)\",',re.S)
        url_mp4 = re.findall(pattern_video, html_list)
        return url_mp4

    def save_to_mp4(self, content_list,title):
        print(content_list)
        with closing(requests.get(content_list[0], headers=self.headers, stream=True)) as r:
            chunk_size = 1024
            content_size = int(r.headers['content-length'])
            path =self.path + title + '.mp4'
            print('下载开始')
            with open(path, "wb") as f:
                n = 1
                for chunk in r.iter_content(chunk_size=chunk_size):
                    loaded = n * 1024.0 / content_size
                    f.write(chunk)
                    if n % 10000 == 0:
                        print('已下载{0:%}'.format(loaded))
                    n += 1

    def run(self):
        # 1、获取url_list
        url_list=self.get_url_list()
        # 2、遍历，发送请求，获取响应
        for url in range(0,len(url_list["lesson_course"])):
            html_str = self.parse_url(url_list["lesson_course"][url])
        # 3、提取数据
            content_list = self.get_content(html_str)
            title = url_list["lesson_title"][url]
            print(title)
        # 4、保存
            self.save_to_mp4(content_list,title)
            print('%s:下载完成' % title)
        print('全部下载完成')


if __name__ == '__main__':
    lesson = LessonSpider()
    lesson.run()
