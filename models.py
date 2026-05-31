from pydantic import BaseModel

class PostAnalysis(BaseModel):
    category:str
    summary:str
    toxic:bool