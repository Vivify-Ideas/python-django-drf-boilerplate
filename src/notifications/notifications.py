ACTIVITY_USER_CREATED = 'new user registered'
ACTIVITY_USER_RESETS_PASS = 'started password reset process'

NOTIFICATIONS = {
    ACTIVITY_USER_CREATED: {
        'email': {
            'email_subject': 'Email Confirmation',
            'email_html_template': 'emails/verify_account.html',
        }
    },
    ACTIVITY_USER_RESETS_PASS: {
        'email': {
            'email_subject': 'Password Reset',
            'email_html_template': 'emails/user_reset_password.html',
        }
    }
}
