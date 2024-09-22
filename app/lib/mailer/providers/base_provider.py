from abc import ABC

class BaseEmailProvider(ABC):
    def __init__(self,**kwarks) -> None:
        super().__init__(kwarks)
    
    def send_email(to:list[str],cc:list[str],bcc:list[str],subject:str,body:str,attachments=None):
        ...
    
    