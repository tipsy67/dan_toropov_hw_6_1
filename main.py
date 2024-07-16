from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080
path_to_html = Path(__file__).parent.joinpath('html', 'index.html')

class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        with open(path_to_html) as f:
            html_file = f.read()
        return html_file.encode()

    def do_GET(self):
        # query_components = parse_qs(urlparse(self.path).query)
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(page_content)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

