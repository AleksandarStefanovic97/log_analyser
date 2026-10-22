import re



with open('server.log', "r") as file:
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    time_pattern = r"\d{2}:\d{2}:\d{2}"
    level_pattern = r"\d{2}:\d{2}:\d{2} (\w+)"
    user_pattern = r"user=(\S+)"
    action_pattern = r"action=(\S+)"
    ip_pattern = r"ip=(\S+)"

    for event in file.readlines():
        date = re.findall(date_pattern, event)
        time = re.findall(time_pattern, event)
        level = re.findall(level_pattern, event)
        user = re.findall(user_pattern, event)
        action = re.findall(action_pattern, event)
        ip = re.findall(ip_pattern, event)

        print(date, time, level, user, action, ip) #prikazuje stats, treba ih obraditi