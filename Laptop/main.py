import tkinter as tk
import laptopR
import laptopS
import threading
import KeybourdD

root = tk.Tk()
root.title("Simple GUI")
root.geometry("1280x720")
root.configure(bg="#1F1F1F")




threading.Thread(target=laptopR.main).start()
threading.Thread(target=KeybourdD.main).start()
threading.Thread(target=laptopS.main).start()

def Update():
    if laptopR.MessageContent != []:
        angle_x.delete(0, "end")
        angle_y.delete(0, "end")
        Yaw_z.delete(0, "end")
        angle_x.insert(0,laptopR.MessageContent[0])
        angle_y.insert(0,laptopR.MessageContent[1])
        Yaw_z.insert(0,laptopR.MessageContent[2])
    laptopS.message = KeybourdD.message
    root.after(15, Update)



ip = tk.Entry(root,font=100)
ip.insert(0, "192.168.1.171")
ip.config(state="readonly")
ip.place(x=500,y=10)






#message shower
angle_x = tk.Entry(root,font=15,width=5)
angle_x.place(x=500,y=500)
angle_y = tk.Entry(root,font=15,width=5)
angle_y.place(x=560,y=500)
Yaw_z = tk.Entry(root,font=15,width=5)
Yaw_z.place(x=620,y=500)
#message sender



root.after(15, Update)
root.mainloop()