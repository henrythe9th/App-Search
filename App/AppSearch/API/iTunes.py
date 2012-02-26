from urllib import urlencode
from urllib2 import urlopen
import simplejson

iTunesSearchURL = 'http://itunes.apple.com/search?media=software&'

def search_by_term(term):
    params = urlencode({'term':term})
    
    try:
        print iTunesSearchURL + params
        result = urlopen(iTunesSearchURL + params)
        json = simplejson.loads(result.read())
        if json['resultCount'] == 0:
            return None
        else:
            results = json['results']
            rtn = []
            for app in results:
                basicapp = {}
                basicapp['name'] = app['trackName']
                basicapp['vendor'] = app['artistName']
                basicapp['vendorUrl'] = app['artistViewUrl']
                basicapp['appUrl'] = app['trackViewUrl']
                basicapp['smallIcon'] = app['artworkUrl60']
                basicapp['largeIcon'] = app['artworkUrl512']
                rtn.append(basicapp)
                
            
            return rtn
        
    except:
        return None