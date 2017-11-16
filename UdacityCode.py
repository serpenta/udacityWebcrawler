my_page = "web page contents <a class='link' href='http://www.youtube.com'></a> <a href='google.com'></a> <a class='link' style='text-decoration:none' href='www.facebook.com'></a>"

def get_next_target(page):
    anchor = page.find("<a")
    if anchor == -1:
        return None, 0
    href_pos = page.find("href", anchor)
    start_url = page.find("'", href_pos)
    end_url = page.find("'", start_url + 1)
    url = page[start_url + 1:end_url]
    return url, end_url
print get_next_target
