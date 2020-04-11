
class Redprint:
    """
    模仿blueprint模块，实现红图管理视图函数，实现blueprint-》redprint-》视图的逐级管理
    """
    def __init__(self, name):
        self.name = name
        self.mound = []
    def route(self, rule, **options):
        def decorator(f):
            #模仿蓝图，但此处无法获取到蓝图对象，将相关参数放置到列表中，到register中进行注册
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            # pop获取到options中endpoint，如果不存在则取视图函数的函数名
            endpoint = options.pop('endpoint', f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
