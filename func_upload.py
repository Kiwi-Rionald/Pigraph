import os
import time

import pandas as pd
from h2o_wave import Q, ui


def render_upload_view(q: Q):
    """Sets up the upload-dataset card"""
    # 先检查路径是否合法
    check_dir_available(q)
    q.client.cards.add('upload')
    q.page['upload'] = ui.form_card(
        box=ui.box('panel', order=1, width='300px'),  # 必须指定order过后才能指定size
        items=[
            ui.message_bar(
                type='info',
                text='Please upload a .csv file first :)',
            ),
            ui.file_upload(name='file_upload', label='UPLOAD',
                           multiple=False,  # 不允许多个文件上传
                           file_extensions=['csv'],
                           tooltip='Choose a .csv file you wanna upload from your PC'),
        ]
    )


def render_table_view(q: Q):
    """Sets up the view a file as ui. table card"""

    items = [ui.separator(label='Here\'s the uploaded data')]

    if q.client.working_file_path is None:
        items.append(ui.message_bar(type='warning', text='Please upload a dataset!'))
    else:
        items.append(ui.text_xl(os.path.basename(q.client.working_file_path)))
        items.append(make_ui_table(file_path=q.client.working_file_path, n_rows=15, name='head_of_table'))
    q.client.cards.add('table')
    q.page['table'] = ui.form_card(box=ui.box('panel', order=2, size=3), items=items)


def check_dir_available(q: Q):
    q.client.data_path = './data'
    if not os.path.exists(q.client.data_path):
        os.mkdir(q.client.data_path)


def make_ui_table(file_path: str, n_rows: int, name: str):
    """Creates an ui.table object from a csv file"""

    df = pd.read_csv(file_path)
    n_rows = min(n_rows, df.shape[0])

    table = ui.table(
        name=name,
        columns=[ui.table_column(name=str(x), label=str(x), sortable=True) for x in df.columns.values],
        rows=[ui.table_row(name=str(i), cells=[str(df[col].values[i]) for col in df.columns.values])
              for i in range(n_rows)]
    )
    return table


def read_uploaded_data(q):
    data_path = q.client.working_file_path
    df = pd.read_csv(data_path)
    df_cols = df.columns

    return df_cols


async def show_data_preview(q: Q):
    """Saves a file uploaded by a user from the UI"""
    data_path = q.client.data_path

    # Download new dataset to data directory
    q.client.working_file_path = await q.site.download(url=q.args.file_upload[0], path=data_path)
    # Update views to end user
    render_table_view(q)
    time.sleep(1)  # show the Upload Success for 1 second before refreshing this view
    render_upload_view(q)
