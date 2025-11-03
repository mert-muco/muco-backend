from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class UploadByField():
    def __init__(self, field):
        self.field = field
    def __call__(self, instance, file):
        ext = file.rsplit('.', 1)[-1]
        brief = getattr(instance, self.field)
        brief = slugify(brief)
        return f'{brief}.{ext}'
        
@deconstructible
class UploadByFieldCount():
    def __init__(self, f_key):
        self.f_key = f_key
    def __call__(self, instance, file):
        ext = file.rsplit('.', 1)[-1]
        brief = getattr(instance, self.f_key)
        safe_name = slugify(brief.title)
        count = brief.images.count() + 1
        return f'{safe_name}-{count}.{ext}'