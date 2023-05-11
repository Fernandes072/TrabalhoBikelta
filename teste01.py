a = ["aaa", "bbb"]
try:
    a.index("ccc")
except ValueError:
    print("DDD")