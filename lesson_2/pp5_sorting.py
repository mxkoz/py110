import pprint

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def published_year(list):
    return int(list['published'])

books.sort(key=published_year)
pprint.pprint(books)


dict2 = {'1st': {'d': 3}, 
         '2nd': {'e': 2, 'f': 1}, 
         '3rd': {'g': 0}}
