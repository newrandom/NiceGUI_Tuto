import webview

if __name__ == '__main__':
    # Create a standard webview window
    webview.settings['ALLOW_DOWNLOADS'] = False
    window = webview.create_window('Simple browser', 'https://pywebview.flowrl.com/download')
    webview.start()