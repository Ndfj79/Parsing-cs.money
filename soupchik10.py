import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70 (Edition Yx GX)',
    'accept':'application/json, text/plain, */*'
    }


def collect_data(cat_type=2):
    # response = requests.get(url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset=71340&sort=botFirst&withStack=true', headers=headers)
    #
    # with open('result.json', 'w', encoding='utf-8') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)
    #

    offset = 0
    batch_size = 60
    result = []


    while True:
        for item in range(offset,offset+batch_size,60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={item}&sort=botFirst&type={cat_type}&withStack=true'

            response = requests.get(url = url,headers= headers)

            offset+= batch_size

            data = response.json()
            items = data.get('items')

            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_over_price = i.get('overprice')
                    
                    result.append(
                        {
                            'Full_name': item_full_name,
                            '3d': item_3d,
                            'price': item_price,
                            'Overprice': item_over_price
                        }
                    )

        if len(items) < 60:
            break

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)



def main():
    collect_data()

if __name__=='__main__':
    main()
