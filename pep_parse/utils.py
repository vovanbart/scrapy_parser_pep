import datetime as dt


def uri_params(params, spider):
    params['time'] = dt.datetime.now().replace(
        microsecond=0).isoformat().replace(':', '-')
