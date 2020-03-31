import jieba  # 中文分词包
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from os import path

# 解决汉字问题
jieba.load_userdict("zhiwei1.txt")

chtext = ''
# 打开文件 ，切词
with open('zhiwei.txt', 'r') as fin:
    for line in fin.readlines():
        line = line.strip('\n')
        chtext += ' '.join(jieba.cut(line))

# 调用包PIL中的open方法，读取背景图片文件，通过numpy中的array方法生成数组
backgroud_Image = np.array(Image.open("图4.jpg"))

# 绘制词云图
wc = WordCloud(
    background_color='white',  # 设置背景颜色，与图片的背景色相关
    mask=backgroud_Image,  # 设置背景图片
    #mac这么写，window字体在另一地方c:/Windows/Fonts/simsun.ttc或 C:/Windows/Fonts/simfang.ttf

    font_path='/System/Library/Fonts/Hiragino Sans GB.ttc',  # 显示中文，可以更换字体
    max_words=800,  # 设置最大显示的字数
    stopwords={'编写','了解','精通','并','要求','优先','具有','至少一种','关键字','流程','系统','经验','工具','软件','项目','产品','测试','of','分享','熟练掌握','职能','基本','to','公司','or','以上学历','类别','根据','for','具备','进行','工程师','相关','包括','任职','资格','岗位职责','完成','熟悉','以上','微信','工作','和','负责','的','等','\\','.','、','n1','n2','n3','n4','n5','n6','n7','n8','and'},  # 设置停用词，停用词则不再词云图中表示
    max_font_size=1000,  # 设置字体最大值
    random_state=1,  # 设置有多少种随机生成状态，即有多少种配色方案
    scale=1  # 设置生成的词云图的大小
)
print(chtext)
# 传入需画词云图的文本
wc.generate(chtext)

# 给词加上颜色
image_colors = ImageColorGenerator(backgroud_Image)
plt.imshow(wc.recolor(color_func=image_colors))

# 隐藏图像坐标轴
plt.axis("off")
# 展示图片
plt.show()
# 保存生成的词云图
wc.to_file('reg.jpg')
