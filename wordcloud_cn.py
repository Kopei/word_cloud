# -*- coding: utf-8 -*- 
import jieba
import click
# jieba.enable_parallel(4)
# Setting up parallel processes :4 ,but unable to run on Windows
from os import path
from imageio import imread
import matplotlib.pyplot as plt
import os
# jieba.load_userdict("txt\userdict.txt")
# add userdict by load_userdict()
from wordcloud import WordCloud, ImageColorGenerator


@click.command()
@click.option('--txt', default='hrsmartfactory.txt', help='input the txt file for word count.')
@click.option('--out', default='artifacts/smartfactory.jpg', help='output the jpg file.')
def main(txt, out):
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    stopwords_path = d + '/wc_cn/stopwords_cn_en.txt'
    # Chinese fonts must be set
    font_path = d + '/fonts/SourceHanSerif/SourceHanSerifK-Light.otf'
    # the path to save worldcloud
    imgname1 = os.path.join(d, out)
    # imgname1 = d + '/wc_cn/LuXun.jpg'
    # imgname2 = d + '/wc_cn/LuXun_colored.jpg'
    # read the mask / color image taken from
    # back_coloring = imread(path.join(d, d + '/artifacts/hrlogo.jpg'))

    # Read the whole text.
    text = open(path.join(d, txt), encoding='utf-8').read()

    # if you want use wordCloud,you need it
    # add userdict by add_word()
    userdict_list = []

    # The function for processing text with Jieba
    def jieba_processing_txt(text):
        for word in userdict_list:
            jieba.add_word(word)

        mywordlist = []
        seg_list = jieba.cut(text, cut_all=False)
        liststr = "/ ".join(seg_list)

        with open(stopwords_path, encoding='utf-8') as f_stop:
            f_stop_text = f_stop.read()
            f_stop_seg_list = f_stop_text.splitlines()

        for myword in liststr.split('/'):
            if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
                mywordlist.append(myword)
        return ' '.join(mywordlist)


    # wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=back_coloring,
                #    max_font_size=100, random_state=42, width=1000, height=860, margin=2,)
    wc = WordCloud(font_path=font_path, background_color='white', max_words=3000,
                    max_font_size=100, random_state=42, width=1000, height=860, margin=2)


    wc.generate(jieba_processing_txt(text))

    # create coloring from image
    # image_colors_default = ImageColorGenerator(back_coloring)

    plt.figure()
    # recolor wordcloud and show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # save wordcloud
    # wc.to_file(path.join(d, imgname1))

    # create coloring from image
    # image_colors_byImg = ImageColorGenerator(back_coloring)

    # show
    # we could also give color_func=image_colors directly in the constructor
    # plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
    # plt.axis("off")
    # plt.figure()
    # plt.imshow(back_coloring, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

    # save wordcloud
    wc.to_file(path.join(d, imgname1))



if __name__ == "__main__":
    main()