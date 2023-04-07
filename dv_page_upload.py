from h2o_wave import on, Q

from func_upload import render_upload_view, render_table_view
from init import clear_cards


@on('#upload')
async def render_upload(q: Q):
    # del q.page['sns_controls']
    # del q.page['pick_xy']
    # del q.page['plot']
    clear_cards(q)
    # 不要加 加了会出错
    render_upload_view(q)
    render_table_view(q)