import pandas as pd
from h2o_wave import ui, Q


def init_graph_params(q: Q):
    q.client.sns_pic_aspect = 1
    q.client.sns_pic_height = 5
    q.client.sns_linewidth = 1
    q.client.histo_binwidth = 1
    q.client.sns_kde_smooth = 0.5


def read_uploaded_data(q):
    data_path = q.client.working_file_path
    df = pd.read_csv(data_path)
    df_cols = list(df.columns)

    return df_cols


def render_choose_xy(q: Q):
    if q.client.working_file_path is not None:
        cols = read_uploaded_data(q)
        q.client.cards.add('pick_xy')
        q.page['pick_xy'] = ui.form_card(
            box=ui.box('panel', order=1, width='250px', height='850px'),
            items=[
                ui.text_xl('Pick the features you want'),
                # 选择XY,hue,style.size五种变量
                ui.combobox(name='sns_x', label='X', value='',
                            choices=cols),
                ui.combobox(name='sns_y', label='Y', value='',
                            choices=cols),
                ui.combobox(name='sns_hue', label='HUE', value='',
                            choices=cols),
                ui.combobox(name='sns_style', label='Style', value='',
                            choices=cols),
                ui.combobox(name='sns_size', label='Size', value='',
                            choices=cols),
                ui.combobox(name='sns_col', label='Filter by Col', value='',
                            choices=cols),
                ui.combobox(name='sns_row', label='Filter by Row', value='',
                            choices=cols),
            ]
        )
        q.client.cards.add('plot')
        q.page['plot'] = ui.markdown_card(box=ui.box('panel', order=3, width='700px'), title='Your plot!', content='')
    else:
        q.client.cards.add('plot')
        q.page['plot'] = ui.form_card(
            box=ui.box('panel', order=3, width='700px'),
            items=[
                ui.text_xl('UPLOAD DATA FIRST')
            ])

def render_control(q:Q):
    q.client.cards.add('sns_controls')
    q.page['sns_controls'] = ui.form_card(
        box=ui.box('panel', order=2, width='250px', height='850px'),
        items=[
            ui.separator(label='General'),
            ui.combobox(name='plot_category', label='Plot Categories', value=None,  # 沃日 为什么出错在这个地方 设置默认值了之后就没法更新了
                        choices=['Scatter', 'Line', 'Histogram',
                                 'KDE', 'ECDF', 'Joint', 'Catplot',
                                 'Box', 'Violin', 'Bar', 'Count'], trigger=True),
            ui.slider(name='sns_pic_aspect', label='Pic Aspect', min=0.3, max=4, step=0.1,
                      value=q.client.sns_pic_aspect,
                      trigger=True),
            ui.slider(name='sns_pic_height', label='Pic Height', min=1, max=15, step=1,
                      value=q.client.sns_pic_height,
                      trigger=True),
            # ##################################### General

            # 选择颜色
            ui.combobox(name='sns_pic_palette', label='ColorSet', value='husl',
                        choices=['husl', 'Set2', 'Paired', 'rocket', 'mako', 'flare',
                                 'crest', 'magma', 'viridis', 'rocket_r', 'cubehelix',
                                 'Spectral', 'coolwarm', 'seagreen', 'light:b',
                                 'dark:salmon_r', 'Blues', 'Y10rBr', 'vlag',
                                 'icefire'], trigger=True),
            ui.text_xl("Plot Features"),
            # ##################################### Scatter
            ui.separator(label='Scatter Plot'),
            ui.combobox(name='sns_line_marker', label='Marker', value=None,  # 沃日 为什么出错在这个地方 设置默认值了之后就没法更新了
                        choices=[".", ",", "o", "v", "^", "<", ">", "1",
                                 "2", "3", "8", "s", "p", "P", "*", "h",
                                 "H", "+", "x", "X", "D", "d", "|", "_"], trigger=True),
            # ##################################### Line
            ui.separator(label='Line Plot'),
            ui.slider(name='sns_linewidth', label='Line Width',
                      min=0.3, max=5, step=0.1,
                      value=q.client.sns_linewidth,
                      trigger=True),
            ui.combobox(name='sns_line_marker', label='Marker', value=None,  # 沃日 为什么出错在这个地方 设置默认值了之后就没法更新了
                        choices=[".", ",", "o", "v", "^", "<", ">", "1",
                                 "2", "3", "8", "s", "p", "P", "*", "h",
                                 "H", "+", "x", "X", "D", "d", "|", "_"], trigger=True),
            # ##################################### Histogram
            ui.separator(label='Histogram'),
            ui.slider(name='histo_binwidth', label='Bin Width',
                      min=0.5, max=10, step=0.5,
                      value=q.client.histo_binwidth,
                      trigger=True),
            ui.combobox(name='histo_normalization', label='Stat', value='count',
                        choices=['count', 'frequency', 'density', 'probability',
                                 'proportion', 'percent'], trigger=True),
            # 阉割版
            # ##################################### KDE
            ui.separator(label='KDE'),
            ui.checkbox(name='sns_fill', label='Fill', trigger=True),
            ui.checkbox(name='sns_cut', label='Cut Outliar', trigger=True),
            ui.slider(name='sns_kde_smooth', label='Smooth',
                      min=0, max=1, step=0.05,
                      value=q.client.sns_kde_smooth,  # 记得去初始化参数
                      trigger=True),
            ui.combobox(name='sns_multiple', label='Stack', value='stack',
                        choices=['layer', 'stack'], trigger=True),

            # ##################################### catplot
            ui.separator(label='Catplot'),
            ui.checkbox(name='sns_jitter', label='Jitter', value=False, trigger=True),
        ]
    )