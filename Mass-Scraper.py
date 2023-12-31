import urllib
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    
]

# Function to scrape and extract titles from a URL
def scrape_url(url):
    try:
        # Send an HTTP GET request to the URL
        response = urllib.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the title of the page
            title = soup.title.string
            return title
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# Loop through the list of URLs and scrape their titles
for url in urls:
    title = scrape_url(url)
    if title:
        print(f'Title of {url}: {title}')
    print('-' * 30)



import urllib.request
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    'https://www.eventective.com/north-york-on/the-florist-s-loft-713531.html',
'https://www.eventective.com/north-york-on/the-florist-s-loft-713531.html',
'https://www.eventective.com/woodbridge-on/w-event-boutique-656376.html',
'https://www.eventective.com/woodbridge-on/w-event-boutique-656376.html,','
'https://www.eventective.com/etobicoke-on/belmont-event-space-708827.html',
'https://www.eventective.com/etobicoke-on/belmont-event-space-708827.html',
'https://www.eventective.com/toronto-on/society-clubhouse-734791.html',
'https://www.eventective.com/toronto-on/society-clubhouse-734791.html',
'https://www.eventective.com/toronto-on/silent-h-restaurant-754235.html',
'https://www.eventective.com/toronto-on/silent-h-restaurant-754235.html',
'https://www.eventective.com/toronto-on/the-spot-goat-gallery--736324.html',
'https://www.eventective.com/toronto-on/the-spot-goat-gallery--736324.html',
'https://www.eventective.com/toronto-on/pioneer-cruises-737955.html',
'https://www.eventective.com/toronto-on/pioneer-cruises-737955.html',
'https://www.eventective.com/milton-on/italian-cultural-center-of-milton-iccm-755356.html',
'https://www.eventective.com/milton-on/italian-cultural-center-of-milton-iccm-755356.html',
'https://www.eventective.com/cambridge-on/cambridge-butterfly-conservatory-599138.html',
'https://www.eventective.com/cambridge-on/cambridge-butterfly-conservatory-599138.html',
'https://www.eventective.com/richmond-hill-on/espace-studio-733743.html
'https://www.eventective.com/richmond-hill-on/espace-studio-733743.html
'https://www.eventective.com/walters-falls-on/the-falls-inn-walter-s-falls-264301.html
'https://www.eventective.com/walters-falls-on/the-falls-inn-walter-s-falls-264301.html
'https://www.eventective.com/cambridge-on/chicago-pub-billiards-753815.html
'https://www.eventective.com/cambridge-on/chicago-pub-billiards-753815.html
'https://www.eventective.com/milton-on/popup-event-space-740015.html
'https://www.eventective.com/milton-on/popup-event-space-740015.html
'https://www.eventective.com/toronto-on/the-playground-754838.html
'https://www.eventective.com/toronto-on/the-playground-754838.html
'https://www.eventective.com/toronto-on/luma-restaurant-603918.html
'https://www.eventective.com/toronto-on/luma-restaurant-603918.html
'https://www.eventective.com/toronto-on/district-28-599189.html
'https://www.eventective.com/toronto-on/district-28-599189.html
'https://www.eventective.com/toronto-on/toronto-marriott-city-centre-hotel-196369.html
'https://www.eventective.com/toronto-on/toronto-marriott-city-centre-hotel-196369.html
'https://www.eventective.com/toronto-on/archeo-trattoria-603951.html
'https://www.eventective.com/toronto-on/archeo-trattoria-603951.html
'https://www.eventective.com/toronto-on/fermenting-cellar-603072.html
'https://www.eventective.com/toronto-on/fermenting-cellar-603072.html
'https://www.eventective.com/toronto-on/chelsea-hotel-197949.html
'https://www.eventective.com/toronto-on/chelsea-hotel-197949.html
'https://www.eventective.com/toronto-on/high-park-club-663939.html
'https://www.eventective.com/toronto-on/high-park-club-663939.html
'https://www.eventective.com/toronto-on/meridian-hall-587765.html
'https://www.eventective.com/toronto-on/meridian-hall-587765.html
'https://www.eventective.com/toronto-on/beach-united-church-722751.html
'https://www.eventective.com/toronto-on/beach-united-church-722751.html
'https://www.eventective.com/toronto-on/assembly-chef-s-hall-708986.html
'https://www.eventective.com/toronto-on/assembly-chef-s-hall-708986.html
'https://www.eventective.com/toronto-on/radisson-blu-toronto-downtown-603075.html
'https://www.eventective.com/toronto-on/radisson-blu-toronto-downtown-603075.html
'https://www.eventective.com/toronto-on/arta-gallery-445439.html
'https://www.eventective.com/toronto-on/arta-gallery-445439.html
'https://www.eventective.com/toronto-on/2nd-floor-events-594202.html
'https://www.eventective.com/toronto-on/2nd-floor-events-594202.html
'https://www.eventective.com/toronto-on/thompson-landry-gallery-612097.html
'https://www.eventective.com/toronto-on/thompson-landry-gallery-612097.html
'https://www.eventective.com/toronto-on/europa-convention-center-catering-599171.html
'https://www.eventective.com/toronto-on/europa-convention-center-catering-599171.html
'https://www.eventective.com/toronto-on/toronto-wedding-chapel-event-space-246035.html
'https://www.eventective.com/toronto-on/toronto-wedding-chapel-event-space-246035.html
'https://www.eventective.com/toronto-on/yankee-lady-yacht-charters-522765.html
'https://www.eventective.com/toronto-on/yankee-lady-yacht-charters-522765.html
'https://www.eventective.com/toronto-on/the-fifth-events-638693.html
'https://www.eventective.com/toronto-on/the-fifth-events-638693.html
'https://www.eventective.com/toronto-on/le-select-bistro-611579.html
'https://www.eventective.com/toronto-on/le-select-bistro-611579.html
'https://www.eventective.com/toronto-on/doubletree-by-hilton-toronto-downtown-206917.html
'https://www.eventective.com/toronto-on/doubletree-by-hilton-toronto-downtown-206917.html
'https://www.eventective.com/toronto-on/university-club-of-toronto-673331.html
'https://www.eventective.com/toronto-on/university-club-of-toronto-673331.html
'https://www.eventective.com/toronto-on/bar-244-739028.html
'https://www.eventective.com/toronto-on/bar-244-739028.html
'https://www.eventective.com/toronto-on/lun%C3%A9-702891.html
'https://www.eventective.com/toronto-on/lun%C3%A9-702891.html
'https://www.eventective.com/toronto-on/the-porch-685493.html
'https://www.eventective.com/toronto-on/the-porch-685493.html
'https://www.eventective.com/toronto-on/amsterdam-brewery-726202.html
'https://www.eventective.com/toronto-on/amsterdam-brewery-726202.html
'https://www.eventective.com/toronto-on/novotel-toronto-centre-211184.html
'https://www.eventective.com/toronto-on/novotel-toronto-centre-211184.html
'https://www.eventective.com/toronto-on/hockey-hall-of-fame-211793.html
'https://www.eventective.com/toronto-on/hockey-hall-of-fame-211793.html
'https://www.eventective.com/toronto-on/silk-road-lounge-restaurant-742168.html
'https://www.eventective.com/toronto-on/silk-road-lounge-restaurant-742168.html
'https://www.eventective.com/toronto-on/bond-place-hotel-208282.html
'https://www.eventective.com/toronto-on/bond-place-hotel-208282.html
'https://www.eventective.com/toronto-on/blu-ristorante-616170.html
'https://www.eventective.com/toronto-on/blu-ristorante-616170.html
'https://www.eventective.com/toronto-on/artscape-sandbox-670951.html
'https://www.eventective.com/toronto-on/artscape-sandbox-670951.html
'https://www.eventective.com/toronto-on/blitz-art-gallery-753335.html
'https://www.eventective.com/toronto-on/blitz-art-gallery-753335.html
'https://www.eventective.com/toronto-on/super-wonder-gallery-754129.html
'https://www.eventective.com/toronto-on/super-wonder-gallery-754129.html
'https://www.eventective.com/toronto-on/third-place-743752.html
'https://www.eventective.com/toronto-on/third-place-743752.html
'https://www.eventective.com/toronto-on/la-vecchia-ristorante-747179.html
'https://www.eventective.com/toronto-on/la-vecchia-ristorante-747179.html
'https://www.eventective.com/toronto-on/the-yorkville-royal-sonesta-731450.html
'https://www.eventective.com/toronto-on/the-yorkville-royal-sonesta-731450.html
'https://www.eventective.com/toronto-on/peter-triantos-art-galleries-661545.html
'https://www.eventective.com/toronto-on/peter-triantos-art-galleries-661545.html
'https://www.eventective.com/toronto-on/holiday-inn-toronto-downtown-centre-198220.html
'https://www.eventective.com/toronto-on/holiday-inn-toronto-downtown-centre-198220.html
'https://www.eventective.com/toronto-on/gezellig-studios-748759.html
'https://www.eventective.com/toronto-on/gezellig-studios-748759.html
'https://www.eventective.com/toronto-on/183-geary-680855.html
'https://www.eventective.com/toronto-on/183-geary-680855.html
'https://www.eventective.com/toronto-on/campbell-house-museum-484447.html
'https://www.eventective.com/toronto-on/campbell-house-museum-484447.html
'https://www.eventective.com/toronto-on/the-pint-public-house-732734.html
'https://www.eventective.com/toronto-on/the-pint-public-house-732734.html
'https://www.eventective.com/toronto-on/the-sultan-s-tent-cafe-moroc-565255.html
'https://www.eventective.com/toronto-on/the-sultan-s-tent-cafe-moroc-565255.html
'https://www.eventective.com/toronto-on/joey-eaton-centre-659348.html
'https://www.eventective.com/toronto-on/joey-eaton-centre-659348.html
'https://www.eventective.com/toronto-on/island-yacht-club-720297.html
'https://www.eventective.com/toronto-on/island-yacht-club-720297.html
'https://www.eventective.com/toronto-on/the-globe-and-mail-centre-685463.html
'https://www.eventective.com/toronto-on/the-globe-and-mail-centre-685463.html
'https://www.eventective.com/toronto-on/steam-whistle-brewing-216501.html
'https://www.eventective.com/toronto-on/steam-whistle-brewing-216501.html
'https://www.eventective.com/toronto-on/rodney-s-oyster-house-215379.html
'https://www.eventective.com/toronto-on/rodney-s-oyster-house-215379.html
'https://www.eventective.com/toronto-on/toronto-yacht-charters-748655.html
'https://www.eventective.com/toronto-on/toronto-yacht-charters-748655.html
'https://www.eventective.com/toronto-on/moonlight-lounge-734491.html
'https://www.eventective.com/toronto-on/moonlight-lounge-734491.html
'https://www.eventective.com/toronto-on/bar-prequel-750349.html
'https://www.eventective.com/toronto-on/bar-prequel-750349.html
'https://www.eventective.com/toronto-on/canoe-restaurant-210646.html
'https://www.eventective.com/toronto-on/canoe-restaurant-210646.html
'https://www.eventective.com/north-york-on/bellamy-loft-715922.html
'https://www.eventective.com/north-york-on/bellamy-loft-715922.html
'https://www.eventective.com/east-york-on/mg-event-centre-755173.html
'https://www.eventective.com/east-york-on/mg-event-centre-755173.html
'https://www.eventective.com/etobicoke-on/mimico-cruising-club-587625.html
'https://www.eventective.com/etobicoke-on/mimico-cruising-club-587625.html
'https://www.eventective.com/north-york-on/northspace-don-mills-711555.html
'https://www.eventective.com/north-york-on/northspace-don-mills-711555.html
'https://www.eventective.com/north-york-on/eqf-lounge-event-space-749812.html
'https://www.eventective.com/north-york-on/eqf-lounge-event-space-749812.html
'https://www.eventective.com/north-york-on/auberge-du-pommier-210657.html
'https://www.eventective.com/north-york-on/auberge-du-pommier-210657.html
'https://www.eventective.com/north-york-on/the-laneway-event-venue-725286.html
'https://www.eventective.com/north-york-on/the-laneway-event-venue-725286.html
'https://www.eventective.com/east-york-on/ayven-loft-754840.html
'https://www.eventective.com/east-york-on/ayven-loft-754840.html
'https://www.eventective.com/east-york-on/the-column-catering-events-741212.html
'https://www.eventective.com/east-york-on/the-column-catering-events-741212.html
'https://www.eventective.com/concord-on/hazelton-manor-599130.html
'https://www.eventective.com/concord-on/hazelton-manor-599130.html
'https://www.eventective.com/concord-on/terrace-banquet-centre-631646.html
'https://www.eventective.com/concord-on/terrace-banquet-centre-631646.html
'https://www.eventective.com/north-york-on/the-grand-luxe-event-boutique-589513.html
'https://www.eventective.com/north-york-on/the-grand-luxe-event-boutique-589513.html
'https://www.eventective.com/scarborough-on/the-scarboro-golf-country-club-213851.html
'https://www.eventective.com/scarborough-on/the-scarboro-golf-country-club-213851.html
'https://www.eventective.com/woodbridge-on/da-vinci-banquet-hall-204498.html
'https://www.eventective.com/woodbridge-on/da-vinci-banquet-hall-204498.html
'https://www.eventective.com/concord-on/avenue-banquet-hall-204537.html
'https://www.eventective.com/concord-on/avenue-banquet-hall-204537.html
'https://www.eventective.com/etobicoke-on/the-vue-598932.html
'https://www.eventective.com/etobicoke-on/the-vue-598932.html
'https://www.eventective.com/north-york-on/national-event-venue-623957.html
'https://www.eventective.com/north-york-on/national-event-venue-623957.html
'https://www.eventective.com/concord-on/presidente-banquet-hall-209750.html
'https://www.eventective.com/concord-on/presidente-banquet-hall-209750.html
'https://www.eventective.com/mississauga-on/delta-hotels-by-marriott-toronto-mississauga-204114.html
'https://www.eventective.com/mississauga-on/delta-hotels-by-marriott-toronto-mississauga-204114.html
'https://www.eventective.com/mississauga-on/the-waterside-inn-521683.html
'https://www.eventective.com/mississauga-on/the-waterside-inn-521683.html
'https://www.eventective.com/mississauga-on/crystal-grand-banquet-hall-585782.html
'https://www.eventective.com/mississauga-on/crystal-grand-banquet-hall-585782.html
'https://www.eventective.com/mississauga-on/hilton-garden-inn-toronto-airport-west-mississauga-624558.html
'https://www.eventective.com/mississauga-on/hilton-garden-inn-toronto-airport-west-mississauga-624558.html
'https://www.eventective.com/mississauga-on/four-points-element-toronto-airport-641984.html
'https://www.eventective.com/mississauga-on/four-points-element-toronto-airport-641984.html
'https://www.eventective.com/north-york-on/class-resto-lounge-649909.html
'https://www.eventective.com/north-york-on/class-resto-lounge-649909.html
'https://www.eventective.com/concord-on/ascott-parc-event-centre-631276.html
'https://www.eventective.com/concord-on/ascott-parc-event-centre-631276.html
'https://www.eventective.com/mississauga-on/fairfield-inn-suites-by-marriott-toronto-airport-296095.html
'https://www.eventective.com/mississauga-on/fairfield-inn-suites-by-marriott-toronto-airport-296095.html
'https://www.eventective.com/north-york-on/casa-ricca-banquet-hall-693882.html
'https://www.eventective.com/north-york-on/casa-ricca-banquet-hall-693882.html
'https://www.eventective.com/mississauga-on/mississauga-grand-banquet-event-centre-632787.html
'https://www.eventective.com/mississauga-on/mississauga-grand-banquet-event-centre-632787.html
'https://www.eventective.com/etobicoke-on/sheraton-toronto-airport-hotel-conference-centre-196332.html
'https://www.eventective.com/etobicoke-on/sheraton-toronto-airport-hotel-conference-centre-196332.html
'https://www.eventective.com/etobicoke-on/sandman-signature-toronto-airport-hotel-624009.html
'https://www.eventective.com/etobicoke-on/sandman-signature-toronto-airport-hotel-624009.html
'https://www.eventective.com/north-york-on/la-luce-ristorante-213054.html
'https://www.eventective.com/north-york-on/la-luce-ristorante-213054.html
'https://www.eventective.com/etobicoke-on/crowne-plaza-toronto-airport-604127.html
'https://www.eventective.com/etobicoke-on/crowne-plaza-toronto-airport-604127.html
'https://www.eventective.com/etobicoke-on/bell-telephone-historical-garden-courtyard-755354.html
'https://www.eventective.com/etobicoke-on/bell-telephone-historical-garden-courtyard-755354.html
'https://www.eventective.com/concord-on/paradise-banquet-convention-centre-204542.html
'https://www.eventective.com/concord-on/paradise-banquet-convention-centre-204542.html
'https://www.eventective.com/mississauga-on/best-western-plus-toronto-airport-hotel-197214.html
'https://www.eventective.com/mississauga-on/best-western-plus-toronto-airport-hotel-197214.html
'https://www.eventective.com/concord-on/boulevard-room-at-the-avenue-715268.html
'https://www.eventective.com/concord-on/boulevard-room-at-the-avenue-715268.html
'https://www.eventective.com/etobicoke-on/holiday-inn-toronto-airport-east-697637.html
'https://www.eventective.com/etobicoke-on/holiday-inn-toronto-airport-east-697637.html
'https://www.eventective.com/etobicoke-on/woodbine-banquet-convention-hall-205449.html
'https://www.eventective.com/etobicoke-on/woodbine-banquet-convention-hall-205449.html
'https://www.eventective.com/mississauga-on/bos-event-center-744424.html
'https://www.eventective.com/mississauga-on/bos-event-center-744424.html
'https://www.eventective.com/etobicoke-on/hampton-inn-by-hilton-toronto-airport-corporate-centre-680109.html
'https://www.eventective.com/etobicoke-on/hampton-inn-by-hilton-toronto-airport-corporate-centre-680109.html
'https://www.eventective.com/woodbridge-on/tremonti-restaurant-213025.html
'https://www.eventective.com/woodbridge-on/tremonti-restaurant-213025.html
'https://www.eventective.com/woodbridge-on/the-chariot-eventspace-756127.html
'https://www.eventective.com/woodbridge-on/the-chariot-eventspace-756127.html
'https://www.eventective.com/north-york-on/a-event-space-755703.html
'https://www.eventective.com/north-york-on/a-event-space-755703.html
'https://www.eventective.com/toronto-on/dublin-calling-party-pub-kitchen-685457.html
'https://www.eventective.com/toronto-on/dublin-calling-party-pub-kitchen-685457.html
'https://www.eventective.com/toronto-on/the-attic-studio-726362.html
'https://www.eventective.com/toronto-on/the-attic-studio-726362.html
'https://www.eventective.com/toronto-on/granite-brewery-and-restaurant-213765.html
'https://www.eventective.com/toronto-on/granite-brewery-and-restaurant-213765.html
'https://www.eventective.com/toronto-on/riverdale-hub-556340.html
'https://www.eventective.com/toronto-on/riverdale-hub-556340.html
'https://www.eventective.com/toronto-on/one-king-west-hotel-residence-210452.html
'https://www.eventective.com/toronto-on/one-king-west-hotel-residence-210452.html
'https://www.eventective.com/toronto-on/capocaccia-trattoria-661309.html
'https://www.eventective.com/toronto-on/capocaccia-trattoria-661309.html
'https://www.eventective.com/toronto-on/par-tee-putt-toronto-714196.html
'https://www.eventective.com/toronto-on/par-tee-putt-toronto-714196.html
'https://www.eventective.com/toronto-on/jump-restaurant-210648.html
'https://www.eventective.com/toronto-on/jump-restaurant-210648.html
'https://www.eventective.com/toronto-on/bymark-restaurant-210966.html
'https://www.eventective.com/toronto-on/bymark-restaurant-210966.html
'https://www.eventective.com/toronto-on/duke-of-york-221616.html
'https://www.eventective.com/toronto-on/duke-of-york-221616.html
'https://www.eventective.com/toronto-on/f-amelia-restaurant-599166.html
'https://www.eventective.com/toronto-on/f-amelia-restaurant-599166.html
'https://www.eventective.com/toronto-on/caffino-ristorante-599211.html
'https://www.eventective.com/toronto-on/caffino-ristorante-599211.html
'https://www.eventective.com/toronto-on/the-capitol-event-theatre-572391.html
'https://www.eventective.com/toronto-on/the-capitol-event-theatre-572391.html
'https://www.eventective.com/toronto-on/the-private-room-at-fox-and-fiddle-danforth-587682.html
'https://www.eventective.com/toronto-on/the-private-room-at-fox-and-fiddle-danforth-587682.html
'https://www.eventective.com/toronto-on/the-national-club-613432.html
'https://www.eventective.com/toronto-on/the-national-club-613432.html
'https://www.eventective.com/toronto-on/the-strathcona-hotel-398351.html
'https://www.eventective.com/toronto-on/the-strathcona-hotel-398351.html
'https://www.eventective.com/toronto-on/hilton-toronto-210938.html
'https://www.eventective.com/toronto-on/hilton-toronto-210938.html
'https://www.eventective.com/toronto-on/sheraton-centre-toronto-hotel-204482.html
'https://www.eventective.com/toronto-on/sheraton-centre-toronto-hotel-204482.html
'https://www.eventective.com/toronto-on/the-westin-harbour-castle-toronto-206360.html
'https://www.eventective.com/toronto-on/the-westin-harbour-castle-toronto-206360.html
'https://www.eventective.com/toronto-on/the-boulevard-club-204451.html
'https://www.eventective.com/toronto-on/the-boulevard-club-204451.html
'https://www.eventective.com/toronto-on/park-hyatt-toronto-196463.html
'https://www.eventective.com/toronto-on/park-hyatt-toronto-196463.html
'https://www.eventective.com/toronto-on/hyatt-regency-toronto-194780.html
'https://www.eventective.com/toronto-on/hyatt-regency-toronto-194780.html
'https://www.eventective.com/toronto-on/pantages-hotel-206295.html
'https://www.eventective.com/toronto-on/pantages-hotel-206295.html
'https://www.eventective.com/toronto-on/four-seasons-hotel-toronto-211812.html
'https://www.eventective.com/toronto-on/four-seasons-hotel-toronto-211812.html
'https://www.eventective.com/toronto-on/the-omni-king-edward-hotel-603067.html
'https://www.eventective.com/toronto-on/the-omni-king-edward-hotel-603067.html
'https://www.eventective.com/toronto-on/the-one-eighty-630491.html
'https://www.eventective.com/toronto-on/the-one-eighty-630491.html
'https://www.eventective.com/toronto-on/liberty-grand-entertainment-complex-538572.html
'https://www.eventective.com/toronto-on/liberty-grand-entertainment-complex-538572.html
'https://www.eventective.com/toronto-on/gladstone-house-724564.html
'https://www.eventective.com/toronto-on/gladstone-house-724564.html
'https://www.eventective.com/toronto-on/aviv-immigrant-kitchen-730287.html
'https://www.eventective.com/toronto-on/aviv-immigrant-kitchen-730287.html
'https://www.eventective.com/toronto-on/fountain-blu-730571.html
'https://www.eventective.com/toronto-on/fountain-blu-730571.html
'https://www.eventective.com/toronto-on/junto-studio-751266.html
'https://www.eventective.com/toronto-on/junto-studio-751266.html
'https://www.eventective.com/toronto-on/baro-755573.html
'https://www.eventective.com/toronto-on/baro-755573.html
'https://www.eventective.com/toronto-on/delta-toronto-667100.html
'https://www.eventective.com/toronto-on/delta-toronto-667100.html
'https://www.eventective.com/toronto-on/the-great-hall-709847.html
'https://www.eventective.com/toronto-on/the-great-hall-709847.html
'https://www.eventective.com/toronto-on/twist-gallery-613441.html
'https://www.eventective.com/toronto-on/twist-gallery-613441.html
'https://www.eventective.com/toronto-on/the-carlu-613429.html
'https://www.eventective.com/toronto-on/the-carlu-613429.html
'https://www.eventective.com/toronto-on/hilton-garden-inn-toronto-downtown-624566.html
'https://www.eventective.com/toronto-on/hilton-garden-inn-toronto-downtown-624566.html
'https://www.eventective.com/toronto-on/fantasy-farm-event-center-banquet-hall-484913.html
'https://www.eventective.com/toronto-on/fantasy-farm-event-center-banquet-hall-484913.html
'https://www.eventective.com/toronto-on/the-albany-club-503490.html
'https://www.eventective.com/toronto-on/the-albany-club-503490.html
'https://www.eventective.com/toronto-on/windsor-arms-hotel-582497.html
'https://www.eventective.com/toronto-on/windsor-arms-hotel-582497.html
'https://www.eventective.com/toronto-on/vantage-venues-587590.html
'https://www.eventective.com/toronto-on/vantage-venues-587590.html
'https://www.eventective.com/toronto-on/hotel-ocho-599197.html
'https://www.eventective.com/toronto-on/hotel-ocho-599197.html
'https://www.eventective.com/toronto-on/monarch-tavern-570649.html
'https://www.eventective.com/toronto-on/monarch-tavern-570649.html
'https://www.eventective.com/toronto-on/sassafraz-restaurant-216593.html
'https://www.eventective.com/toronto-on/sassafraz-restaurant-216593.html
'https://www.eventective.com/toronto-on/arcadian-court-203205.html
'https://www.eventective.com/toronto-on/arcadian-court-203205.html
'https://www.eventective.com/toronto-on/the-drake-hotel-toronto-204056.html
'https://www.eventective.com/toronto-on/the-drake-hotel-toronto-204056.html
'https://www.eventective.com/toronto-on/great-lakes-schooner-co--195817.html
'https://www.eventective.com/toronto-on/great-lakes-schooner-co--195817.html
'https://www.eventective.com/toronto-on/the-fairmont-royal-york-198777.html
'https://www.eventective.com/toronto-on/the-fairmont-royal-york-198777.html
'https://www.eventective.com/toronto-on/adelaide-hall-714194.html
'https://www.eventective.com/toronto-on/adelaide-hall-714194.html
'https://www.eventective.com/toronto-on/lodge-on-queen-698266.html
'https://www.eventective.com/toronto-on/lodge-on-queen-698266.html
'https://www.eventective.com/toronto-on/918-bathurst-centre-684380.html
'https://www.eventective.com/toronto-on/918-bathurst-centre-684380.html
'https://www.eventective.com/toronto-on/empire-sandy-684470.html
'https://www.eventective.com/toronto-on/empire-sandy-684470.html
'https://www.eventective.com/toronto-on/the-loft-on-king-street-725781.html
'https://www.eventective.com/toronto-on/the-loft-on-king-street-725781.html
'https://www.eventective.com/toronto-on/palais-royale-ballroom-719337.html
'https://www.eventective.com/toronto-on/palais-royale-ballroom-719337.html
'https://www.eventective.com/toronto-on/the-anndore-house-toronto-715309.html
'https://www.eventective.com/toronto-on/the-anndore-house-toronto-715309.html
'https://www.eventective.com/toronto-on/ahma-744973.html
'https://www.eventective.com/toronto-on/ahma-744973.html
'https://www.eventective.com/toronto-on/stock-tc-754476.html
'https://www.eventective.com/toronto-on/stock-tc-754476.html
'https://www.eventective.com/toronto-on/delta-hotels-ontario-206811.html
'https://www.eventective.com/toronto-on/delta-hotels-ontario-206811.html
'https://www.eventective.com/north-york-on/toronto-don-valley-hotel-suites-541171.html
'https://www.eventective.com/north-york-on/toronto-don-valley-hotel-suites-541171.html
'https://www.eventective.com/north-york-on/ontario-science-centre-196961.html
'https://www.eventective.com/north-york-on/ontario-science-centre-196961.html
'https://www.eventective.com/east-york-on/local-public-eatery-leaside-755376.html
'https://www.eventective.com/east-york-on/local-public-eatery-leaside-755376.html
'https://www.eventective.com/north-york-on/ewg-eglinton-west-gallery-687381.html
'https://www.eventective.com/north-york-on/ewg-eglinton-west-gallery-687381.html
'https://www.eventective.com/north-york-on/york-mills-gallery-673737.html
'https://www.eventective.com/north-york-on/york-mills-gallery-673737.html
'https://www.eventective.com/north-york-on/toronto-botanical-garden-642296.html
'https://www.eventective.com/north-york-on/toronto-botanical-garden-642296.html
'https://www.eventective.com/north-york-on/pan-pacific-hotel-toronto-742906.html
'https://www.eventective.com/north-york-on/pan-pacific-hotel-toronto-742906.html
'https://www.eventective.com/etobicoke-on/holiday-inn-toronto-international-airport-704173.html
'https://www.eventective.com/etobicoke-on/holiday-inn-toronto-international-airport-704173.html
'https://www.eventective.com/concord-on/homewood-suites-by-hilton-toronto-vaughan-624568.html
'https://www.eventective.com/concord-on/homewood-suites-by-hilton-toronto-vaughan-624568.html
'https://www.eventective.com/mississauga-on/la-scala-ristorante-213910.html
'https://www.eventective.com/mississauga-on/la-scala-ristorante-213910.html
'https://www.eventective.com/etobicoke-on/tibetan-canadian-cultural-centre-564772.html
'https://www.eventective.com/etobicoke-on/tibetan-canadian-cultural-centre-564772.html
'https://www.eventective.com/woodbridge-on/element-vaughan-southwest-672662.html
'https://www.eventective.com/woodbridge-on/element-vaughan-southwest-672662.html
'https://www.eventective.com/mississauga-on/renaissance-by-the-creek-633106.html
'https://www.eventective.com/mississauga-on/renaissance-by-the-creek-633106.html
'https://www.eventective.com/mississauga-on/hilton-toronto-airport-hotel-suites-205869.html
'https://www.eventective.com/mississauga-on/hilton-toronto-airport-hotel-suites-205869.html
'https://www.eventective.com/mississauga-on/maple-banquet-hall-209295.html
'https://www.eventective.com/mississauga-on/maple-banquet-hall-209295.html
'https://www.eventective.com/mississauga-on/international-centre-196327.html
'https://www.eventective.com/mississauga-on/international-centre-196327.html
'https://www.eventective.com/etobicoke-on/courtyard-toronto-airport-196378.html
'https://www.eventective.com/etobicoke-on/courtyard-toronto-airport-196378.html
'https://www.eventective.com/etobicoke-on/the-westin-toronto-airport-204109.html
'https://www.eventective.com/etobicoke-on/the-westin-toronto-airport-204109.html
'https://www.eventective.com/woodbridge-on/castello-ristorante-209918.html
'https://www.eventective.com/woodbridge-on/castello-ristorante-209918.html
'https://www.eventective.com/woodbridge-on/la-primavera-event-space-204485.html
'https://www.eventective.com/woodbridge-on/la-primavera-event-space-204485.html
'https://www.eventective.com/north-york-on/graydon-hall-manor-210957.html
'https://www.eventective.com/north-york-on/graydon-hall-manor-210957.html
'https://www.eventective.com/thornhill-on/courtyard-toronto-markham-195964.html
'https://www.eventective.com/thornhill-on/courtyard-toronto-markham-195964.html
'https://www.eventective.com/richmond-hill-on/marlowe-restaurant-and-bar-568724.html
'https://www.eventective.com/richmond-hill-on/marlowe-restaurant-and-bar-568724.html
'https://www.eventective.com/etobicoke-on/canadiana-restaurant-banquet-hall-214434.html
'https://www.eventective.com/etobicoke-on/canadiana-restaurant-banquet-hall-214434.html
'https://www.eventective.com/etobicoke-on/royal-king-event-centre-743445.html
'https://www.eventective.com/etobicoke-on/royal-king-event-centre-743445.html
'https://www.eventective.com/scarborough-on/nandan-events-733528.html
'https://www.eventective.com/scarborough-on/nandan-events-733528.html
'https://www.eventective.com/north-york-on/black-creek-event-space-598911.html
'https://www.eventective.com/north-york-on/black-creek-event-space-598911.html
'https://www.eventective.com/mississauga-on/hilton-garden-inn-toronto-airport-624557.html
'https://www.eventective.com/mississauga-on/hilton-garden-inn-toronto-airport-624557.html
'https://www.eventective.com/concord-on/the-venetian-banquet-hospitality-centre-205394.html
'https://www.eventective.com/concord-on/the-venetian-banquet-hospitality-centre-205394.html
'https://www.eventective.com/thornhill-on/le-parc-banquet-hall-611575.html
'https://www.eventective.com/thornhill-on/le-parc-banquet-hall-611575.html
'https://www.eventective.com/markham-on/crystal-fountain-banquet-hall-604018.html
'https://www.eventective.com/markham-on/crystal-fountain-banquet-hall-604018.html
'https://www.eventective.com/toronto-on/sunnyside-pavilion-613425.html
'https://www.eventective.com/toronto-on/sunnyside-pavilion-613425.html
'https://www.eventective.com/toronto-on/the-burroughes-599146.html
'https://www.eventective.com/toronto-on/the-burroughes-599146.html
'https://www.eventective.com/toronto-on/casa-loma-194988.html
'https://www.eventective.com/toronto-on/casa-loma-194988.html
'https://www.eventective.com/markham-on/hilton-toronto-markham-suites-conference-centre-spa-684092.html
'https://www.eventective.com/markham-on/hilton-toronto-markham-suites-conference-centre-spa-684092.html
'https://www.eventective.com/mississauga-on/chef-kausar-s-autaq-banquet-hall-751445.html
'https://www.eventective.com/mississauga-on/chef-kausar-s-autaq-banquet-hall-751445.html
'https://www.eventective.com/mississauga-on/c-banquets-613261.html
'https://www.eventective.com/mississauga-on/c-banquets-613261.html
'https://www.eventective.com/woodbridge-on/kortright-centre-207158.html
'https://www.eventective.com/woodbridge-on/kortright-centre-207158.html
'https://www.eventective.com/mississauga-on/the-glenerin-inn-210950.html
'https://www.eventective.com/mississauga-on/the-glenerin-inn-210950.html
'https://www.eventective.com/woodbridge-on/le-jardin-196699.html
'https://www.eventective.com/woodbridge-on/le-jardin-196699.html
'https://www.eventective.com/mississauga-on/-company-resto-bar-626030.html
'https://www.eventective.com/mississauga-on/-company-resto-bar-626030.html
'https://www.eventective.com/kleinburg-on/copper-creek-golf-club-195376.html
'https://www.eventective.com/kleinburg-on/copper-creek-golf-club-195376.html
'https://www.eventective.com/mississauga-on/europa-convention-centre-204477.html
'https://www.eventective.com/mississauga-on/europa-convention-centre-204477.html
'https://www.eventective.com/oakville-on/dave-and-busters-oakville-706086.html
'https://www.eventective.com/oakville-on/dave-and-busters-oakville-706086.html
'https://www.eventective.com/oakville-on/dirty-martini-oakville-656674.html
'https://www.eventective.com/oakville-on/dirty-martini-oakville-656674.html
'https://www.eventective.com/oakville-on/hilton-garden-inn-toronto-oakville-207029.html
'https://www.eventective.com/oakville-on/hilton-garden-inn-toronto-oakville-207029.html
'https://www.eventective.com/mississauga-on/braeben-golf-course-207825.html
'https://www.eventective.com/mississauga-on/braeben-golf-course-207825.html
'https://www.eventective.com/brampton-on/speranza-banquet-hall-210852.html
'https://www.eventective.com/brampton-on/speranza-banquet-hall-210852.html
'https://www.eventective.com/walters-falls-on/the-falls-inn-walter-s-falls-264301.html
'https://www.eventective.com/walters-falls-on/the-falls-inn-walter-s-falls-264301.html
'https://www.eventective.com/alliston-on/stevenson-inn-and-spa-206442.html
'https://www.eventective.com/alliston-on/stevenson-inn-and-spa-206442.html
'https://www.eventective.com/woodview-on/viamede-resort-200030.html
'https://www.eventective.com/woodview-on/viamede-resort-200030.html
'https://www.eventective.com/cambridge-on/whistle-bear-golf-club-198289.html
'https://www.eventective.com/cambridge-on/whistle-bear-golf-club-198289.html
'https://www.eventective.com/niagara-on-the-lake-on/hilton-garden-inn-niagara-on-the-lake-624560.html
'https://www.eventective.com/niagara-on-the-lake-on/hilton-garden-inn-niagara-on-the-lake-624560.html
'https://www.eventective.com/niagara-falls-on/ruth-s-chris-steak-house-niagara-falls-652051.html
'https://www.eventective.com/niagara-falls-on/ruth-s-chris-steak-house-niagara-falls-652051.html
'https://www.eventective.com/mississauga-on/red-spoon-restaurant-602885.html
'https://www.eventective.com/mississauga-on/red-spoon-restaurant-602885.html
'https://www.eventective.com/cambridge-on/cambridge-butterfly-conservatory-599138.html
'https://www.eventective.com/cambridge-on/cambridge-butterfly-conservatory-599138.html
'https://www.eventective.com/brighton-on/coach-house-micro-weddings-588234.html
'https://www.eventective.com/brighton-on/coach-house-micro-weddings-588234.html
'https://www.eventective.com/thornton-on/the-wilds-at-cedar-valley-golf-course-583028.html
'https://www.eventective.com/thornton-on/the-wilds-at-cedar-valley-golf-course-583028.html
'https://www.eventective.com/burlington-on/tyandaga-golf-course-564471.html
'https://www.eventective.com/burlington-on/tyandaga-golf-course-564471.html
'https://www.eventective.com/oshawa-on/oshawa-convention-centre-713101.html
'https://www.eventective.com/oshawa-on/oshawa-convention-centre-713101.html
'https://www.eventective.com/jordan-station-on/harbour-estates-winery-697261.html
'https://www.eventective.com/jordan-station-on/harbour-estates-winery-697261.html
'https://www.eventective.com/milton-on/popup-event-space-740015.html
'https://www.eventective.com/milton-on/popup-event-space-740015.html
'https://www.eventective.com/guelph-on/royal-city-brewing-company-746506.html
'https://www.eventective.com/guelph-on/royal-city-brewing-company-746506.html
'https://www.eventective.com/mount-albert-on/vivian-events-spa-749353.html
'https://www.eventective.com/mount-albert-on/vivian-events-spa-749353.html
'https://www.eventective.com/cambridge-on/chicago-pub-billiards-753815.html
'https://www.eventective.com/cambridge-on/chicago-pub-billiards-753815.html
'https://www.eventective.com/milton-on/italian-cultural-center-of-milton-iccm-755356.html
'https://www.eventective.com/milton-on/italian-cultural-center-of-milton-iccm-755356.html',
]

# Function to scrape and extract titles from a URL
def scrape_url(url):
    try:
        # Send an HTTP GET request to the URL using urllib
        response = urllib.request.urlopen(url)

        # Read the HTML content of the page
        html_content = response.read()

        # Parse the HTML content of the page
        bsh = BeautifulSoup(html.read(), 'html.parser')
        print(bsh.h1)

        # Extract the title of the page
        a = soup.a.string
        return a
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# Loop through the list of URLs and scrape their titles
for url in urls:
    a = scrape_url(url)
    if a:
        print(f'Title of {url}: {a}')
    print('-' * 30)
