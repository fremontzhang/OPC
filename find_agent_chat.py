with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'const AgentChatView =' in line:
            print(f"Line {i+1}: {line.strip()}")
