#!/usr/bin/env python
import ckanapi
import urllib
import json

def main():
    site_url = 'http://localhost:5000'
    storage_path = '/'.join([site_url, 'storage/f/'])
    storage_len = len(storage_path)
    ckan = ckanapi.RemoteCKAN(site_url, user_agent='ckanapi/1.0 '
            '(json-recreate)')
    datasets = ckan.action.current_package_list_with_resources()
    resources = {}
    resource = None
    for dataset in datasets:
        for res in dataset['resources']:
            if res['url'].startswith(storage_path):
                resource = urllib.unquote(res['url'][storage_len:])
                resources[resource] = {'key': resource}
    print json.dumps(resources)



if __name__ == '__main__':
    main()
