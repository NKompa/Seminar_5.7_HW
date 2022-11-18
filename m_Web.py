import view

def All_Web():
    new_data = view.All_view()
    style = 'style = "font-size:20px;"'
    html = '<html>\n <head></head>\n <body>\n'
    for i in new_data:
        html += '     <p {}> {} </p>\n'.format(style, i)
    with open('web.html', 'w', encoding='utf-8') as page:
        page.write(html)
    return html