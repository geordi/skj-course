from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    """
    Adds two things.
    """
    return a + b

def main():
    server_address = ('localhost', 10000)
    server = SimpleXMLRPCServer(server_address)
    server.register_function(add)
    server.register_introspection_functions()

    print("CTRL-C to stop")
    server.serve_forever()

main()

