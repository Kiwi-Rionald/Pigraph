import base64
import io

import pandas as pd
from h2o_wave import ui, on, Q, copy_expando

from func_data_vis import *
from init import clear_cards
from plot_sns import *


@on('#data_vis')
async def render_dv_view(q: Q):
    # del q.page['upload']
    # del q.page['table']
    # del q.page['error_vis']
    clear_cards(q, ['pick_xy', 'plot', 'sns_controls'])
    if not q.client.plot_initialized:  # First visit
        q.client.plot_initialized = True
        init_graph_params(q)
        render_choose_xy(q)
        render_control(q)
        # TODO: 逗嫩个 不要再动它了！！！！


    copy_expando(q.args, q.client)

    if q.client.working_file_path is not None:
        df = pd.read_csv(q.client.working_file_path)


        if q.client.plot_category == 'Scatter':
            img_fileName = sns_scatter(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'Line':
            img_fileName = sns_line(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'Histogram':
            img_fileName = sns_histogram(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'KDE':
            img_fileName = sns_KDE(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'ECDF':
            img_fileName = sns_ECDF(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'Joint':
            img_fileName = sns_joint(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'Catplot':
            img_fileName = sns_catplot(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'Box':
            img_fileName = sns_box(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'Violin':
            img_fileName = sns_violin(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'Bar':
            img_fileName = sns_bar(q, df)
            await show_pic(img_fileName, q)

        if q.client.plot_category == 'Count':
            img_fileName = sns_count(q, df)
            await show_pic(img_fileName, q)

    # Save page
    await q.page.save()

