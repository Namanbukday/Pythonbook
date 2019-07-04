# Return values
'''
def formatted_name(f_name, l_name):
    full_name = f_name.title() + " " + l_name.title()
    return full_name


name = formatted_name('naman', 'bukday')
print(name)
'''

# making an argument optional
'''
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + last_name
    return full_name


name = get_formatted_name('ab', 'gh')
print(name.title())
name = get_formatted_name('as', 'sd', 'fg')
print(name)
'''

# returning a dictionary:
'''
def name(f_name, l_name, age=''):
    person = {'first':f_name,'last':l_name}
    if age:
        person['age'] = age
    return person


p = name('na', 'ma',5)
print(p)
'''


# using  a function with a while loop:
'''
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

while True:
    print("\nEnter your name.")
    print("(or press 'q' to quit)")

    first_name = input("first name")
    if first_name == 'q':
        break

    last_name = input("last name")
    if last_name == 'q':
        break

    n = get_formatted_name(first_name, last_name)
    print("hello, " + n.title())
'''


def city_country(city, country):
    s = city + "," + country
    return s


f = city_country('delhi', 'india')
print(f.title())


def make_album(artist_name, album_title, no_of_tracks=1):
    album = {'artist_name': artist_name, 'album_title': album_title}
    if no_of_tracks:
        album['no_of_tracks'] = no_of_tracks
    return album


while True:
    print("enter artist and title of the album:")
    print("(to quit.press 'q')")
    art_name = input("artist name")
    if art_name == 'q':
        break
    alb_title = input("title of the album")
    if alb_title == 'q':
        break
    n = make_album(art_name, alb_title)
    print("\n", n)
