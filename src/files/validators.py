from django.core.exceptions import ValidationError

MAX_FILESIZE = 10100000  # 10MB


def validate_file_size(value):
    filesize = value.size
    if filesize > MAX_FILESIZE:
        raise ValidationError('The maximum file size that can be uploaded is 10MB')
    else:
        return value
