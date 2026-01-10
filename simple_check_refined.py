
import re

def check_balance(content):
    stack = []
    # Match tags, but be careful with self-closing and attributes containing >
    # This regex is a bit better
    tag_pattern = re.compile(r'<(/?)([a-zA-Z0-9:]+)(\s+(?:[^>"\']|"[^"]*"|\'[^\']*\')*)?(/?|)>')
    
    for i, line in enumerate(content.splitlines()):
        for match in tag_pattern.finditer(line):
            is_closing = match.group(1) == '/'
            tag_name = match.group(2)
            is_self_closing = match.group(4) == '/' or tag_name in ['img', 'br', 'hr', 'input', 'meta', 'link']
            
            if is_self_closing and not is_closing:
                continue
            
            if is_closing:
                if not stack:
                    print(f"Extra closing tag </{tag_name}> at line {i+1}")
                else:
                    last_tag, last_line = stack.pop()
                    if last_tag != tag_name:
                        print(f"Mismatched tag: </{tag_name}> at line {i+1} does not match <{last_tag}> from line {last_line}")
            else:
                stack.append((tag_name, i+1))
                
    for tag_name, line in stack:
        print(f"Unclosed tag <{tag_name}> from line {line}")

with open(r"d:\Antigravity\yc创作者\dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()
    # Extract AnalyticsView
    start_marker = "const AnalyticsView = () => {"
    end_marker = "const ConnectedCard ="
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    if start_idx != -1 and end_idx != -1:
        line_num = content.count('\n', 0, start_idx) + 1
        print(f"Checking AnalyticsView from line {line_num}")
        sub = content[start_idx:end_idx]
        check_balance(sub)
    else:
        print("Markers not found")
