from dotenv import load_dotenv
import os

load_dotenv()

class Settings():
    host: str = os.getenv("HOST")
    port:int = os.getenv("PORT")
    password : str = os.getenv("PASSWORD")

    def __post__init(self):
        if not self.host:
            raise ValueError("The Host Id is not Set")
        if not self.password:
            raise ValueError("The Password is not Set")


credentials = Settings()