'''  this program also needs en_core_web_lg (spacy model)
    copy 'python -m spacy download en_core_web_lg' and run in terminal to download '''
from tkinter import filedialog
import customtkinter as ctk
import spacy
from spacy.matcher import Matcher
from spacy.tokens import span
import sys, fitz


#window
window = ctk.CTk()
window.title('Resume Parser')
window.geometry(f'{860}x{590}')

window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure((2, 3), weight=0)
window.grid_rowconfigure((0, 1, 2), weight=1)

#window frame

frameb = ctk.CTkFrame(
    window,
    width=50,
    height=40,
    fg_color='transparent'
)
frameb.grid(row = 0,
            column=1,
            sticky="nsew",
)
frameb.grid_rowconfigure(4, weight=1)

#frame for label
framel = ctk.CTkFrame(
    window,
    width= 950,
    height= 70,
    fg_color='transparent',
    )
framel.grid(row=0,column=0,rowspan= 4,sticky= "nsew")

#label
label = ctk.CTkLabel(
    framel,
    text ='Welcome To Resume Parser',
    fg_color= ('lightblue', 'lightyellow'),
    corner_radius= 15,
    text_color= ('black'),
    width=40, 
    height= 50,
    font= ('brush script mt', 40)
    )
label.pack(pady = 10)


frame_s = ctk.CTkFrame(
    window,
    height = 40,
    width = 50,
    fg_color= 'transparent',
)
frame_s.grid(
    column = 1,
    row = 1,
    )
frame_s.grid_rowconfigure(2, weight= 1,)
label_s = ctk.CTkLabel(
    frame_s,
    text ='Rating Of this resume for common skills is : ',
    fg_color= ('lightyellow', 'lightblue'),
    corner_radius= 15,
    text_color= ('black'),
    width= 50,
    height= 40,
    font= ('high tower text',21 )
    )
label_s.grid(row=0,column=1,padx = 5)

progressbar = ctk.CTkSlider(frame_s, orientation="vertical",from_=0, to= 10, number_of_steps= 10, state = "disabled",width=15,progress_color="#FF9966",border_width=2,border_color="white",fg_color="grey",)
progressbar.grid(row=1, column=1, rowspan=2, padx=(10, 20), pady=(10, 10), sticky="ns", )

progressbar.set(0)


