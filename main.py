import os
import time
from init import init_page
from func_upload import show_data_preview, render_upload_view, render_table_view
from dv_page_data_sum import *
import pandas as pd
from h2o_wave import main, app, Q, ui, site, data, copy_expando, handle_on, on


from dv_page_upload import *
from dv_page_data_vis import *
from plot_sns import *


@app('/demo')
async def serve(q: Q):
    if not q.client.initialized:
        q.client.cards = set()
        await init_page(q)
        q.client.initialized = True
    # else:
    #     copy_expando(q.args, q.client)
    #     await handle_on(q)

    copy_expando(q.args, q.client)

    if q.args.file_upload:
        await show_data_preview(q)

    await handle_on(q)
    #
    #
    #
    # if q.client.working_file_path is not None:
    #     df = pd.read_csv(q.client.working_file_path)
    #
    #     if q.client.plot_category == 'Scatter':
    #         img_fileName = sns_scatter(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'Line':
    #         img_fileName = sns_line(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'Histogram':
    #         img_fileName = sns_histogram(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'KDE':
    #         img_fileName = sns_KDE(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'ECDF':
    #         img_fileName = sns_ECDF(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'Joint':
    #         img_fileName = sns_joint(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'Catplot':
    #         img_fileName = sns_catplot(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'Box':
    #         img_fileName = sns_box(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'Violin':
    #         img_fileName = sns_violin(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'Bar':
    #         img_fileName = sns_bar(q, df)
    #         await show_pic(img_fileName, q)
    #
    #     if q.client.plot_category == 'Count':
    #         img_fileName = sns_count(q, df)
    #         await show_pic(img_fileName, q)

    await q.page.save()
