my_page = "web page contents <a class='link' href='http://www.youtube.com'></a> <a href='google.com'></a> <a class='link' style='text-decoration:none' href='www.facebook.com'></a>"

#Finding all urls (no need for links_number())
def find_urls(page):
    end_url = 0
    while True:
        anchor = page.find("<a", end_url)
        if anchor == -1:
            break
        else:
            href_pos = page.find("href", anchor)
            start_url = page.find("'", href_pos)
            end_url = page.find("'", start_url + 1)
            print page[start_url + 1:end_url]
    return

find_urls(my_page)
