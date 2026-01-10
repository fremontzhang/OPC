with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'const MyAgentsView =' in line:
            print(f"Line {i+1}: {line.strip()}")
