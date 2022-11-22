import requests
import time
import csv
from time import sleep, time
from termcolor import colored
from datetime import datetime
from dhooks import *
import random
from bs4 import BeautifulSoup
import threading


def justDate():
    date = str(datetime.utcnow().strftime('%d-%m-%Y'))
    return date


def getTime(task_num):
    date = str(datetime.utcnow().strftime('%d-%m-%Y'))
    t = str(datetime.utcnow().strftime('%H:%M:%S'))
    (h, m, s) = t.split(":")
    h = int(h) + 1
    finalTime = f"{date} {h}:{m}:{s}"
    a = f"[Shoelosophy] [{finalTime}] [{task_num}]"
    return a


def get_code(province):
    place = []
    codes = [
        "126",
        "127",
        "128",
        "129",
        "130",
        "131",
        "132",
        "133",
        "134",
        "135",
        "136",
        "137",
        "138",
        "139",
        "140",
        "141",
        "142",
        "143",
        "144",
        "145",
        "146",
        "147",
        "148",
        "149",
        "150",
        "151",
        "152",
        "153",
        "154",
        "155",
        "156",
        "157",
        "158",
        "159",
        "160",
        "161",
        "162",
        "163",
        "164",
        "165",
        "166",
        "167",
        "168",
        "169",
        "170",
        "171",
        "172",
        "173",
        "174",
        "175",
        "176",
        "177",
        "178",
        "179",
        "180",
        "181",
        "182",
        "183",
        "184",
        "185",
        "186",
        "187",
        "188",
        "189",
        "190",
        "191",
        "192",
        "193",
        "194",
        "195",
        "196",
        "197",
        "198",
        "199",
        "200",
        "201",
        "202",
        "203",
        "204",
        "205",
        "206",
        "207",
        "208",
        "209",
        "210",
        "211",
        "212",
        "213",
        "214",
        "215",
        "216",
        "217",
        "218",
        "219",
        "220",
        "221",
        "222",
        "223",
        "224",
        "225",
        "226",
        "227",
        "228",
        "229",
        "230",
        "231",
        "232",
        "233",
        "234",
        "235"
    ]
    provinces = [
        "AG",
        "AL",
        "AN",
        "AO",
        "AR",
        "AP",
        "AT",
        "AV",
        "BA",
        "BT",
        "BL",
        "BN",
        "BG",
        "BI",
        "BO",
        "BZ",
        "BS",
        "BR",
        "CA",
        "CL",
        "CB",
        "CI",
        "CE",
        "CT",
        "CZ",
        "CH",
        "CO",
        "CS",
        "CR",
        "KR",
        "CN",
        "EN",
        "FM",
        "FE",
        "FI",
        "FG",
        "FC",
        "FR",
        "GE",
        "GO",
        "GR",
        "IM",
        "IS",
        "AQ",
        "SP",
        "LT",
        "LE",
        "LC",
        "LI",
        "LO",
        "LU",
        "MC",
        "MN",
        "MS",
        "MT",
        "VS",
        "ME",
        "MI",
        "MO",
        "MB",
        "NA",
        "NO",
        "NU",
        "OG",
        "OT",
        "OR",
        "PD",
        "PA",
        "PR",
        "PV",
        "PG",
        "PU",
        "PE",
        "PC",
        "PI",
        "PT",
        "PN",
        "PZ",
        "PO",
        "RG",
        "RA",
        "RC",
        "RE",
        "RI",
        "RN",
        "RM",
        "RO",
        "SA",
        "SS",
        "SV",
        "SI",
        "SR",
        "SO",
        "TA",
        "TE",
        "TR",
        "TO",
        "TP",
        "TN",
        "TV",
        "TS",
        "UD",
        "VA",
        "VE",
        "VB",
        "VC",
        "VR",
        "VV",
        "VI",
        "VT"
    ]
    a = len(provinces)

    for i in range(a):
        this = provinces[i]
        if province in this:
            place.append(i)

    n = place[0]
    province_id = codes[n]
    return province_id


