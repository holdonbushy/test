import sys

# 获取命令行参数列表
args = sys.argv

# 打印命令行参数
print("命令行参数:")
print(args[0])

# 处理命令行参数
if len(args) > 1:
    # 获取第一个命令行参数
    arg1 = args[1]
    print("第一个命令行参数:", arg1)

    # 获取后续的命令行参数
    other_args = args[2:]
    print("后续的命令行参数:", other_args)
