from lxml import html
import requests

class Scraper:

  def scrape():
    #Grab new text
    url = "http://www.bigspooncreamery.com/menu1/"

    page = requests.get(url)

    #If successful
    if(page.ok):
        tree = html.fromstring(page.content)
        flavorsHTML = tree.xpath('//section[@id="description"]/div/div/div/div/div/div/ul/li')

        flavors = []
        for flavorHTML in flavorsHTML:
            flavors.append({
                'name': flavorHTML.xpath('./p/strong/text()')[0],
                'blurb': flavorHTML.xpath('./ul/li/p/text()')[0]
            })
        return flavors
    else:
        return None