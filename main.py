
import google.generativeai as genai
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

gemini_api_key = "AIzaSyBYaZjmPH_PlD-uFHv2oLLFhLVETXhMX58"
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel('gemini-pro')
from customtkinter import *
app =CTk()
app.geometry("1400x800")

yd =0.13
response="k"
st=""
string_variable=StringVar()



def textbtn():
    t_entry=CTkEntry(master=app,placeholder_text="input skill or subject",width=280,height=28)
    t_entry.place(relx=0.56,rely=0.5)
    def submit():
        topic=t_entry.get()
        t_entry.configure(state="disabled")   
        t_entry.destroy()
        sub_bt.destroy()

        def show5bts():
                
            def func1():
                label.delete("0.0","end")
                prompt1="I want to learn about "+topic+" Identify and share the most important 20 percent of learnings from this topic that will help me understand 80 percent of it"
                response=model.generate_content(prompt1)
                st=response.text
                string_variable.set(str(st))
                label.insert("0.0",str(st))
                print(st)
                print(response.text)
            def func2():
                label.delete("0.0","end")
                prompt2="I want to learn/get better at "+topic+" .I am a complete beginner.Create a 30 day learning plan that will help a beginner like me learn and improve this skill"
                response=model.generate_content(prompt2)
                st=response.text
                string_variable.set(str(st))
                label.insert("0.0",str(st))
                print(st)
                print(response.text)
            def func3():
                label.delete("0.0","end")
                prompt3="Your role is that of a problem solver.Give me a step-by-step guide to solving "+topic
                response=model.generate_content(prompt3)
                st=response.text
                string_variable.set(str(st))
                label.insert("0.0",str(st))
                print(st)
                print(response.text)
            def func4():
                label.delete("0.0","end")
                prompt4="I am currently learning about "+topic+" .Convert the key lessons from this topic into engaging stories and metaphors to aid my memorization."
                response=model.generate_content(prompt4)
                st=response.text
                string_variable.set(str(st))
                label.insert("0.0",str(st))
                print(st)
                print(response.text)
            def func5():
                label.delete("0.0","end")
                prompt5="I am currently learning about "+topic+" .Ask me a series of questions that will test my knowledge . Identify knowledge gaps in my answers and give me better answers to fill those gaps."
                response=model.generate_content(prompt5)
                st=response.text
                string_variable.set(str(st))
                label.insert("0.0",str(st))
                print(st)
                print(response.text)
            btn1=CTkButton(master=app,text="80/20 principle",command=func1,fg_color="green",hover_color="dark green")
            btn1.place(relx=0.02,rely=0.3)
            btn2=CTkButton(master=app,text="30 days learning plan",command=func2,fg_color="green",hover_color="dark green")
            btn2.place(relx=0.02,rely=0.4)
            btn3=CTkButton(master=app,text="problem solving skills",command=func3,fg_color="green",hover_color="dark green")
            btn3.place(relx=0.02,rely=0.5)
            btn4=CTkButton(master=app,text="Enhance memory",command=func4,fg_color="green",hover_color="dark green")
            btn4.place(relx=0.02,rely=0.6)
            btn5=CTkButton(master=app,text="Self Assessment",command=func5,fg_color="green",hover_color="dark green")
            btn5.place(relx=0.02,rely=0.7)
        skill_btn=CTkButton(master=app,text=topic,command=show5bts,height=40,fg_color="green",hover_color="dark green")
        skill_btn.place(relx=0.02,rely=0.2)
        
    
        
    sub_bt=CTkButton(master=app,text="submit",command=submit)
    sub_bt.place(relx=0.56,rely=0.55)




def addskill():
    textbtn()


label=CTkTextbox(master=app,width=1080,height=700)
label.place(relx=0.22,rely=0.1)    

s_button=CTkButton(master=app,text="SEARCH SKILL",command=addskill,width=200,height=40,fg_color="green",hover_color="dark green")

s_button.place(relx=0.02,rely=0.1,anchor="nw")

lab=CTkLabel(master=app,bg_color="dark green",text="MINT",width=2500,height=70,anchor="nw",text_color="white",font=('Times',56))
lab.place(relx=0,rely=0)


app.mainloop()



