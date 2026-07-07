from collections.abc import Iterable


def send_many_msg(sender, msg, recipients, clear=True, at=None, delay=0):
    if isinstance(recipients, str) or not isinstance(recipients, Iterable):
        raise TypeError("recipients must be an iterable of chat names, not a string")

    result = {"success": [], "failed": {}}

    for recipient in recipients:
        try:
            sender(msg, who=recipient, clear=clear, at=at)
            result["success"].append(recipient)
        except Exception as exc:
            result["failed"][recipient] = str(exc)

        if delay:
            import time

            time.sleep(delay)

    return result