def info_all(s, task_num, url):
    print(f"{colored(getTime(task_num), 'blue')} {colored(f'Getting product page', 'cyan')} ")
    r = s.get(url)
    if r.status_code == 200:
        try:
            soup = BeautifulSoup(r.text, "lxml")
            token = soup.find("input", {"name": "leoproductsearch_static_token"})["value"]
            group_2 = soup.find("input", {"name": "group[2]"})["value"]
            pid = soup.find("a", {"class": "open-review-form"})["data-id-product"]
            img = soup.find("img", {"class": "js-modal-product-cover product-cover-modal"})["src"]
            product_name = soup.find("img", {"class": "js-modal-product-cover product-cover-modal"})["alt"]
            price = soup.find("span", {"class": "current-price-value"}).text
            try:
                list_sizes = soup.findAll("input", {"class": "input-radio"})
                lenght = len(list_sizes)
                list_size = []
                user_size = []
                for h in range(lenght):
                    x = str(list_sizes[h])
                    if "US" in x:
                        try_ = x.split('value="')[1]
                        f = try_.split('"/>')[0]
                        real = f.strip()
                        list_size.append(real)
                group_1 = random.choice(list_size)
                for h in range(lenght):
                    x = str(list_sizes[h])
                    if group_1 in x:
                        if "US" in x:
                            a = x.split('title="')[1]
                            b = a.split('" type="radio"')[0]
                            user = b.strip()
                            user_size.append(user)
                user_sz = random.choice(user_size)
                return s, token, group_2, pid, img, product_name, price, group_1, user_sz
            except Exception as e:
                print(f"{colored(getTime(task_num), 'blue')} {colored(f'Product out of stock', 'red')} ")
                sleep(3)
                info_all(s, task_num, url)
        except Exception as e:
            print(f"{colored(getTime(task_num), 'blue')} {colored(f'Error getting product info [{e}]', 'red')} ")
            sleep(3)
            info_all(s, task_num, url)
    else:
        print(f"{colored(getTime(task_num), 'blue')} "
              f"{colored(f'Error getting product page [{r.status_code}]', 'red')} ")
        sleep(3)
        info_all(s, task_num, url)


def atc(s, token, group_2, pid, group_1, task_num, user_sz, url):
    head_atc = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "it-IT,it;q=0.9,ca-IT;q=0.8,ca;q=0.7,en-GB;q=0.6,en;q=0.5,pl-PL;q=0.4,pl;q=0.3,en-US;q=0.2",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
    }
    pay_atc = f"token={token}&id_product={pid}&id_customization=0&group%5B1%5D={group_1}&group%5B2%5D={group_2}&qty=1&add=1&action=update"
    print(f"{colored(getTime(task_num), 'blue')} {colored(f'Attempting add to cart [{user_sz}]', 'cyan')} ")
    r = s.post("https://shoelosophy.it/en/cart", headers=head_atc, data=pay_atc)
    soup = BeautifulSoup(r.text, "lxml")
    string_soup = str(soup)
    if '"quantity":1' in string_soup:
        print(f"{colored(getTime(task_num), 'blue')} {colored(f'Added to cart [{user_sz}]', 'magenta')} ")
        return True
    else:
        if r.status_code != 200:
            print(f"{colored(getTime(task_num), 'blue')} "
                  f"{colored(f'Error adding to cart [{user_sz}]', 'red')} ")
            sleep(3)
            atc(s, token, group_2, pid, group_1, task_num, user_sz, url)
        else:
            print(f"{colored(getTime(task_num), 'blue')} "
                  f"{colored(f'Product out of stock [{user_sz}]', 'red')} ")
            sleep(3)
            info_all(s, task_num, url)


