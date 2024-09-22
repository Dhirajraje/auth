from .base_provider import BaseEmailProvider

class EmailServiceProvider(BaseEmailProvider):
    def __init__(self, **kwarks) -> None:
        ...
    

    def send_email(to: list[str], cc: list[str], bcc: list[str], subject: str, body: str,attachments=None):
        print('Test send')
    
    