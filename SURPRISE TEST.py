from typing import Any, Dict
def flatten_dictionary(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    for key in list(dictionary.keys()):
        value = dictionary[key]
        if type(value) == dict:
            value = flatten_dictionary(value)
            del dictionary[key]
            for nested_dictionary_key in value:
                dictionary[f"{key}.{nested_dictionary_key}"] = value[
                    nested_dictionary_key
                ]
    return dictionary
