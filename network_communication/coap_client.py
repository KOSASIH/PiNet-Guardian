import coapthon.client.helperclient

class CoAPClient:
    def __init__(self, server_ip, server_port):
        self.client = coapthon.client.helperclient.CoAPClient(server=(server_ip, server_port))

    def get_resource(self, resource_path):
        response = self.client.get(resource_path)
        return response.payload

    def post_resource(self, resource_path, payload):
        response = self.client.post(resource_path, payload)
        return response.payload

    def put_resource(self, resource_path, payload):
        response = self.client.put(resource_path, payload)
        return response.payload

    def delete_resource(self, resource_path):
        response = self.client.delete(resource_path)
        return response.payload
