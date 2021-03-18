import logging
from actstream import action

from src.notifications.channels.email import EmailChannel
from src.notifications.notifications import NOTIFICATIONS

logger = logging.getLogger(__name__)


def _send_email(email_notification_config, context, to):
    email_html_template = email_notification_config.get('email_html_template')
    email_subject = email_notification_config.get('email_subject')

    EmailChannel.send(context=context, html_template=email_html_template, subject=email_subject, to=to)


def notify(verb, **kwargs):
    notification_config = NOTIFICATIONS.get(verb)

    if notification_config and notification_config.get('email'):
        email_notification_config = notification_config.get('email')
        context = kwargs.get('context', {})
        email_to = kwargs.get('email_to', [])

        if not email_to:
            logger.debug('Please provide list of emails (email_to argument).')

        _send_email(email_notification_config, context, email_to)


# Use only with actstream activated
def send_action(sender, verb, action_object, target, **kwargs):
    action.send(sender=sender, verb=verb, action_object=action_object, target=target)
    notify(verb, **kwargs)
