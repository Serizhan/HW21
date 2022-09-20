class Request:
    def __init__(self, request: str):
        pre_request = request.lower().split(' ')
        self.from_ = pre_request[4]
        self.to = pre_request[6]
        self.amount = int(pre_request[1])
        self.product = pre_request[2]