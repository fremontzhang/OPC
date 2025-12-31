
import re

def check_balance(content):
    # Very simple JSX/HTML tag balancer
    stack = []
    # Match <tag...>, </tag>, or <tag.../>
    # This is a crude regex and might fail on strings, but usually works for finding big issues
    pattern = re.compile(r'<(/?)([a-zA-Z0-9]+)(\s[^>]*)?(/?|)>')
    
    for i, line in enumerate(content.splitlines()):
        for match in pattern.finditer(line):
            is_closing = match.group(1) == '/'
            tag_name = match.group(2)
            is_self_closing = match.group(4) == '/'
            
            if is_self_closing:
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
    check_balance(f.read())
