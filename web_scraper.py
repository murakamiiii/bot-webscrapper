from requests_html import AsyncHTMLSession

async def Web_scraper():
  s_link = ""

  #create the session
  asession = AsyncHTMLSession()

  #define our URL
  url = 'https://mtg.bigweb.co.jp/stocks/free-item-list/43'

  #use the session to get the data
  r = await asession.get(url)

  #Render the page, up the number on scrolldown to page down multiple times on a page
  await r.html.arender()

  objs = r.html.find('.thumbnail a')

  for obj in objs:
    if s_link == "" or s_link != obj.absolute_links:
      s_link = obj.absolute_links
    elif s_link == obj.absolute_links:
      return "false"

    return s_link
    
