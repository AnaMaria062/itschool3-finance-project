def singleton(cls):
    instances = {}
    print('after declaration')
    print(instances)
    print(cls)

    def wrapper(*args, **kwargs):  # when you want dynamic variables
        if cls not in instances:
            print(*args, **kwargs)
            instances[cls] = cls(*args, **kwargs)
        print('before return')
        print(instances)
        return instances[cls]

    return wrapper
