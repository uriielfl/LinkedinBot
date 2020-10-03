import selenium
from selenium import webdriver
dv = selenium.webdriver.Chrome("chromedriver.exe")
dv.get("https://www.linkedin.com/")


from os import system 
from time import sleep
system('cls')
sleep(5)

#Login
def LoginInLikedin():
    YourUser = str(input("User:\n"))
    YourPw = str(input("Password:\n")) 
    dv.find_element_by_xpath('//*[@id="session_key"]').send_keys(YourUser)
    dv.find_element_by_xpath('//*[@id="session_password"]').send_keys(YourPw)
    sleep(2)
    dv.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button').click()
    sleep(5) 


def Stalk():
    from random import randint
    lettersLi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    rangeofLi = len(lettersLi)
    randomChars = str(lettersLi[randint(0, rangeofLi-1)])#Choose a random letter
    dv.get('https://www.linkedin.com/search/results/people/?keywords='+str(randomChars)+'&origin=SWITCH_SEARCH_VERTICAL')#Search for the chosen random letter
    sleep(3)

    #Scrolls Page Down
    try:
        for x in range(0,5):
            dv.execute_script("window.scrollBy(0,3000)") 
            sleep(2)
    except KeyboardInterrupt:
        pass
    people = dv.find_elements_by_class_name('search-result__result-link') #Get all the people's name in the page.
    names = []
    count = 0 #counter
    links = []
    for p in people:        
        try:
            links.append(str(p.get_attribute('href'))) #Get the links of their profiles.     
        except:
            pass
    rangeofList = len(links)+1 #The links will be duplicated in the list. The lis length is count from Zero to the the last index of our list,
    #so we won't count Zero and we will sum it with one to we get a even number.
    try:
        for i in range(0,int(rangeofList)):
            dv.get(str(links[count]))
            count = count+2 #counter will jump 2 per 2 to don't pass through the duplicate values.
            sleep(3)
    except:
        pass 

    continueordont = str(input("Finalizado! O que deseja fazer?\n1 - Recomeçar\n2 - Modo automático(Para cancelar, pressione 'Ctrl+C'.\n0 - Sair\n")) #Next round? lol
    if continueordont == "1":
        Stalk()
    if continueordont == "2":
        while True:
            Stalk()
    if continueordont == "0":
        exit()
def Menu():
    mainMenu = str(input("Seja bem-vindo, Usuário! O que deseja fazer?\n1 - Stalkear\n2 - Modo automático(Para cancelar, pressione 'Ctrl+C'.\n0 - Sair\n"))
    if mainMenu == "1":
        Stalk()
    if mainMenu == "2":
        while True:
            Stalk()
    if mainMenu == "0":
        exit()

LoginInLikedin()
Menu()
Stalk()
