import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarise():
    url = utext.get('1.0', 'end').strip() # to get rid of newlineCharacter

    # nltk.download('punkt')
    # url = 'https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html'

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    #normal to enter
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0','end')
    author.insert('1.0',article.authors)

    publication.delete('1.0','end')
    publication.insert('1.0',article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity},Sentiment : {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral" }')


    #disabled so user cannot change it
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    # print(f'Title: {article.title}')
    # print(f'Authors: {article.authors}')
    # print(f'Publication Date: {article.publish_date}')
    # print(f'Summary: {article.summary}')

    

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x550')


tlabel = tk.Label(root,text = "Title")
tlabel.pack()

title = tk.Text(root, height = 1, width = 140)
title.config(state='disabled', bg='#458B74')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height =1, width = 140)
author.config(state = 'disabled', bg = '#458B74')
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height =1, width = 140)
publication.config(state = 'disabled', bg = '#458B74')
publication.pack()


slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height =20, width = 140)
summary.config(state = 'disabled',bg = '#458B74')
summary.pack()


selabel = tk.Label(root,text = "Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height =1, width = 140)
sentiment.config(state = 'disabled', bg = '#458B74')
sentiment.pack()


ulabel = tk.Label(root,text = "URL")
ulabel.pack()


utext = tk.Text(root, height =1, width = 140)
utext.config(bg = '#458B74')
utext.pack()

btn = tk.Button(root, text = "Summarize", command=summarise) #no call summarise, just referring
btn.pack()

root.mainloop()