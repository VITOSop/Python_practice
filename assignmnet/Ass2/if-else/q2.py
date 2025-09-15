tot_cla=int(input("Enetr total classes conducted:"))
att_cla=int(input("Enter attende classes:"))

per=att_cla/tot_cla*100

if(per<85):
    ch=input("Any medical cause:")

    if(ch=='y')|(ch=='Y'):
        print("Allowed to atteded classes.")
        print("Attendence is ",per," %")
    else:
        print("Not allowed to attend exam.")
        print("Attendence is ",per," %")
else:
    print("Allowed to atteded classes.")
    print("Attendence is ",per," %")




