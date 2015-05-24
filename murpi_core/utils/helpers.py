from django.http.request import QueryDict
from MURPI.settings import MEDIA_ROOT
import os


def dict_has_keys(d, keys, check_not_empty=False):
    if type(d) is QueryDict and type(keys) is tuple:
        if all(k in d for k in keys):
            if check_not_empty is False:
                return True
            else:
                if all([True if d[k] and d[k] is not None else False for k in keys]):
                    print [True if not d[k] or d[k] is not None else False for k in keys]
                    return True
                else:
                    return False
        else:
            return False
    else:
        raise TypeError('expected types: d=QueryDict, keys=tuple')


def handle_uploaded_files(f, path_to_file):
    with open(MEDIA_ROOT + '/' + path_to_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def delete_uploaded_file(model, field, file_path):
    args = {field: file_path}
    if not model.objects.filter(**args):
        try:
            os.remove(MEDIA_ROOT + '/' + file_path)
        except IOError:
            print u"Was not able to delete file: {}".format(file_path)


def clean_uploaded_files():
    from murpi_core.models import Player, Universe, World, Place
    models_with_file_fields = [Player, Universe, World, Place]
    for path, subdirs, files in os.walk(MEDIA_ROOT):
        for name in files:
            if not name.startswith('default') and (name.endswith('.jpg') or name.endswith('.png')):
                if not any([model.has_file(os.path.join(path, name).split(MEDIA_ROOT)[-1].strip('/')) for model in models_with_file_fields]):
                    print u"Deleting file {} from directory {}".format(name, path)
                    os.remove(os.path.join(path, name))