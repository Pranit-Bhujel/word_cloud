'''Import the required packages.'''
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

'''In case you've saved all the names in excel sheet, then export them as csv and uncomment the following to run.'''
# with open(r'your_file_location', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# text = ""
# for i in data:
#     text += i[0] + " "

'''This is when youve saved all your names in a text file'''
f = open("sample_text.txt", "r")
text = f.read()


wordcloud = WordCloud(background_color="white", max_font_size=120, max_words=500, width=800, height=500, colormap="plasma").generate(text)
plt.figure(figsize = (18, 12))
plt.imshow(wordcloud, interpolation="lanczos")
plt.axis("off")
plt.margins(x=20, y=20)
plt.show()

plt.savefig("image.png")