nlp = spacy.load('en_core_web_lg')
insights = spacy.load('./model-best')
def main() :
    file =  filedialog.askopenfilename(
    filetypes= (('PDF(.pdf)','*.pdf'),
    ('All files','*.*')),
    title= 'Locate The Resume',)

    
    
    pattern_s = [
        {"LOWER":"python",'OP':'?'},{"LOWER":"css",'OP':'?'},{"LOWER":"html",'OP':'?'},{"LOWER" :"java",'OP':'?'},{"LOWER" :"c#",'OP':'?'}, {"LOWER" :"javascript",'OP':'?'},{"LOWER" : "sql",'OP':'?'},{"LOWER" : "c++",'OP':'?'},{"LOWER" : "r",'OP':'?'},{"LOWER" : "matlab",'OP':'?'},{"LOWER" : "excel",'OP':'?'},{"LOWER" : "tableau",'OP':'?'},{"LOWER" : "hadoop",'OP':'?'},{"LOWER" : "spark",'OP':'?'},{"LOWER" :"big data",'OP':'?'},{"LOWER" : "data science",'OP':'?'},{"LOWER" : "machine learning",'OP':'?'},{"LOWER" : "ai",'OP':'?'},{"LOWER" : "deep learning",'OP':'?'},{"LOWER" :"tensorflow",'OP':'?'},{"LOWER" :"keras",'OP':'?'},{"LOWER" :"pytorch",'OP':'?'},{"LOWER" :"pandas",'OP':'?'},{"LOWER" :"numpy",'OP':'?'},{"LOWER" : "opencv",'OP':'?'},{"LOWER" : "dlib",'OP':'?'},{"LOWER" :"sklearn",'OP':'?'},{"LOWER" : "nltk",'OP':'?'},{"LOWER":"spacy",'OP':'?'},{"LOWER":"scipy",'OP':'?'},{"LOWER":"xgboost",'OP':'?'},{"LOWER":"lightgbm",'OP':'?'},{"LOWER":"torch",'OP':'?'}, {"LOWER":"vision",'OP':'?'},{"LOWER":"nlp",'OP':'?'},{"LOWER":"cv",'OP':'?'}, {"LOWER":"resume parser",'OP':'?'}, {"LOWER":"word embedding",'OP':'?'},{"LOWER":"bert",'OP':'?'},{"LOWER": "transformer",'OP':'?'}, {"LOWER":"pre-trained model",'OP':'?'},{"LOWER":"reinforcement learning",'OP':'?'},{"LOWER":"image recognition",'OP':'?'},{"LOWER":"text recognition",'OP':'?'},{"LOWER":"nlp tasks",'OP':'?'},{"LOWER": "bertology",'OP':'?'}, {"LOWER":"universal dependency",'OP':'?'},{"LOWER":"gpt",'OP':'?'},{"LOWER":"bert-for-next sentence prediction",'OP':'?'},{"LOWER":"masked language modeling",'OP':'?'},{"LOWER":"multitask learning",'OP':'?'},{"LOWER":"pretraining tasks",'OP':'?'},{"LOWER":"language modeling",'OP':'?'},{"LOWER":"bert pretraining",'OP':'?'},{"LOWER":"multilingual",'OP':'?'},{"LOWER":"bart",'OP':'?'},{"LOWER":"gpt-2",'OP':'?'},{"LOWER":"gpt-3",'OP':'?'},{"LOWER":"xlnet",'OP':'?'},{"LOWER":"roberta",'OP':'?'},{"LOWER":"distilbert",'OP':'?'},{"LOWER":"t5",'OP':'?'},{"LOWER":"albert",'OP':'?'},{"LOWER":"camembert",'OP':'?'},{"LOWER":"flaubert",'OP':'?'},{"LOWER":"xla",'OP':'?'},{"LOWER":"xlm",'OP':'?'},{"LOWER":"m",'OP':'?'},{"LOWER":"xla-lxmt5-l33t",'OP':'?'},{"LOWER":'knowledge of machine learning algorithms','OP':'?'},{"LOWER":'strong programming skills','OP':'?'},{"LOWER":'ability to analyze large datasets','OP':'?'},{"LOWER":'proficient in natural language processing echniques','OP':'?'},{"LOWER":'skilled in computer vision','OP':'?'}, {"LOWER":'familiar with cloud-based computing services','OP':'?'}
        ]

    
    matcher = Matcher(nlp.vocab)
    matcher.add("Skills", [pattern_s])
    
    cv = fitz.open(file)
    
    pg_t = ""
    for page in cv:
        pg_t = pg_t + str(page.get_text())
        

    pg_t = " ".join(pg_t.split('\n'))
    value = insights(pg_t)

    tt = nlp(pg_t)

    skills = matcher(tt)
    print(len(skills))

    if len(skills) == 0:
        progressbar.set(1)
    elif len(skills) < 5:
        progressbar.set(len(skills) + 1)
    else:
        progressbar.set(len(skills))  
    
    textbox = ctk.CTkTextbox(window, width=300, height= 450)
    textbox.grid(row=1, column=0,sticky="nsew", rowspan = 6)

    for ent in value.ents:
        textbox.insert(0.0, f"{ent.label_.upper() :{10}} - {ent.text}\n\n")

    textbox.insert(0.0, "Insights of this resume are : \n\n")



button = ctk.CTkButton(
    frameb,
    width= 20,
    height= 40,
    text= 'Locate The Resume',
    text_color= ('black','white'),
    fg_color= 'transparent' ,
    border_width= 5,
    border_color= "#FF9966",
    corner_radius= 20,
    hover_color= ('#003399' ,'#FF9966'),
    command= main
    )
button.pack(pady=30)


window.mainloop()
