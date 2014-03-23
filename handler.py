from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import cgi

class FormPage(Resource):
    def render_GET(self, request):
        get_path = str(request.content.read())
        path = str('./'+get_path)
        with open(path, 'rb') as fd:
            get_file = fd.read()
            print get_file
        return get_file

    def render_POST(self, request):
        post_json = request.content.read()
        
        return post_json

root = Resource()
root.putChild("post", FormPage())
factory = Site(root)
reactor.listenTCP(8080, factory)
reactor.run()

