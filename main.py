from tkinter import *
import datetime
import random
start = datetime.datetime.now() + datetime.timedelta(seconds=2)
E = 1
text = ["""Abu Jamal Datar is a Palestinian poet and political activist who was convicted of terrorism in 2002 for 
his role in the suicide bombing attack on the Radio Television Cultural Center in Beirut in October 2000.
In addition to his sentence, Abu Jamal Datar was also banned from writing or speaking in public for eight years, 
in addition to being placed under house arrest.
He was not allowed to leave his home.
""",
"""People said this was wrong but I needed to take care of my nephew until he was 3 months and a formal paternity test 
could be done.
Since I can't pay child support to her I have to see my son twice a week and have a every other weekend visit.
I thought that when the test came back that the ex would get joint physical and legal custody.
I felt that would be fair because of the phone call and email.
""",
"""He seemed to swallow hard, his eyes all confused and blurry looking.
Then, in what seemed like the blink of an eye, he recovered himself and rushed forward, pushing past me, 
towards the group of black men.
At first, I didn't know what to think.
Was he okay?
What the hell was going on?
I had never seen him like this.
I was going to wait until he spoke to make sure he was okay.
""",
"""
But if I want to continue the job I've got now, I've got to make some room in the bed to sit down.
And make the space work.
I'm not one to stay up late watching TV.
My eyes get all puffy and everything.
I watched a movie last night that I've been wanting to see for a long time, called Quills.
It's from the 1970's and about a guy, who's an architect, whose wife dies.
He becomes a recluse.
""",
"""The multivolume list of such venues, which covers even smaller places, is covered by the Internet Archive, though a 
whole lot of it was added on Friday night. Most of the additions are small and obscure, like the pair of gatherings for 
encyclopedists held at the Metropolitan Museum of Art and the court at the Lincoln Center in the 1960s and 1970s.
""",
"""People say that all the time, but I don't agree.
We only did it because he was the tallest guy and it would be a good laugh.
He probably won't get back together with his ex, if he really loved her, because she's got too much baggage for a man 
like him, but he's right, we were far from innocent.
At some point in our lives, we had all done things that we're not proud of, and neither are you.
""",
"""We were working at our real jobs in this show and we realized that, all of our jobs together, we just didn’t make 
that much money, he explained. It became a couple of friends wanting to make a show and their friends would come in.
What started as a simple idea has now turned into a profitable business. The duo have a show that goes out to five 
theaters in New York City and they also do one in Miami
""",
"""In December 2009 he appeared in a guest role on the BBC Scotland soap opera River City as Liam Brenan in a one-off 
Christmas story.
For a second time the character is cast to appear in the series after Liam is admitted to Craiglang.
In 2010, Bradley briefly returned to co-star with Susan Calman in The Big Fat Quiz of the Year, an awards programme 
hosted by Stephen Fry and Jonathan Ross.
Towards the end
""",
"""
We discussed a couple of the fights he's already had that resulted in serious consequences.
How can I be proud of that when all I can think is that he's a little boy who has got to be terrified?
I can't find that pride and I don't know how to.
I don't even know how to deal with this but this is what happened.
So much of our relationship is built around Aiden's progress and our fears and how to make him
"""]

def timer_params(*args):
    global start, E
    if len(text_area.get(0.0, END)) == 2:
        start_e = datetime.datetime.now()
        start = start_e
    if len(text_area.get(0.0, END)) > 2:
        finish = start + datetime.timedelta(seconds=1)
        delta = finish - datetime.datetime.now()
        timer['text'] = str(delta)[:-7]
        if datetime.datetime.now() > finish:
            timer['text'] = '0:00:00'
            check_text(text_area.get(0.0, END))
            text_area.config(state=DISABLED)
            E = 0

def check_text(user_text):
    global E
    W = 0
    S = 0
    for index in range(len(text_area.get(0.0, END).split())):
        if label['text'].split()[index] == text_area.get(0.0, END).split()[index]:
            W += 1
            S += len(label['text'].split()[index])
        else:
            try:
                for x in range(len(label['text'].split()[index])):
                    if label['text'].split()[index][x] == text_area.get(0.0, END).split()[index][x]:
                        S += 1
            except Exception:
                pass
    word_res['text'] = f'{W}/min'
    simbols_res['text'] = f'{S}/min'
    if E == 1:
        with open('result.txt', 'a') as file:
            t = f'{str(datetime.datetime.now()).split(".")[0]}\nWord:{W}/min\nSimbols:{S}/min\n'
            file.write(t)


def clear_text():
    global start, E
    E = 1
    text_area.config(state=NORMAL)
    text_area.delete(0.0, END)
    timer['text'] = '0:01:00'
    start = datetime.datetime.now()

def retreat():
    clear_text()
    label['text'] = random.choice(text)

win = Tk()
win.geometry("705x500")

label = Label(padx=5, text=random.choice(text), justify='left')
label.grid(row=0, column=0, columnspan=3)

text_area = Text(height=10, padx=40)
text_area.config(state=NORMAL)
text_area.bind("<KeyRelease>", timer_params)
text_area.grid(row=1, column=0, columnspan=3)

button_confirm = Button(text="Retreat", command=retreat)
button_confirm.grid(row=2, column=0)

test_button = Button(text='Clear', command=clear_text)
test_button.grid(row=2, column=1)

timer = Label(text="0:01:00", font=20)
timer.grid(row=2, column=2)

label_res = Label(text="Your result", pady=10, font=20)
label_res.grid(row=3, column=1)

word = Label(text="True world:", pady=10, font=20)
word.grid(row=4, column=0)

word_res = Label(text="--/min", pady=10, font=20)
word_res.grid(row=4, column=1)

simbols = Label(text="True Simbols:", pady=10, font=20)
simbols.grid(row=5, column=0)

simbols_res = Label(text="--/min", pady=10, font=20)
simbols_res.grid(row=5, column=1)






win.mainloop()