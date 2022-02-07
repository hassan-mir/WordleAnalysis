import bs4 as bs
import urllib.request
import requests


def get_words_from_url(url, n):
    html_text = requests.get(url).text
    soup = bs.BeautifulSoup(html_text, 'html.parser')

    for script in soup(["script", "style"]):
        script.decompose()

    pages_index = 0
    strips = list(soup.stripped_strings)

    try:
        pages_index = strips.index('Pages:')
    except:
        pages_index = strips.index('BASIC BASIL BASIN BASIS BASKS')+1

    strips = strips[strips.index('There are 12478 five-letter words')+1:pages_index]

    if '(' in strips[0]:
        strips = strips[1:]

    result = []
    for strip in strips:
        result.extend(strip.split())
    return result



##MAIN-----------------------------------------
list_of_words = []

for x in range(1, 16):
    if x==1:
        url = "https://www.bestwordlist.com/5letterwords.htm"
    else:
        url = "https://www.bestwordlist.com/5letterwordspage"+str(x)+".htm"
    list_of_words.extend(get_words_from_url(url, x))

print("size of list of words: " + str(len(list_of_words)))


textfile = open("all_5_lettered_words.txt", "w")
for word in list_of_words:
    textfile.write(word + "\n")
textfile.close()
