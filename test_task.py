info_groups = {}
info_groups2 = {}

def num_grp_z(n_customers):
    for i in range(n_customers):
        num = sum(map(int,str(i)))
        if num in info_groups:
            info_groups[num] += 1
        else:
            info_groups[num] = 1

def num_grp_any(n_customers, n_first_id):
    for i in range(n_first_id, n_first_id + n_customers + 1):
        num = sum(map(int,str(i)))
        if num in info_groups2:
            info_groups2[num] += 1
        else:
            info_groups2[num] = 1

info_groups2 = {key:info_groups2[key] for key in sorted(info_groups2)}       