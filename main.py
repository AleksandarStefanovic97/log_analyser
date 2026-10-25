import re


date_pattern = r"(\d{4}-\d{2}-\d{2})"
time_pattern = r"(\d{2}:\d{2}:\d{2})"
level_pattern = r"\d{2}:\d{2}:\d{2} (\w+)"
user_pattern = r"user=(\S+)"
action_pattern = r"action=(\S+)"
ip_pattern = r"ip=(\S+)"

def helper_function(pattern, line):
    match = re.search(pattern,line)
    if match:
        return match.group(1)
    return None

def parse_line(line):
    return{
        "date": helper_function(date_pattern, line),
        "time": helper_function(time_pattern, line),
        "level": helper_function(level_pattern, line),
        "user": helper_function(user_pattern, line),
        "action": helper_function(action_pattern, line),
        "ip": helper_function(ip_pattern, line)
    }

with open('server.log', "r") as file:
    for line in file:
        parsed = parse_line(line)
        print(parsed)

