import random
def greeting():
    responses = [
        "Hello there!",
        "Hello. Glad to have you with us",
        "Hey!"
    ]
    return random.choice(responses)

def book_table():
    url = "https://www.zomato.com/mumbai/the-fusion-kitchen-borivali-west/book"
    responses = [
        f'Book table on <a href="{url}" target="_blank"><strong>Zomato</strong></a>',
        f'For booking tables please visit <a href="{url}" target="_blank"><strong>here</strong></a>'
    ]
    return random.choice(responses)

def available_tables():
    url = "https://www.zomato.com/mumbai/the-fusion-kitchen-borivali-west/book"
    responses = [
       f'For checking table availability head to <a href="{url}" target="_blank"><strong>Zomato</strong></a>',
       f'Check <a href="{url}" target="_blank"><strong>here</strong></a>'
    ]
    return random.choice(responses)

def goodbye():
    responses = [
       'See you !',
       'Have a good day',
       'Thank you for being with us'
    ]
    return random.choice(responses)

def name():
    responses = [
       'I am Shin',
       'My name is Shin<br>Ma Shin',
       'People know me as Shin'
    ]
    return random.choice(responses)

def address():
    url = r'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3766.6371270817685!2d72.84689371486854!3d19.25464018698566!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b11d2e9df595%3A0x7ffb0239312a17b8!2sThe%20Fusion%20Kitchen!5e0!3m2!1sen!2sin!4v1633783963550!5m2!1sen!2sin'
    return f'<br>Shop 1, IC Colony, Holy Cross Road, Near Bhavdevi Garage, Borivali West, Mumbai <br><br><iframe src="{url}" width="100%" height="auto" style="border:0;" allowfullscreen="" loading="lazy"></iframe>'

def contact():
    return 'You can call us on: <br><a href="tel:7506863906">+917506863906</a><br><a href="tel:9769015215">+919769015215</a>'

def hours():
    return 'We are open from 12 pm to 10 pm'

def menu():
    from datetime import date
    r = random.Random(date.today())
    items = ['Chicken Pesto Pasta','Paneer Pizza','Blueberry Cheesecake','Chicken red thai curry','Garlic Bread']
    url = "https://www.zomato.com/mumbai/the-fusion-kitchen-borivali-west/menu"
    return f'Today\'s special dish is {r.choice(items)} <br> <a href="{url}" target="_blank">Check out full menu</a>'