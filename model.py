class User:
    def __init__(self,username,connection):
        self.username=username
        self.connection=connection

    async def send_message(self,message):
        await self.connection.send_text(message)