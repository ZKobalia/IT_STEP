"""დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products" მისამართზე, შეამოწმებს 
სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:

ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ 
გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით"""

import requests
def get_data():
    try:
        api_url = "https://fakestoreapi.com/products"
        response = requests.get(api_url)

        if response.status_code != 200:
            print(f"ERROR: can't get data. Status Code: {response.status_code}", "\n")
            return False
        
        data = response.json()
        print(f"Status Code: {response.status_code}", "\n")
        # print(data)
        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ERROR: {http_err}")
    except requests.exceptions.ConnectionError as con_err:
        print(f"Connection ERROR: {con_err}")
    except requests.exceptions as err:
        print(f"ERROR: {err}")


def parese_data():
    all_data = get_data()

    products_price = []
    products_category = set()
    products_id_title = []
    products_rating = []

    for product in all_data:
        products_price.append(product['price'])
        products_category.add(product['category'])
        products_id_title.append({'id': product['id'], 'title': product['title']})
        products_rating.append({'id': product['id'], 'rating': product['rating']})   


    print(f"Products Price List: {products_price}")
    print(f"Products Minimal Price: {min(products_price)}")
    print(f"Products Maximal Price: {max(products_price)}")
    print(f"Products Average Price: {sum(products_price) / len(products_price)}", "\n")
    print(f"Products Category List (without duplicates, sorted): {sorted(list(products_category))}", "\n")
    print(f"Products ID & Title List (sorted by title): {sorted(products_id_title, key = lambda x: x['title'])}", "\n")
    print(f"Products ID & Rating List (sorted by rate): {sorted(products_rating, key = lambda x: x['rating']['rate'])}")

parese_data()