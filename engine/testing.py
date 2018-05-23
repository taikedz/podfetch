import importlib

def testModule(args):
    module = args[0]
    weburl = args[1]
    method = args[2]

    imported = importlib.import_module(module)

    podule = imported.get_resource(weburl)

    themethod = getattr(podule, method)

    print( str( themethod(*args[3:]) ) )
