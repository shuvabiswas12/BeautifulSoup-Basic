from bs4 import BeautifulSoup

def readFile():
    file = open("index.html", "r+")
    data = file.read()
    file.close()
    return data

html_page = readFile()

soup = BeautifulSoup(html_page, 'lxml')

# children  => returns an iterator object

# print(soup.children)

# [print(type(item)) for item in list(soup.children)]

# print(list(soup.children))  # this return all object as a list

# html = list(soup.children)[1]  # returns the first item from the list

# p = list(html.body.children)[1]  # returns the first item from the list

# print(p.get_text())  # return the text which is inside the p tag

# print(soup.find_all('p')[0].get_text())

# print(soup.find('p'))

# print(soup.find_all('p', class_='inner-text'))

# print(soup.find_all(id='first'))


# css selector ...... >>

# print(soup.select('div p'))  # returns all the p tag from all the div tags as a list

# p  = soup.select('body')
# print(p[0].select('p#Second'))

# print(soup.body.find_all('p'))

# contents  => returns a list of all tags

# print(soup.contents)

# next_siblings  => returns a generator object which contains new line ('\n') and other stuff

'''
siblings = soup.find('div').p.next_siblings

for item in siblings:
    if item.string is not None:
        print(len(item.string.strip()))
'''

# descendants  => returns a list of all of the children from all tags
'''
print(list(soup.descendants))

for item in soup.descendants:
    print(item)
    print('*' * 20)
    print('\n\n')
'''

# .attrs  => it returns a dictionary of all attributes
'''
print(soup.find('div').p['id'])
# this is can be written as below ---
print(soup.find('div').p.attrs)

'''

# .strings  => returns a generator object of all string
# print(soup.find('div').p.strings)

# .stripped_strings  => returns a generator object of all
#                       strings which stripped all the space 
# print(soup.find('div').p.stripped_strings)



# .parent  => returns parent of said tag
# print(soup.find('div').parent)

# .name  => returns name of parent
# print(soup.find('div').parent.name)


# .parents  => returns all parent of parent of said tag

'''
for item in soup.find('title').parents:
        print(f'{item} \n \n')

'''



# .next_sibling
# .previous_sibling

'''
div = soup.find('div')
print(div.p.next_sibling.next_sibling)
'''

'''
p = soup.find(id='first').next_sibling.next_sibling
print(p.previous_sibling.previous_sibling)
'''


# .next_siblings
# .previous_siblings

# this two are used for iteration only
'''
for item in soup.find('div').p.next_siblings:
        print(item)

print(list(soup.find('div').p.next_siblings))
'''

'''
for item in soup.find(id='last-text').previous_siblings:
        print(item)

print(list(soup.find(id='last-text').previous_siblings))
'''