with open('dashboard.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'const handlePublish =' in line:
            print(f"Match found at line {i+1}: {line.strip()}")
