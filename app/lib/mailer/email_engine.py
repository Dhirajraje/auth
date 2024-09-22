# from .providers.email_service_provider import EmailServiceProvider


class EmailEngine:
    _email_provider = None

    def __init__(self) -> None:
        # TODO: Decide the required service provider from environement variable
        ...

    def _send_email(
        to: list[str],
        cc: list[str],
        bcc: list[str],
        subject: str,
        body: str,
        attachments=None,
    ): ...

    def _perform_template_checks(
        template_name: str, special_var_dict: dict[str, any], raise_errors: bool = False
    ):
        # TODO: Get template details from template name
        _required_special_variable = []

        # TODO: check if the provided special variables are in complient with the reqired template

        if all(
            special_var in special_var_dict
            for special_var in _required_special_variable
        ):
            # TODO: send the email
            ...
        else:
            _error_message = f'The template requires few more special variables i.e. ({','.join([special_var in special_var_dict for special_var in _required_special_variable])})'
            if raise_errors:
                raise KeyError(_error_message)

            else:
                # TODO: Log worning for missing variables
                print(_error_message)
