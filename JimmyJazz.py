import requests
import random
from bs4 import BeautifulSoup as bs

session = requests.session()

def get_sizes_in_stock():
    global session
    endpoint  = "http://www.jimmyjazz.com/mens/footwear/champion-93-eighteen-big-c/CM100105M?color=Red"
    response = session.get(endpoint)
    soup = bs(response.text, "html.parser")

    div = soup.find("div",{"class":"box_wrapper" })
    all_sizes = div.find_all("a")

    sizes_in_stock = []
    for size in all_sizes:
        size_id = size["id"]
        sizes_in_stock.append(size_id.split("_")[1])
    return sizes_in_stock

def add_to_cart():
    global session
    sizes_in_stock = get_sizes_in_stock()
    size_chosen = random.choice(sizes_in_stock)

    endpoint = "http://www.jimmyjazz.com/cart-request/cart/add/%s/1"%(size_chosen)
    print (endpoint)
    response = session.get(endpoint)

    print (response.text)
    return '"success":1' in response.text

#form-xf5VWUJzTx4dSZZycD5CJtDgdoaDR5pAYmzrOPnkWQw

def checkout():
    global session
    endpoint0 = "https://www.jimmyjazz.com/cart/checkout"
    response0 = session.get(endpoint0)

    soup = bs(response0.text,"html.parser")

    inputs = soup.find_all("input",{"name":"form_build_id"})
    form_build_id = inputs[0]["value"]

    print (form_build_id)



    endpoint1 = "https://www.jimmyjazz.com/cart/checkout"
    payload1 = {
    "billing_email": "email@enugrasaio.club",
    "billing_email_confirm": "email@enugrasaio.club",
    "billing_phone": "111-111-1111",
    "email_opt_in":"1",
    "shipping_first_name":"John",
    "shipping_last_name": "Doe",
    "shipping_country_html": "United States",
    "shipping_address1": "123 Main Street",
    "shipping_address2": "",
    "shipping_city": "Main City",
    "shipping_state": "AL",
    "shipping_zip": "11111",
    "shipping_method": "1",
    "billing_same_as_shipping": "1",
    "billing_first_name": "",
    "billing_last_name": "",
    "billing_country": "US",
    "billing_address1": "",
    "billing_address2": "",
    "billing_city": "",
    "billing_state": "",
    "billing_zip": "",
    "payment_type": "credit_card",
    "cc_type": "Visa",
    "cc_number": "4859 1016 7400 3033",
    "cc_exp_month": "10",
    "cc_exp_year": "22",
    "cc_cvv": "726",
    "gc_num": "",
    "form_build_id": form_build_id,
    "form_id": "cart_checkout_form"
    }

    response1 = session.post(endpoint1, data = payload1)

    soup = bs(response1.text,"html.parser")
    inputs = soup.find_all("input",{"name": "form_build_id"})
    form_build_id = inputs[0]["value"]


    endpoint2 = "https://www.jimmyjazz.com/cart/confirm"
    payload2 = {
        "form_build_id":form_build_id,
        "form_id": "cart_confirm_form"
    }

    response2 = session.post(endpoint2, data=payload2)
#developed by Sargune#2462, @ogBearlyWorking(twitter)
add_to_cart()
checkout()
