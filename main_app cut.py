import tkinter.filedialog as tk_file
import tkinter.messagebox as tm
import tkinter

root = tkinter.Tk()
root.withdraw()

print('进程提示：正在选择输入文件')
file = tk_file.askopenfilename(title='请选择需要进行分割的文件', filetypes=[("所有文件", "*.*")])
print('进程提示：正在选择输出路径')
dir = tk_file.askdirectory(title='请选择输出路径')

f1 = open(file, 'rb')
num = 0

print('不温馨的提示：分割可能需要亿点时间,请耐心等待')
while True:
    # 读取
    info = f1.read(1073741824)# 这里的参数是分割文件后单个文件的大小(单位:字节[不是千字节KB,是字节B!!!]),千万不能大于运行内存
    if len(info) == 0:
        # 如果为零说明已读完,此时可以退出循环
        break
    else:
        # 如果不等于零把读取到的东西写入f2
        print("正在分割 " + file + "到" + dir + '/' + str(num) + '.bin')
        f2 = open(dir + '/' + str(num) + '.bin', 'wb')
        f2.write(info)
        f2.close()
    num = num + 1
f1.close()
print('分割完成')
tm.showinfo('提示', '分割完成')
