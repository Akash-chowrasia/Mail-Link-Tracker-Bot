from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import sys
import webbrowser

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("found")
        webbrowser.open("http://www.onlinethedimension.com")
        sys.exit()

def main():
    PORT = 9000
    server_address = ('localhost',PORT)
    server = HTTPServer(server_address, requestHandler)
    print('server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()

