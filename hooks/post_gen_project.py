#!/usr/bin/env python
import os
import shutil
import yaml

MANIFEST = 'manifest.yml'


def delete_resources_for_disabled_features():
    """ Deleting unnecessary files after 
        cookiecutter files generation """
    with open(MANIFEST) as manifest_file:
        manifest = yaml.load(manifest_file, Loader=yaml.FullLoader)
        for feature in  manifest['features']:
            if feature.get('enabled'):
                if feature['enabled'] == "n":
                    for resource in feature['resources']:
                        delete_resource(resource)
            elif feature.get('technology'):
                if feature['technology'] == "BasicHTML":
                    for resource in feature['resources']:
                        delete_resource(resource)
    print("[+] Cleanup completed, removing manifest")
    delete_resource(MANIFEST)


def delete_resource(resource):
    """ helper function: removing file
        or directories for delete 
        resources for disabled features 
    """
    if os.path.isfile(resource):
        print(f"[*] Removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"[*] Removing directory: {resource}")
        shutil.rmtree(resource)


if __name__ == '__main__':
    delete_resources_for_disabled_features()
