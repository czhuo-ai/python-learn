import sys

if len(sys.argv)<2:
    print("用法:py day20.py 你的名字")
    sys.exit(1)

name=sys.argv[0]
print(f"你好，{name}")