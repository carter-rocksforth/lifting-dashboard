import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Importing the app itself and all the pages
from dashboard import app

# Creating the navigation bar
navbar_links = [
    # Link for the Summary Page
    dbc.NavLink(
        'Summary',
        href='/summary'
    ),
    # Links to the Single Exercise Pages
    dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem('Squats', href='/metrics/squats')
        ],
        label='Types of Exercises',
        color='primary'
    ),
    # Link to the update lift data page
    dbc.NavLink(
        'Input Workout',
        href='/input-data'
    )
]

# Setting the app layout
app.layout = html.Div([
    dcc.Location(id='url'),
    dbc.NavbarSimple(
        children=navbar_links,
        brand='Lifting Dashboard',
        color='primary',
        dark=True,
        fixed='Top'
    ),
    html.Div(style={'padding': 25}),
    # Loading in the page content/layout
    dbc.Container(id='page-content', className='pt-4'),
])


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
