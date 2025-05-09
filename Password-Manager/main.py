from tkinter import *
from tkinter import messagebox
from random import shuffle, choice , randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def find_password():
    key=website_input.get()
    try:
        with open("data.json","r") as f:
                data=json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="no data",message="No data file found")
    else:
        if key in data:
            dict_=data[key]
            email=dict_['Email']
            password=dict_['Password']
            messagebox.showinfo(title=key,message=f"Email: {email}\n"
                                                      f"Password: {password}")
        else:
            messagebox.showerror(title="no data", message=f"No details regarding {key}")



def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters= [choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for i in range(randint(2, 4))]
    password_numbers=[choice(numbers) for j in range(randint(2, 4))]

    password_list= password_letters +password_symbols+password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, 'end')
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    email=email_input.get()
    password =password_input.get()
    new_data={website:{"Email":email , "Password": password}}

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")

    else:

        is_ok=messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail: {email}"
                                                            f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json","r") as f:
                    data=json.load(f)

            except FileNotFoundError:
                with open("data.json","w") as f:
                    json.dump(new_data,f,indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
                    # f.write(f"{website} | {email} | {password}\n")
            finally:
                password_input.delete(0,'end')
                website_input.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

#labels
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)


#entry
website_input=Entry(width=33)
website_input.grid(column=1,row=1)
website_input.focus()

email_input=Entry(width=52)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"example@email.com")

password_input=Entry(width=33)
password_input.grid(column=1,row=3)

#button
gen_pass=Button(text="Generate Password",command=generate_pass)
gen_pass.grid(column=2,row=3)

add_btn=Button(text="Add",width=44,command=save)
add_btn.grid(column=1,row=4,columnspan=2)

search_btn=Button(text="Search",width=15,command=find_password)
search_btn.grid(column=2,row=1)






window.mainloop()