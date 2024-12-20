import grpc
from concurrent import futures
import my_service_pb2
import my_service_pb2_grpc

class MyServiceServicer(my_service_pb2_grpc.MyServiceServicer):
    def HelloServer(self, request, context):
        response = my_service_pb2.MyResponse()
        response.message = f"Hello, {request.name}!"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()