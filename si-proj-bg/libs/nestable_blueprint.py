"""
-*- coding: utf-8 -*-
@Time    : 2020-07-18 17:11
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : nestable_blueprint.py
"""

from flask import Blueprint


class NestableBlueprint(Blueprint):
    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            # state.url_prefix => 自己url前缀 + blueprint.url_prefix => /v3/api/cmdb/
            url_prefix = (state.url_prefix or u"") + (options.get('url_prefix', blueprint.url_prefix) or u"")
            if 'url_prefix' in options:
                del options['url_prefix']
            # app.register_blueprint(blueprint, '/v3/api/cmdb/')
            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)
        self.record(deferred)
