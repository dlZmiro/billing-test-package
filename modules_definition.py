import dtlpy as dl
import json
from create_service import package_name


def generate_package_json():
    package = {
        "name": package_name,
        "modules": [module.to_json() for module in get_modules()]
    }

    with open('package.json', 'w', encoding='utf-8') as f:
        json.dump(package, f, indent=4)


def get_modules():
    modules = dl.PackageModule(
        class_name='Runner',
        name=package_name,
        entry_point='download_dataset.py',
        functions=[
            dl.PackageFunction(name='change_item_metadata',
                               inputs=[dl.FunctionIO(type=dl.PACKAGE_INPUT_TYPE_ITEM, name='item')]
                               )
        ]
    )
    return [modules]
