def upd(d, k):
    d[k] = 1
    if k == 'b':
        raise Exception(7)
cfg = {}
for k in ['a', 'b', 'c']:
    try:
        upd(cfg, k)
    except Exception as e:
        print(e)
print(len(cfg))
