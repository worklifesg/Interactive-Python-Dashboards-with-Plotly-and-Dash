# In this small program, we will see how to include Markdowns in our Dash
# Aloows text for links, italics, bold text, bullet lists and more.

import dash 
import dash_html_components as html 
import dash_core_components as dcc 

app = dash.Dash()

markdown_text = '''
#### Dash and Markdown
Dash supports [Markdown](http://commonmark.org/help).
Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.

'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ =='__main__':
    app.run_server()
