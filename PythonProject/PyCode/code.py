import requests
from twilio_conn import  send_whatsapp_message , client

def get_quote(category):

    """Fetch a random quote from the ZenQuotes API based on the specified category.
    """
    API_URL = 'https://zenquotes.io/api/random&category={}'.format(category)
    res = requests.get(API_URL)
    print(res)
    print(res.status_code)
    match res.status_code :
        case 200:
            data = res.json()[0]
            quote_text = data['q']
            author_name = data['a']
            quote = f"{quote_text}\n- {author_name}"
            return quote
        case _:
            return "Error: Unable to fetch quote."
quote=get_quote(category='inspire')
if __name__ == "__main__":
    send_whatsapp_message(client, quote)