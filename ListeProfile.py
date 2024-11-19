import Class_interface
app = Class_interface.App()
app.geometry('1240x900')


scrollframe=Class_interface.ctk.CTkScrollableFrame(app,width=1000,height=750)
scrollframe.pack(pady=20,padx=10,fill='both')
for i in range(1,30):
    itemframe=Class_interface.ctk.CTkFrame(scrollframe,fg_color='blue',width=800)
    itemframe.pack(pady=7,padx=5,fill='both')

app.mainloop()

