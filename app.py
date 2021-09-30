'''
Dashy app entrypoint.
'''
from Dashy.dashy import dash_app


if __name__ == '__main__':
    dash_app.run_server(debug=True, port=8056)
