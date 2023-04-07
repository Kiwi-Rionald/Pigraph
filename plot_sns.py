from h2o_wave import main, app, Q, ui, site, data
import os
import time
import uuid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io


sns.set_theme(style="darkgrid")

"""
    Seaborn引擎板块, 返回生成图片的filename
    
    规范: 每个生成图后面加上代码
    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)
    return image_filename
    
    一定有的是
    data=data,
    x=q.client.sns_x,
    y=q.client.sns_y,
    palette=q.client.sns_pic_palette,
    
"""

""" template

def sns_(q:Q, data):
    plt.figure(figsize=(5, 5))
    
    # ############### CUSTOM ###########
    sns.x(data=data,
        x=q.client.sns_x,
        y=q.client.sns_y,
        palette=q.client.sns_pic_palette,
        col=q.client.col,
        row=q.client.row,)
    # ############### CUSTOM ###########
    
    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)
    
    return image_filename
    
    * 某类型图特有的属性名字前面加上这个图的类型名,例如histo_bindwidth
    * 写程序的时候再来对照着这个文件和jupyter的笔记写, 对于一些有冲突的项目,需要在combobox的默认提示中指明 
"""


def sns_scatter(q: Q, data):
    plt.figure(figsize=(5, 5))
    sns.relplot(x=q.client.sns_x,
                y=q.client.sns_y,
                hue=q.client.sns_hue,
                style=q.client.sns_style,
                palette=q.client.sns_pic_palette,
                col=q.client.col,  # ################################### new feature
                row=q.client.row,  # ################################### new feature
                size=q.client.sns_size,
                # s=q.client.dot_size,  # ################################### new feature
                sizes=(15, 200),  # 每个点的形状大小根据对应的值改变
                data=data,
                markers=q.client.sns_line_marker,
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height)
    # pic_IObytes = io.BytesIO()
    # plt.savefig(pic_IObytes, format='png')
    # pic_IObytes.seek(0)
    # image = base64.b64encode(pic_IObytes.read()).decode()
    #
    # return image

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


# 连续的line
def sns_line(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.relplot(data=data,
                x=q.client.sns_x,
                y=q.client.sns_y,
                palette=q.client.sns_pic_palette,
                hue=q.client.sns_hue,
                style=q.client.sns_style,
                size=q.client.sns_size,
                col=q.client.col,
                row=q.client.row,
                sizes=(15, 200),
                linewidth=q.client.sns_linewidth,
                kind="line",
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height,
                marker=q.client.sns_line_marker,
                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


def sns_histogram(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.displot(data=data,
                x=q.client.sns_x,
                y=q.client.sns_y,
                palette=q.client.sns_pic_palette,
                col=q.client.col,
                row=q.client.row,
                binwidth=q.client.histo_binwidth,  # ################################### new feature
                # element=q.client.histo_transparent_histo,  # ################################### new feature
                # 可选None和step, 效果是分类展示重叠且透明
                # multiple=q.client.histo_stackBinOrStandByBin,  # ################################### new feature
                # 可选None,stack重叠起来, dodge,不同类并排展示
                stat=q.client.histo_normalization,  # ################################### new feature
                # 可选None, density,条状图面积正则到1, "probability",安条状长度正则到1
                # common_norm=q.client.histo_commonNorm,  # ################################### new feature
                # boolean
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height
                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


# TODO:Done 可以像下面处理None值
def sns_KDE(q: Q, data):  # 分为一维二维
    plt.figure(figsize=(5, 5))

    # if q.client.sns_multiple:
    #     multiple = 'stack'
    # else:
    #     multiple = None

    # ############### CUSTOM ###########
    sns.displot(data=data,
                x=q.client.sns_x,
                palette=q.client.sns_pic_palette,
                col=q.client.col,
                row=q.client.row,
                hue=q.client.sns_hue,
                multiple=q.client.sns_multiple,  # ################################### new feature
                # 可选stack和None
                cut=q.client.sns_cut,  # # ################################### new feature
                # 0时去掉极端点
                fill=q.client.sns_fill,  # ################################### new feature
                # True, False
                bw_adjust=q.client.sns_kde_smooth,  # ################################### new feature
                # 0-1 决定曲线的平滑程度
                kind="kde",
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height
                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


# TODO:Done
def sns_ECDF(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.displot(data=data,
                x=q.client.sns_x,
                palette=q.client.sns_pic_palette,
                col=q.client.col,
                row=q.client.row,
                hue=q.client.sns_hue,
                kind="ecdf",
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height
                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


def sns_joint(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.jointplot(data=data,
                  x=q.client.sns_x,
                  y=q.client.sns_y,
                  palette=q.client.sns_pic_palette,
                  hue=q.client.sns_hue,
                  # aspect=q.client.sns_pic_aspect,
                  # height=q.client.sns_pic_height
                  )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


def sns_summary(q: Q, data):
    # 指pairplot
    pass


# TODO: 到这里出错了
def sns_catplot(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.catplot(data=data,
                x=q.client.sns_x,
                y=q.client.sns_y,
                palette=q.client.sns_pic_palette,
                col=q.client.col,
                row=q.client.row,
                hue=q.client.sns_hue,
                size=q.client.sns_size,
                kind="swarm",
                jitter=q.client.sns_jitter,  # ################################### new feature
                # 默认True，用于把所有东西堆在一起
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height
                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


def sns_box(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.boxplot(data=data,
                x=q.client.sns_x,
                y=q.client.sns_y,
                palette=q.client.sns_pic_palette,
                col=q.client.col,
                row=q.client.row,
                hue=q.client.sns_hue,
                dodge=q.client.sns_dodge,  # ################################### new feature
                # 默认True
                kind=q.client.sns_box_kind,
                # 默认box，可选boxen
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height

                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


def sns_violin(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.catplot(data=data,
                x=q.client.sns_x,
                y=q.client.sns_y,
                palette=q.client.sns_pic_palette,
                col=q.client.col,
                row=q.client.row,
                hue=q.client.sns_hue,
                kind="violin",
                bw=q.client.sns_width,  # ################################### new feature
                cut=0,
                split=q.client.sns_split,  # ################################### new feature
                # 默认False， 可选True
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height
                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


def sns_bar(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.barplot(data=data,
                x=q.client.sns_x,
                y=q.client.sns_y,
                palette=q.client.sns_pic_palette,
                # col=q.client.col,
                # row=q.client.row,
                hue=q.client.sns_hue,
                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename


def sns_count(q: Q, data):
    plt.figure(figsize=(5, 5))

    # ############### CUSTOM ###########
    sns.catplot(data=data,
                x=q.client.sns_x,
                palette=q.client.sns_pic_palette,
                kind="count",
                aspect=q.client.sns_pic_aspect,
                height=q.client.sns_pic_height
                )
    # ############### CUSTOM ###########

    image_filename = f'{str(uuid.uuid4())}.png'
    plt.savefig(image_filename)

    return image_filename

async def show_pic(fileName, q:Q):
    image_path, = await q.site.upload([fileName])

    # Clean up
    os.remove(fileName)

    # Display our plot in our markdown card
    q.page['plot'].content = f'![plot]({image_path})'

    await q.page.save()