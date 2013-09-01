import json
import oauth2
import urllib
import urllib2
import os


def request(latitude, longitude):
    url_params = {}
    url_params['radius_filter'] = 1609 # 1 mile in meters
    url_params['ll'] = str(latitude) + ',' + str(longitude)
    url_params['limit'] = 4 # Maximum number of places to get
    url_params['sort'] = 2 # Sort by rating
    url_params['term'] = 'food+drinks' # Sort by rating

    # Unsigned URL
    encoded_params = ''
    if url_params:
      encoded_params = urllib.urlencode(url_params)
    url = 'http://api.yelp.com/v2/search?%s' % (encoded_params)

    consumer_key = os.environ.get('YELP_CONSUMER_KEY')
    consumer_secret = os.environ.get('YELP_CONSUMER_SECRET')
    token = os.environ.get('YELP_TOKEN')
    token_secret = os.environ.get('YELP_TOKEN_SECRET')
    
    # Sign the URL
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': token,
                          'oauth_consumer_key': consumer_key})

    token = oauth2.Token(token, token_secret)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    # Connect
    try:
        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()
    except urllib2.HTTPError, error:
        response = json.loads(error.read())

    return response


