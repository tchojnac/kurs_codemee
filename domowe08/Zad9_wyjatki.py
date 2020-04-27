import webbrowser


   # prefixes =
    #https://flynerd.pl
    #http://flynerd.pl
    #www.flynerd.pl
    #flynerd.pl
    #https://
#    1. mają odpowiednie końcówki
#    2. nie mają spacji

#user_url = 'https://flynerd.pl'
def check_url(url):
    allowed_sufixes = ('pl', 'com')
    valid_url = False
    for sufix in allowed_sufixes:
        if url.endwith(sufix):
            print('Prawidlowa koncowka')
            valid_url = True
    if not valid_url:
        raise Exception('Twoj url nie jest obslugiwany')

def with_prefix(url):
    if url.startwith('https://') or url.startwith('http://'):
        return  url
    else:
        return 'http://' + url

user_url = input('Podaj strone www')
user_url = 'https://flynerd.pl'
user_url = user_url.strip()
user_url = user_url.replace(' ', '')

try:
    check_url(user_url)
except Exception as e:
    print('Wpadl blad')
    print(e)
else:
    webbrowser.open(url_withprefix(user_url))




