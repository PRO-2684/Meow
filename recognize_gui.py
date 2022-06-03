#展示
from cProfile import label
from genericpath import exists
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from recognize import recognize
import os

window = tk.Tk()
window.title('Welcome to USTC CAT')
window.geometry('420x320')

#导入背景图片 用canvas
canvas0 = tk.Canvas(window, height=300,width=500)
image_file = tk.PhotoImage(file='xiaohei.gif')
image = canvas0.create_image(0,0,anchor='nw',image=image_file)
canvas0.pack(side='top')

#获取文件路径
def get_filename():
    default_dir = r"文件路径"
    filePath = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)), filetypes=[('JPG', '.jpg')])
    # print(filePath)
    entry_usr_cat.delete(0, "end")
    entry_usr_cat.insert(0, filePath)

#基本信息
btn_select = tk.Button(window, text='选择文件', command=get_filename)
btn_select.place(x=320, y=105)
tk.Label(window, text='请输入要检测的图片').place(x=80, y=70)
tk.Label(window, text='文件名:').place(x=80, y=110)

#输入部分
var_usr_cat = tk.StringVar()
var_usr_cat.set('如：example.jpg')
entry_usr_cat = tk.Entry(window, textvariable=var_usr_cat)
entry_usr_cat.place(x=160, y=110)
infos = {
    'a': ("./ustc/a/00.jpg", "<名字 a>", "<活动区域 a>", "<喜好 a>", "<故事 a>"),
    'b': ("./ustc/b/00.jpg", "<名字 b>", "<活动区域 b>", "<喜好 b>", "<故事 b>"),
    'c': ("./ustc/c/00.jpg", "<名字 c>", "<活动区域 c>", "<喜好 c>", "<故事 c>"),
    'd': ("./ustc/d/00.jpg", "<名字 d>", "<活动区域 d>", "<喜好 d>", "<故事 d>"),
    'e': ("./ustc/e/00.jpg", "<名字 e>", "<活动区域 e>", "<喜好 e>", "<故事 e>"),
    'f': ("./ustc/f/00.jpg", "<名字 f>", "<活动区域 f>", "<喜好 f>", "<故事 f>"),
}

def cat_check():
    #获取信息并显示新的窗口
    file_name = var_usr_cat.get()
    r = recognize([file_name])

    #检验文件，在此处留出位置使用识别模型
    cat_name = r[0][0]

    #根据检验结果输出
    if cat_name not in infos:
        return
    info = infos[cat_name]
    window_result = tk.Toplevel()
    window_result.title('Welcome to USTC CAT')
    window_result.geometry('800x500')
    canvas = tk.Canvas(window_result,width=800,height=500,bg='white')

    #图片
    img1 = Image.open(info[0])  #打开图片
    photo1 = ImageTk.PhotoImage(img1) #用PIL模块打开
    imglabel_1 = tk.Label(window_result, image= photo1)
    imglabel_1.place(x=0,y=0)
    #详细信息
    label_name = tk.Label(window_result, text='名字：' + info[1])
    label_name.place(x=430, y=60)
    label_area = tk.Label(window_result, text='活动区域：' + info[2])
    label_area.place(x=430, y=130)
    label_like = tk.Label(window_result, text='喜好：' + info[3])
    label_like.place(x=430, y=200)
    label_like = tk.Label(window_result, text='TA与科大的故事：' + info[4])
    label_like.place(x=430, y=280)
    #最后显示
    canvas.pack()
    window_result.mainloop()


    # else:
    #     choice = tk.messagebox.askyesno('Sorry', '我们还不认识这只猫哦.也许您可以向我们提供TA的相关信息.')
    #     if choice:
    #         write()

def write():
    #定义一个函数，后面会用到
    def confirm():
        pass #因为暂时没有存储信息的数据库，所以先用pass占位
        #获取值
        photo = var_photo.get()
        area = var_area.get()
        name = var_name.get()
        #无输入时的反馈
        if photo == '' or area == '' or name == '':
            tk.messagebox.showerror('Error', '抱歉，输入不能为空。')
        else:
            #提交成功显示反馈
            tk.messagebox.showinfo('Thank you!', '感谢您对我们的支持，您提供的信息将会为我们提供巨大的帮助。')
            #关闭窗口:destroy
            window_write.destroy()

    window_write = tk.Toplevel(window)
    window_write.geometry('400x300')
    window_write.title('提交信息')
    #上传图片信息和其它信息
    label_photo = tk.Label(window_write, text='请输入您要上传的图片信息：')
    label_photo.place(x=50, y=50)
    label_name_write = tk.Label(window_write, text='您可以为它取一个名字：')
    label_name_write.place(x=50, y=90)
    label_area_write = tk.Label(window_write, text='您在哪里发现了TA:')
    label_area_write.place(x=50, y=130)
    #输入部分
    var_photo = tk.StringVar()
    var_photo.set('如：example.jpg')
    entry_photo = tk.Entry(window_write, textvariable=var_photo)
    entry_photo.place(x=220, y=50)
    var_name = tk.StringVar()
    var_name.set('如：xxx')
    entry_name = tk.Entry(window_write, textvariable=var_name)
    entry_name.place(x=220, y=90)
    var_area = tk.StringVar()
    var_area.set('如：xxx')
    entry_area = tk.Entry(window_write, textvariable=var_area)
    entry_area.place(x=220, y=130)
    #按钮
    btn_confirm = tk.Button(window_write, text='确认提交', command=confirm)
    btn_confirm.place(x=160, y=200)


#开始检测按钮
btn_login = tk.Button(window, text='开始检测', command=cat_check)
btn_login.place(x=130, y=160)

window.mainloop()