namer_last_id = 0

def gen_id():
    global namer_last_id
    namer_last_id += 1
    return namer_last_id
