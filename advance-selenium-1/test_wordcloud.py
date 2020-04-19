
"""
@Author   :linda
@File     :test_wordcloud.py
@Time     :2020/3/29 9:20 PM
@Software :Pycharm
@Copyright (c) 2020,All Rights Reserved.
"""

import re
import collections
import numpy as np
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt


class Text2WordCloud:
    def __init__(self,
                 file_path,
                 stopwords_path,
                 template_pic_path,
                 output_pic_path):
        self.file_path = file_path
        self.stopwords_path = stopwords_path
        self.template_pic_path = template_pic_path
        self.output_pic_path = output_pic_path

    def load(self):
        self.mask = np.array(Image.open(self.template_pic_path))  # 定义词频背景
        self.stopwords = self.read_file(self.stopwords_path)  # 读取停顿词
        self.ww = [word[0] for word in self.stopwords]
        self.pattern = re.compile("|".join(self.ww))  # 定义正则表达式匹配模式
        self.data = self.read_file(self.file_path)  # 读取文件内容
        self.string_data = ""
        for data in self.data:
            self.string_data += data[0]
        self.string_data += re.sub(self.pattern, '', self.string_data)  # 将符合模式的字符去除

    # 读取文档
    @staticmethod
    def read_file(filename, sep="\t"):
        if ".txt" in filename:
            with open(filename, 'r', encoding="utf-8-sig") as file:
                lines = file.readlines()
                if sep is not None:
                    lines = [line.replace("\n", "").split(sep) for line in lines]
                else:
                    lines = [line.replace("\n", "") for line in lines]
                return lines

    def count(self):
        # step 1: jieba分词切分
        object_list = jieba.cut(self.string_data, cut_all=False)  # 精确模式分词

        # step 2: 统计词频
        self.word_counts = collections.Counter(object_list)  # 对分词做词频统计
        # word_counts_topK = self.word_counts.most_common(20)  # 获取前K最高频的词
        # print(word_counts_topK)  # 输出检查

    def plot(self):
        wc = wordcloud.WordCloud(
            background_color='white',  # 设置背景颜色
            font_path='/System/Library/Fonts/Hiragino Sans GB.ttc',  # 设置字体格式
            mask=self.mask,  # 设置背景图
            max_words=200,  # 最多显示词数
            max_font_size=80,  # 字体最大值
            scale=128  # 调整图片清晰度，值越大越清楚
        )

        wc.generate_from_frequencies(self.word_counts)  # 从字典生成词云
        image_colors = wordcloud.ImageColorGenerator(self.mask)  # 从背景图建立颜色方案
        wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
        wc.to_file(self.output_pic_path)  # 将图片输出为文件
        plt.imshow(wc)  # 显示词云
        plt.axis('off')  # 关闭坐标轴
        plt.show()  # 显示图像


if __name__ == "__main__":
    twc = Text2WordCloud(
        file_path="zhiwei.txt",
        stopwords_path="stopwords.txt",
        template_pic_path="图2.jpg",
        output_pic_path="/Users/lindafang/PycharmProjects/seleniumforpython2020/advance-selenium-1/res.png"
    )
    twc.load()
    twc.count()
    twc.plot()