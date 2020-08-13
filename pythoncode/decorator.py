from functools import wraps

def timer(name):
    def decorator(func):
        @wraps(func)
        def wraper(*args,**kwargs):
            print(*args)
            return func(*args,**kwargs)
        return wraper
    return decorator

if __name__ == '__main__':
    @timer('do')
    def dosomething(aaa):
        return 1
    dosomething(1)