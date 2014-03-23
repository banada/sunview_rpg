from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import cgi
import json

class FormPage(Resource):
    def render_GET(self, request):
        get_path = str(request.content.read())
        path = str('./'+get_path)
        with open(path, 'rb') as fd:
            get_file = fd.read()
            fd.close()
            print get_file
        return get_file

    def render_POST(self, request):
        r = request.content.read()
        print r
        j = json.loads(r)
        print j
        d = json.dumps(r)
        print d
        post_path = str(j['safe_name'])
        path = str('./JSON/'+post_path)
        with open(path, 'w') as fd:
            fd.write(r)
            fd.close()
        return path

root = Resource()
root.putChild("post", FormPage())
factory = Site(root)
reactor.listenTCP(8080, factory)
reactor.run()

