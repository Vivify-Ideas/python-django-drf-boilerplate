from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):

    def connect(self):
        # To accept the connection call:
        self.accept()
        # to access user provided by middleware = self.scope['user']
        # To reject the connection, call:
        # self.close()

    # Called with either text_data or bytes_data for each frame
    def receive(self, text_data=None, bytes_data=None):
        # You can call:
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        # self.close()
        # Or add a custom WebSocket error code!
        # self.close(code=4123)

    # Called when the socket closes
    # def disconnect(self, close_code):
        # print(close_code)
