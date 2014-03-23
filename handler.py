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
        return get_file

    def render_POST(self, request):
        r = request.content.read()
        j = json.loads(r)
        d = json.dumps(r)
        if str(j['class']) == 'character':
            post_path = str(j['safe_name'])
        elif str(j['class']) == 'terrain':
            post_path = str(j['x'])+"_"+str(j['y'])+".json"
        else:
            post_path = "dummy.log"
            print "WRITING TO DUMMY LOG"
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

