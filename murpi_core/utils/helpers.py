from django.http.request import QueryDict


def dict_has_keys(d, keys, check_not_empty=False):
    if type(d) is QueryDict and type(keys) is tuple:
        if all(k in d for k in keys):
            if check_not_empty is False:
                return True
            else:
                if all([True for k in keys if d[k] != '' or d[k] is not None]):
                    return True
                else:
                    return False
        else:
            return False
    else:
        raise TypeError('expected types: d=QueryDict, keys=tuple')