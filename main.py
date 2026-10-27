import re


date_pattern = r"(\d{4}-\d{2}-\d{2})"
time_pattern = r"(\d{2}:\d{2}:\d{2})"
level_pattern = r"\d{2}:\d{2}:\d{2} (\w+)"
user_pattern = r"user=(\S+)"
action_pattern = r"action=(\S+)"
ip_pattern = r"ip=(\S+)"

def scheme_filter(pattern, line):
    match = re.search(pattern,line)
    if match:
        return match.group(1)
    return None

def parse_line(line):
    return{
        "date": scheme_filter(date_pattern, line),
        "time": scheme_filter(time_pattern, line),
        "level": scheme_filter(level_pattern, line),
        "user": scheme_filter(user_pattern, line),
        "action": scheme_filter(action_pattern, line),
        "ip": scheme_filter(ip_pattern, line)
    }

def build_stats(parsed_lines):

    stats = {}

    for parsed in parsed_lines:

        user = parsed["user"]

        if user is None:
            continue

        if user not in stats:
            stats[user] = {"login_count": 0, "err_count": 0, "pay_count": 0, "actions_count": 0}

        stats[user]["actions_count"] += 1

        if parsed["action"] == "login":
            stats[user]["login_count"] += 1

        if parsed["level"] == "ERROR":
            stats[user]["err_count"] += 1

        if parsed["action"] == "payment":
            stats[user]["pay_count"] += 1

    return stats

def most_active(stats):
    return max(stats, key=lambda user: stats[user]["actions_count"])


def find_bad_ips(parsed_lines):
    ip_errors = {}
    bad_ips = []

    for parsed in parsed_lines:

        ip = parsed["ip"]

        if parsed["level"] != "ERROR":
            continue
        if ip is None:
            continue
        if ip not in ip_errors:
            ip_errors[ip] = 0

        ip_errors[ip] += 1

    for ip in ip_errors:
        if ip_errors[ip] > 3:
            bad_ips.append(ip)

    return bad_ips


parsed_lines = []

with open('server.log', "r") as file:
    for line in file:
        parsed_lines.append(parse_line(line))


stats = build_stats(parsed_lines)
print(stats)
print(most_active(stats))
print(find_bad_ips(parsed_lines))
