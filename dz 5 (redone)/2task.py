request_cnt = int(input())
base_nick = dict()

def check_for_change(base, nick):
    global key
    if bool(base.keys()):
        for key in base.keys():
            if base[key] == nick:
                return True, key
        return False, key
    else:
        return False, nick

for cnt in range(request_cnt):
    request = input().split()
    old_nick = request[0]
    new_nick = request[1]

    if old_nick not in base_nick.keys():
        check_res = check_for_change(base_nick, old_nick)
        if check_res[0]:
            base_nick[check_res[1]] = new_nick

        else:
            base_nick[old_nick] = new_nick
    else:
        base_nick[old_nick] = new_nick

print(len(base_nick.keys()))
for key, value in base_nick.items():
    print(key, value)