from xmlrpc.server import SimpleXMLRPCServer

class CalcService:

    def add(self, a, b):
        """
        This is add method.
        """
        return a + b

def main():
    server_address = ('localhost', 10000)
    server = SimpleXMLRPCServer(server_address)
    xmlrpc_service = CalcService()
    server.register_instance(xmlrpc_service)
    server.register_introspection_functions()

    print("CTRL-C to stop")
    server.serve_forever()

main()
