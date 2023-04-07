from h2o_wave import main, app, Q, ui, site, data, copy_expando, handle_on, on

from init import clear_cards


@on('#data_summary')
async def render_data_summary(q: Q):
    clear_cards(q, ['table'])
    q.client.cards.add('data_sum')
    q.page['data_sum'] = ui.form_card(
        box=ui.box('panel', order=1, size=1),
        items=[ui.text_xl('DATA SUMMARY'),
               ui.separator(label='Data Shape'),
               ui.text_m('Building...')]
    )
