from BeautifulSoup import *
import urllib2
import string
import webbrowser

links_counter = 0
link_dict = {}
review_sites = ['http://www.joystiq.com', 'http://www.ign.com/xbox-one', 'http://www.kotaku.com']

def print_links(inspect_url):
    global links_counter
    print "=================================================="
    print inspect_url
    print "=================================================="
    response = urllib2.urlopen(inspect_url)
    html = response.read()
    home_page = BeautifulSoup(html)
    links = home_page('a')

    for i in links:
        if i.string is not None:
            search_str = i.string.encode('utf-8')
            if ("review" in search_str) or ("review" in i['href'].lower()):
                if is_number(search_str) == False:
                    link_dict[links_counter] = i['href']
                    links_counter += 1
                    print str(links_counter) + ") " + search_str

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def review_finder():
    global links_counter
    for site in review_sites:
        print_links(site)
    print '\n\n'
    choice = int(raw_input("Select a review to view.\n"))
    chosen_link = link_dict[choice]
    webbrowser.open(chosen_link)
    

review_finder()
    


