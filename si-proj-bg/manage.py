"""
-*- coding: utf-8 -*-
@Time    : 2020-07-15 11:06
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : manage.py
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from models import db

app = create_app()
manager = Manager(app)

# 创建db管理工具=》app， db
# migrate = Migrate(app, db)
# manager.add_command('db', Migrate)
# sqlite数据库不支持列删除，需要一个判断
with app.app_context():
    migrate = Migrate()
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_ad_batch=True)
    else:
        migrate.init_app(app, db)
manager.add_command('db', MigrateCommand)
if __name__ == "__main__":
    manager.run()

