import os
import sys

# 将根目录添加到 sys.path 以便导入 server.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app as application

# 对 Vercel 环境进行特殊处理
# 因为 Vercel 是只读环境，除了 /tmp 目录
# 我们需要确保数据库路径在 /tmp 中
import sqlite3
import shutil

# 获取原始数据库路径
original_db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'platform.db')
target_db = '/tmp/platform.db'

# 如果 /tmp 中没有数据库，尝试从项目根目录复制一个过去
if not os.path.exists(target_db) and os.path.exists(original_db):
    try:
        shutil.copy2(original_db, target_db)
        print(f"Database copied to {target_db}")
    except Exception as e:
        print(f"Error copying database: {e}")

# 通知应用使用临时路径
os.environ['DATABASE_PATH'] = target_db

# 暴露接口给 Vercel
app = application
