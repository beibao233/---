import uuid
import tkinter
import tkinter.filedialog as tk_file
import tkinter.messagebox as tm

root = tkinter.Tk()
root.withdraw()

print('进程提示：正在选择输入文件')
file = tk_file.askopenfilenames(title='请选择需要进行还原的被分割文件(请框选分割后的所有文件(多个))', filetypes=[("分割后的一堆二进制文件", "*.bin*")])
print('进程提示：正在选择输出路径')
dir = tk_file.askdirectory(title='请选择输出路径')

tm.showinfo('注意','请关闭此对话框后查看输出区并在其中输入文件后缀名(注意后缀名需带有".")')
suffix = input('请输入还原的文件后缀:')

f2 = open(dir + '/' + str(uuid.uuid1()) + suffix, 'wb')

print('不温馨的提示：还原可能需要亿点时间,请耐心等待')
for file_info in file:
    print("正在合成" + file_info + "到" + dir)
    # 读取
    f1 = open(file_info, 'rb')
    info = f1.read()
    f1.close()
    # 把读取到的东西写入f2
    f2.write(info)
f2.close()
print('进程提示：还原成功')
tm.showinfo('提示', '还原成功')
