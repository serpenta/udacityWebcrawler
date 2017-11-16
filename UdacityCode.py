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

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
