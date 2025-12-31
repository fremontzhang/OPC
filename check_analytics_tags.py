import re

def check_balance(content):
    tags = re.findall(r'<(div|table|thead|tbody|tr|td|span|h2|h3|p|button|Icon|a|video|img|DataDetailModal|span)(?:\s+[^>]*)?>|</(div|table|thead|tbody|tr|td|span|h2|h3|p|button|Icon|a|video|img|DataDetailModal|span)>', content)
    
    stack = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        line_num = i + 1
        # Find all tags in this line
        line_tags = re.finditer(r'<(/?)(div|table|thead|tbody|tr|td|span|h2|h3|p|button|Icon|a|video|img|DataDetailModal|span)(?:\s+[^>]*)?>', line)
        for match in line_tags:
            is_closing = match.group(1) == '/'
            tag_name = match.group(2)
            
            # Skip self-closing tags
            if not is_closing and (match.group(0).endswith('/>') or tag_name in ['img', 'video', 'Icon']):
                if tag_name == 'Icon' and not match.group(0).endswith('/>') and '</Icon>' not in line:
                    # Icon can be <Icon ... /> or <Icon>...</Icon>
                    # But if it's <Icon ...>, it might be self-closing if it has no children
                    # Actually, standard Icon component usage here is <Icon ... />
                    pass
                else:
                    continue

            if is_closing:
                if not stack:
                    print(f"Error: Unexpected closing tag </{tag_name}> at line {line_num}")
                    return
                last_tag, last_line = stack.pop()
                if last_tag != tag_name:
                    print(f"Error: Mismatched tag. Expected </{last_tag}> (opened at line {last_line}), but found </{tag_name}> at line {line_num}")
                    # return
            else:
                stack.append((tag_name, line_num))
    
    if stack:
        print("Error: Unclosed tags:")
        for tag, line in stack:
            print(f"  <{tag}> opened at line {line}")
    else:
        print("Success: All tags are balanced!")

with open(r'd:\Antigravity\yc创作者\dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract AnalyticsView content (roughly)
start = content.find('const AnalyticsView = () => {')
end = content.find('const ConnectedCard =', start)
analytics_content = content[start:end]

check_balance(analytics_content)
