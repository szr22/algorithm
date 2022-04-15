def simplifyPath(path: str) -> str:
    path_components = path.split('/')
    res_components = []
    print(path_components)
    for component in path_components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if res_components:
                res_components.pop()
            else:
                continue
        else:
            res_components.append(component)
    print(res_components)
    return '/'+'/'.join(res_components)

path = "/../"
res = simplifyPath(path)
print(res)