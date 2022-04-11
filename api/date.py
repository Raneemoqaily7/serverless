from email import message
from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform
from os.path import join

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s=self.path
        url_components =parse.urlsplit(s)
        query_string_list =parse.parse_qsl(url_components.query)
        dic =dict(query_string_list)
        name = dic.get("name")
        if name :
          message = f"Hello {name}"
        else :
          message = "Hello"

        message += f"\ngreeting for all{platform.python_version()}"
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        with open(join('data', 'file.txt'), 'r') as file:
          for line in file:
            self.wfile.write(line.encode())
        self.wfile.write(message.encode())
        return

