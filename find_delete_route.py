with open('server.py', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if "@app.route('/api/posts/<post_id>'" in line:
            print(f"Line {i+1}: {line.strip()}")
