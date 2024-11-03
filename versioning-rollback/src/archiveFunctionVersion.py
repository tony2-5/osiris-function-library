from restoreArchivedVersion import functions

def archiveFunctionVersion(function_name: str, version: str) -> bool:
    if function_name not in functions:
        functions[function_name] = {}
    if version not in functions[function_name]:
        return False
    if functions[function_name][version] == 'archived':
        return False
    functions[function_name][version] = 'archived'
    return True