def checkout(s, code_id, task_num, email, phone, name, surname, cap, city, address, num):
    try:
        email = email.replace("@", "%40")
        city = city.replace(" ", "+")
        address = address.replace(" ", "+")
        r = s.get("https://shoelosophy.it/en/order-shoelosophy")
        soup = BeautifulSoup(r.text, "lxml")
        fit = str(soup)
        customer_token_1 = fit.split('psgdpr_customer_token = "')[1]
        cust_tok = customer_token_1.split('";')[0]
        a = fit.split('psgdpr_guest_token = "')[1]
        guest = a.split('";')[0]
        c = fit.split('psgdpr_id_module = "')[1]
        module = c.split('";')[0]
        b = fit.split('psgdpr_id_guest = "')[1]
        id_guest = b.split('";')[0]
        if r.status_code == 200:
            head_pls = {
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "it-IT,it;q=0.9,ca-IT;q=0.8,ca;q=0.7,en-GB;q=0.6,en;q=0.5,pl-PL;q=0.4,pl;q=0.3,en-US;q=0.2",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest"
            }
            pay_pls = f"supercheckoutPlaceOrder=1&checkout_option=1&supercheckout_email={email}&supercheckout_password=" \
                      f"&SubmitLogin=SubmitLogin&customer_personal%5Bpassword%5D=&customer_personal%5Bid_gender%5D=2&cu" \
                      f"stomer_personal%5Bdob_days%5D=22&customer_personal%5Bdob_months%5D=11&customer_personal%5Bdob_y" \
                      f"ears%5D=2002&shipping_address%5Bfirstname%5D={name}&shipping_address%5Blastname%5D={surname}&sh" \
                      f"ipping_address%5Bcompany%5D=&shipping_address%5Bvat_number%5D=&shipping_address%5Baddress1%5D" \
                      f"={address}+{num}&shipping_address%5Baddress2%5D=&shipping_address%5Bpostcode%5D={cap}&shipping_" \
                      f"address%5Bcity%5D={city}&shipping_address%5Bid_country%5D=10&shipping_address%5Bid_state%5D" \
                      f"={code_id}&shipping_address%5Bphone_mobile%5D={phone}&shipping_address%5Bother%5D=&shipping_addr" \
                      f"ess%5Bdni%5D=&use_for_invoice=on&payment_address%5Bfirstname%5D=&payment_address%5Blastname%5D=&" \
                      f"payment_address%5Bcompany%5D=&payment_address%5Bvat_number%5D=&payment_address%5Baddress1%5D=&pa" \
                      f"yment_address%5Baddress2%5D=&payment_address%5Bpostcode%5D=&payment_address%5Bcity%5D=&payment_a" \
                      f"ddress%5Bid_country%5D=10&payment_address%5Bid_state%5D={code_id}&payment_address%5Bphone%5D=&p" \
                      f"ayment_address%5Bphone_mobile%5D=&payment_address%5Bother%5D=&payment_address%5Bdni%5D=&deliver" \
                      f"y_option%5B47%5D=21%2C&payment_method=payment-option-4&quantity_3180_44129_47_0_hidden=1&quanti" \
                      f"ty_3180_44129_47_0_minqty=1&quantity_3180_44129_47_0=1&submitDiscount=1&discount_name=&comment=" \
                      f"&supercheckout_default_policy=I+agree+to+the+terms+of+service+and+will+adhere+to+them+unconditio" \
                      f"nally.&conditions_to_approve%5Bterms-and-conditions%5D=1&supercheckout_submission="
            print(f"{colored(getTime(task_num), 'blue')} {colored(f'Submitting shipping', 'cyan')} ")
            r = s.post(
                "https://shoelosophy.it/en/en/index.php?fc=module&module=supercheckout&controller=supercheckout&rand=1656607733640&ajax=true",
                headers=head_pls, data=pay_pls)
            if r.status_code == 200:
                head_tokens = {
                    "accept": "*/*",
                    "accept-language": "it-IT,it;q=0.9,ca-IT;q=0.8,ca;q=0.7,en-GB;q=0.6,en;q=0.5,pl-PL;q=0.4,pl;q=0.3,en-US;q=0.2",
                    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "x-requested-with": "XMLHttpRequest"
                  }
                r = s.get(f"https://shoelosophy.it/en/module/psgdpr/FrontAjaxGdpr?ajax=true&action=AddLog&id_customer=0"
                          f"&customer_token={cust_tok}&id_guest={id_guest}&guest_token={guest}&id_module={module}",
                          headers=head_tokens)
                if r.status_code == 200:
                    head_pp = {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-language": "it-IT,it;q=0.9,ca-IT;q=0.8,ca;q=0.7,en-GB;q=0.6,en;q=0.5,pl-PL;q=0.4,pl;q=0.3,en-US;q=0.2",
                        "cache-control": "max-age=0",
                        "content-type": "application/x-www-form-urlencoded",
                        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1"
                    }
                    print(f"{colored(getTime(task_num), 'blue')} {colored(f'Submitting order', 'cyan')} ")
                    r = s.post("https://shoelosophy.it/en/module/paypal/ecInit?credit_card=0", headers=head_pp)
                    if "paypal" in r.url:
                        print(f"{colored(getTime(task_num), 'blue')} {colored(f'Checkout successfully', 'magenta')} ")
                        return r.url
                    else:
                        print(f"{colored(getTime(task_num), 'blue')} "
                              f"{colored(f'Error getting PayPal [{r.status_code}]', 'red')} ")
                        sleep(3)
                        checkout(s, code_id, task_num, email, phone, name, surname, cap, city, address, num)
                else:
                    print(f"{colored(getTime(task_num), 'blue')} "
                          f"{colored(f'Error submitting tokens [{r.status_code}]', 'red')} ")
                    sleep(3)
                    checkout(s, code_id, task_num, email, phone, name, surname, cap, city, address, num)
            else:
                print(f"{colored(getTime(task_num), 'blue')} "
                      f"{colored(f'Error submitting shipping [{r.status_code}]', 'red')} ")
                sleep(3)
                checkout(s, code_id, task_num, email, phone, name, surname, cap, city, address, num)
        else:
            print(f"{colored(getTime(task_num), 'blue')} "
                  f"{colored(f'Error getting checkout [{r.status_code}]', 'red')} ")
            sleep(3)
            checkout(s, code_id, task_num, email, phone, name, surname, cap, city, address, num)
    except:
        print(f"{colored(getTime(task_num), 'blue')} {colored(f'Code error - WTF', 'red')} ")
        sleep(3)
        checkout(s, code_id, task_num, email, phone, name, surname, cap, city, address, num)


