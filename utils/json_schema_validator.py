import json

from jsonschema import validate, ValidationError

from conf_test import PROJECT_ROOT


def load_schema(file_name):
    with open(f"{PROJECT_ROOT}/test_data/schema/{file_name}", "r") as schema_file:
        return json.load(schema_file)


def validate_json(data, schema_file_name):
    validate(instance=data, schema=load_schema(file_name=schema_file_name))
