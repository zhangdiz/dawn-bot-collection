# 定义文件路径
file_path = './proxies.txt'

# 读取文件内容
with open(file_path, 'r') as file:
    ip_list = file.readlines()

# 去除每行末尾的换行符并添加 http://
updated_ip_list = ['http://' + ip.strip() + '\n' for ip in ip_list]

# 将修改后的内容写回文件
with open(file_path, 'w') as file:
    file.writelines(updated_ip_list)

print("IP列表已更新并写入文件。")