def getit(email, phone, name, surname, cap, city, province, address, num, task_num, url):
    print(f"{colored(getTime(task_num), 'blue')} {colored(f'Starting tasks', 'grey')} ")
    start = time()
    s = requests.Session()
    try:
        info = info_all(s, task_num, url)
        s = info[0]
        token = info[1]
        group_2 = info[2]
        pid = info[3]
        img = info[4]
        product_name = info[5]
        price = info[6]
        group_1 = info[7]
        user_sz = info[8]
        atc_status = atc(s, token, group_2, pid, group_1, task_num, user_sz, url)
        if atc_status:
            lmao = get_code(province)
            code_id = lmao[0]
            pp_url = checkout(s, code_id, task_num, email, phone, name, surname, cap, city, address, num)

            end = time()
            checkout_time = end - start
            time_check = round(checkout_time, 2)
            hook = Webhook('YOUR_WEBHOOK')

            now = justDate()
            embed = Embed(
                color=0x202020
            )
            embed.set_title(title="Checkout successful", url=pp_url)
            embed.set_author(name="PiedeAIO",
                             icon_url="https://cdn.discordapp.com/attachments/799962707377127444/990"
                                      "984201664888912/bartFoto.PNG")
            embed.add_field(name="Store", value="||Shoelosophy||")
            embed.add_field(name="Product", value=f"{product_name}")
            embed.add_field(name="Pid", value=f"||{pid}||")
            embed.set_thumbnail(url=img)
            embed.add_field(name="Size", value=f"{user_sz}")
            embed.add_field(name="Price", value=f"{price}")
            embed.add_field(name="Speed", value=f"{time_check}s")
            embed.set_footer(text=f"{now} • Powered by @nicko_py",
                             icon_url="https://cdn.discordapp.com/attachments/799962707377127444/9909842"
                                      "01664888912/bartFoto.PNG")
            hook.send(embed=embed)
    except:
        print(f"{colored(getTime(task_num), 'blue')} {colored(f'Error getting info', 'red')} ")
        sleep(3)
        info_all(s, task_num, url)


def start():
    with open('profile.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        i = 0
        for row in csv_reader:
            i += 1
            if line_count == 0:
                line_count += 1
            else:
                sleep(0.1)
                try:
                    url = row[0]
                    email = row[1]
                    phone = row[2]
                    name = row[3]
                    surname = row[4]
                    cap = row[5]
                    city = row[6]
                    province = row[7]
                    address = row[8]
                    num = row[9]
                    thread = threading.Thread(target=getit, args=(email, phone, name, surname, cap, city, province, address, num, (i-2), url))
                    thread.start()
                except Exception as e:
                    pass


start()
