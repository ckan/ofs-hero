#!/usr/bin/env python
import urllib
import json
from pylons import config

import ckan.model as model
import ckan.plugins.toolkit as toolkit
from ckan.lib.cli import CkanCommand


class Regenerate(CkanCommand):
    """
    Print a JSON dict for persisted_state.json

    Usage:

    paster rengerate
           - Regenerate the persisted_state.json file in case of corruption.
             Generates just enough data for the filestore to work again.
    """
    summary = __doc__.split('\n')[1]
    usage = __doc__
    min_args = 0
    max_args = 1
    MAX_PER_PAGE = 50

    def _get_all_packages(self, context):
        page = 1
        while True:
            data_dict = {
                'page': page,
                'limit': self.MAX_PER_PAGE,
            }
            packages = toolkit.get_action(
                'current_package_list_with_resources')(context, data_dict)
            if not packages:
                raise StopIteration
            for package in packages:
                yield package
            page += 1

    def command(self):
        if self.args and self.args[0] in ['--help', '-h', 'help']:
            print self.__doc__
            return

        self._load_config()
        site_url = config['ckan.site_url']
        user = toolkit.get_action('get_site_user')({'model': model,
                                                    'ignore_auth': True}, {})
        context = {'username': user.get('name'),
                   'user': user.get('name'),
                   'model': model}
        datasets = self._get_all_packages(context)

        storage_path = '/'.join([site_url, 'storage/f/'])
        storage_len = len(storage_path)
        resources = {}
        resource = None

        for dataset in datasets:
            for res in dataset['resources']:
                if res['url'].startswith(storage_path):
                    resource = urllib.unquote(res['url'][storage_len:])
                    resources[resource] = {'key': resource}
        print json.dumps(resources)
