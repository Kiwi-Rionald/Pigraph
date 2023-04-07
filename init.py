import base64
import os.path
from typing import Optional, List

from h2o_wave import Q, ui
from PIL import Image
from func_data_vis import init_graph_params


async def init_page(q):
    """ 更改之前没有async和if条件判断 """
    # 确认已初始化
    # q.client.initialized = True

    init_graph_params(q)
    if q.args['#'] is None:
        render_start_page(q)  # meta，header，sidebar，footer


def render_start_page(q: Q):
    render_meta(q)
    render_header(q)
    render_sidebar(q)
    render_footer(q)
    path = 'https://s1.ax1x.com/2023/04/06/ppov8Cn.png'
    q.client.cards.add('welcome')
    # q.page['welcome'] = ui.form_card(
    #     box=ui.box('panel'),
    #     items=[
    #         ui.image(title='1', path=path, width='1250px')
    #     ],
    # )
    content = '''
    
    Have a wonderful trip with this app! :)
   
    '''
    q.page['welcome'] = ui.tall_article_preview_card(
        box=ui.box('panel'),
        title='Welcome to my DV Project',
        subtitle='Start from your left',
        name='tall_article',
        image=path,
        content=content,
        items=[
            ui.buttons(items=[
                ui.button(name='like', icon='Like'),
                ui.button(name='comment', icon='CommentAdd'),
                ui.button(name='share', icon='Share'),
            ]),
        ]
    )


def render_meta(q: Q):
    # 元数据设置
    q.page['meta'] = ui.meta_card(
        box='',
        layouts=[ui.layout(breakpoint='xs', zones=[  # 定义三个区域
            ui.zone(name='header'),
            ui.zone(name='body', direction=ui.ZoneDirection.ROW,
                    zones=[
                        ui.zone(name='sidebar', size='15%'),
                        ui.zone(name='panel', size='85%', direction=ui.ZoneDirection.ROW)
                    ],
                    size='100%'),
            ui.zone(name='footer')
        ])],
        themes=[
            ui.theme(
                name='theme1',
                primary='#145152',
                text='#2b2b2b',
                card='#ededed',
                page='#d1d1d1',
            ),
            ui.theme(
                name='theme2',
                primary='#a9bfcc',
                text='#e8e8e8',
                card='#3d3d3d',
                page='#1f1f1f',
            ),
            ui.theme(
                name='theme3',
                primary='#51a9ad',
                text='#ebebeb',
                card='#292929',
                page='#000000',
            )
        ],
        title='Kiwi DV Project NEW GUI',
        theme='theme3'
    )


def render_header(q: Q):
    # Header
    q.page['header'] = ui.header_card(
        box=ui.box('header'),
        title='🐷Piggy Visual',
        subtitle='Data Visualizing ALL in ONE',
        items=[ui.menu(image='https://s1.ax1x.com/2023/04/06/ppovrCR.jpg', items=[
            ui.command(name='profile', label='Profile', icon='Contact'),
            ui.command(name='preferences', label='Preferences', icon='Settings'),
            ui.command(name='logout', label='Logout', icon='SignOut'),
        ])],
        secondary_items=[
            ui.mini_button(name="btn_visualizing", label="Vis", icon='Savings'),
            ui.mini_button(name="btn_community", label="COMMUNITY", icon='Home'),
            ui.mini_button(name="btn_donate", label="DONATE", icon='Money'),
            ui.mini_button(name="btn_help", label="HELP", icon='EditContact'),
        ],
    )


def render_sidebar(q: Q):
    # Sidebar
    q.page['nav'] = ui.nav_card(
        box=ui.box('sidebar'),
        items=[
            ui.nav_group('Data Visualizing', items=[
                ui.nav_item(name='#upload', label='Data Upload'),
                ui.nav_item(name='#data_summary', label='Data Summary'),
                ui.nav_item(name='#data_vis', label='Visualizing'),
                ui.nav_item(name='#building', label='Developing', disabled=True),
            ]),
            ui.nav_group('Data Preprocessing', items=[
                ui.nav_item(name='#preprocessing', label='Data Preprocessing', disabled=True),
            ]),
            ui.nav_group('Others', items=[
                ui.nav_item(name='#about', label='About', icon='Info'),
                ui.nav_item(name='#support', label='Support', icon='Help'),
            ])
        ]
    )


def render_footer(q: Q):
    # Footer
    q.page['footer'] = ui.footer_card(
        box=ui.box('footer'),
        caption='Thanks for using!💛',
        items=[
            ui.inline(justify='end', items=[
                ui.links(label='Basic', width='200px', items=[
                    ui.link(label='Pandas', path='https://pandas.pydata.org/', target='_blank'),
                    ui.link(label='H2O Wave', path='https://wave.h2o.ai/', target='_blank'),
                    ui.link(label='Kaggle', path='https://www.kaggle.com/', target='_blank'),
                ]),
                ui.links(label='Plotting', width='200px', items=[
                    ui.link(label='Seaborn', path='https://seaborn.pydata.org/', target='_blank'),
                    ui.link(label='Scikit-Learn', path='https://scikit-learn.org/stable/', target='_blank'),
                    ui.link(label='Numpy', path='https://www.numpy.org.cn/reference/', target='_blank'),
                ]),
                ui.links(label='Developing', width='200px', items=[
                    ui.link(label='Matplotlib', path='https://matplotlib.org/stable/api/index.html', target='_blank'),
                    ui.link(label='PyCharm', path='https://www.jetbrains.com/pycharm/', target='_blank'),
                    ui.link(label='Sample link', path='https://www.h2o.ai/', target='_blank'),
                ]),
            ]),
        ]
    )


def clear_cards(q, ignore: Optional[List[str]] = []) -> None:
    if not q.client.cards:
        return

    for name in q.client.cards.copy():
        if name not in ignore:
            del q.page[name]
            q.client.cards.remove(name)
