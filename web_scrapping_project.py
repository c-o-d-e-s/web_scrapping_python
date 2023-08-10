#use web scrapping to get real time currency rates
exchange_rate_dict = {}
#required BeautifulSoup code
#{
import requests
from bs4 import BeautifulSoup as bs
Website_URL="https://www.x-rates.com/table/?from=INR&amount=1"
page=requests.get(Website_URL)
Data_paraser = bs(page.content,"html.parser")
#this can differ based on year webpage's html style
results=Data_paraser.find(id="content")
#}
# currency_table_elements has the whole html code of table which has name ratesTable 
currency_table_elements=results.find("table",class_="ratesTable")
#currency_table_element_body is a element for tbody's html code
currency_table_element_body=currency_table_elements.find("tbody")
#currency_table_element_rows is a element for all of table's rows's data
currency_table_element_rows=currency_table_element_body.find_all("tr")
#using loop to access the two elements in row (title,conversion rate)
for currency_table_element_row in currency_table_element_rows: 
    title_element=currency_table_element_row.find("td")
    rate_element=currency_table_element_row.find("td",class_="rtRates")
    # appending the data in dictionary
    #.text just gives text removing html syntax
    #.strip() removes all whitespaces
    exchange_rate_dict[title_element.text.strip()] = float(rate_element.text.strip())

#------------------------------------------------------------------------------------------------------------
#menu driven program from here

while True:
    print("1. For converting to US Dollar\n2. for converting to Euro\n3. for converting to British Pound\n4. for converting to Australian Dollar\n5. for converting to Canadian Dollar\n6. for converting to Singapore Dollar\n7. for converting to Swiss Franc\n8. for converting to Malaysian Ringgit\n9. for converting to Japanese Yen\n10. for converting to Chinese Yuan Renminbi\n11. To exit\n")
    ch=int(input("what would you like to do: "))
    if ch==1:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["US Dollar"]*rs,2),"US Dollars")
        print()
    elif ch==2:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["Euro"]*rs,2),"Euros")
        print()
    elif ch==3:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["British Pound"]*rs,2),"British Pounds")
        print()
    elif ch==4:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["Australian Dollar"]*rs,2),"Australian Dollars")
        print()
    elif ch==5:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["Canadian Dollar"]*rs,2),"Canadian Dollars")
        print()
    elif ch==6:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["Singapore Dollar"]*rs,2),"Singapore Dollars")
        print()
    elif ch==7:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["Swiss Franc"]*rs,2),"Swiss Francs")
        print()
    elif ch==8:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["Malaysian Ringgit"]*rs,2),"Malaysian Ringgits")
        print()
    elif ch==9:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["Japanese Yen"]*rs,2),"Japanese Yen")
        print()
    elif ch==10:
        rs=int(input("enter the amount in Rupees : "))
        print(round(exchange_rate_dict["Chinese Yuan Renminbi"]*rs,2),"Chinese Yuan Renminbi")
        print()
    elif ch==11:
        break
    else:
        print("please choose from choices provided")
        
        




# all tries from here -------------------------------------------------------------------------------------

#print(exchange_rate_dict)

"""#print(currency_table_element_rows.text.strip())
    print(title_element.text.strip())
    print(rate_element.text.strip())
    print()
"""

#print(currency_table_element_rows)
     
#print(results.text.strip())

"""
currency_table_elements=results.find("table",class_="ratesTable")
currency_table_element_rows=currency_table_elements.find_all("tr")
    for currency_table_element_row in currency_table_elements_rows:
    title_element=currency_table_element_row.find("td")
    rate_element=currency_table_element_row.find("td",class_="rtRates")
    print(title_element.text.strip())
    print(rate_element.text.strip())
    print()

print(currency_table_element_rows)
"""
#}
