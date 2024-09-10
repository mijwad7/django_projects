class CustomMiddleware():
    def __init__(self, get_response) -> None:
        self.get_response  = get_response

    def call(self, request):
        print("call")
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        print("process_exception")
        return exception