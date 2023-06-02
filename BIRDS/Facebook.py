'''
Created on 25 oct 2022

@author: zorro
'''

from sys import exit
import os


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import wget

url = 'mongodb://localhost:27017'

def buscarPersona(driver):
    time.sleep(3)
    print("escriba el nombre de la persona que busca")
    #nombre=input()
    driver.find_element(By.XPATH, "//input[@placeholder='Search Facebook']").send_keys("luis miguel peña")
    time.sleep(2)
    webdriver.Keys.ENTER
    enlace = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/ul/li[9]/ul/li/div/a").get_attribute("href")
    driver.get(enlace)
    try:
        for i in range(1,6):
            nombre= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div[2]/div[1]/div[1]/div/div[1]/span/div/a".format(i)).text
            try:
                info=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div[2]/div[1]/div[1]/div/div[2]/span/span".format(i)).text                                                         
            except:
                info="no info"                       
            foto=driver.find_element(By.CSS_SELECTOR,"image".format(i)).get_attribute("xlink:href")
            enlace=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div[{}]/div/div/div[2]/div[1]/div[1]/div/div[1]/span/div/a".format(i)).get_attribute("href")
            print("nombre: "+ nombre)
            print("info: "+ info)
            print("foto: "+ foto)
            print("enlace: "+ enlace)
            print("\n")
                                                
    except:
        print("Quieres ver más? responda si/no")
        nombre=input()
                  
def bajaHastaAbajo():
    last_height = driver.execute_script("return document.body.scrollHeight")
    cont=0
    while cont<20:
        SCROLL_PAUSE_TIME = 0.5
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        cont=cont+1
        
def busca_amigos(driver):
    time.sleep(2)
    driver.get("https://www.facebook.com/"+persona+"/friends")
    amigos=[]
    cont=1
    while(cont<5):
        try:
            nombre=driver.find_element(By.CSS_SELECTOR, ".x6s0dn4:nth-child({}) .x1i10hfl > .x193iq5w".format(cont)).text
            link=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[{}]/div[2]/div[1]/a".format(cont)).get_attribute("href")
            amigos.append((nombre,link))            
            print(nombre+": "+link)
        except:
            pass
        cont=cont+1
    return amigos

def busca_fotos(driver):
    time.sleep(2)
    if not os.path.exists("Fotos/fotos_"+persona):
            os.mkdir("Fotos/fotos_"+persona)
    driver.get("https://www.facebook.com/"+"/"+persona+"/photos")
    fotos=[]
    cont=1
    try:
        while(cont<5):
            foto=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[1]/div[{}]/div/div/a/img".format(cont)).get_attribute("src")
            a=wget.download(foto,"Fotos/fotos_"+persona)
            fotos.append(a)
            cont=cont+1
    except:
        pass
    return fotos    
     
def busca_info(driver):
    time.sleep(2)
    driver.get("https://www.facebook.com/"+persona+"/about")
    print("\n")
    print("Información general")
    nombre=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/h1").text

    print("nombre: "+nombre)
    #donde trabaja 
    try:    
        trabajo=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/span").text
        print("trabajo: "+trabajo)
    except:trabajo=""
    try:
        trabajo_s=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/span/span").text
        print("trabajo: "+trabajo_s)
    except:trabajo_s=""
    
    
    #donde estudió
    try:
        estudio=driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/span").text                                             
        print("estudió: "+estudio)
    except:estudio=""
    try:
        estudio_s=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/span/span").text
        print("estudió: "+estudio_s)
    except:pass
    
    
    #donde vive
    try:
        vive=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div[2]/div/span/a/span").text
        print("vive: "+vive)
    except:vive=""
    
    
    #donde nació
    try:
        nace=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[5]/div/div/div[2]/div/span/a/span").text
        print("nació: "+nace)
    except:nace=""
    
    
    #tiene una relación y con quien?
    try:
        pareja=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[6]/div/div/div[2]/div[1]/span/a/span").text
        print("su pareja es: "+pareja)
    except:pareja=""
    
    #estado civil
    try:
        estado_civil=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[6]/div/div/div[2]/div/span").text
        print("estado civil: "+estado_civil)
    except:estado_civil=""
    
    return nombre,trabajo,estudio,vive,nace,pareja,estado_civil
    
def info_work_education(driver):
    time.sleep(2)
    driver.get("https://www.facebook.com/"+persona+"/about_work_and_education")
    print("\n")
    print("TRABAJOS:")
    trabajos=[]
    for i in range(2,5):
        try:
            trabajo=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[{}]/div/div/div[2]/div/span".format(i)).text
            print(trabajo)
            trabajos.append(trabajo)
        except:pass
    
    print("UNIVERSIDADES")
    universidades=[]
    for i in range(2,5):
        try:
            uni=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div[{}]/div/div/div[2]/div/span/a/span".format(i)).text
            print(uni)
            universidades.append(uni)
        except:pass
        
    
    print("COLEGIOS")
    colegios=[]
    for i in range(2,5):
        try:
            cole=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[3]/div/div[{}]/div/div/div[2]/div/span".format(i)).text
            print(cole)
            colegios.append(cole)
        except:pass  
        
    return trabajos,universidades,colegios     

def info_places_lived(driver):
    time.sleep(2)
    driver.get("https://www.facebook.com/"+persona+"/about_places")
    print("\n")
    print("ha vivido en:")
    sitios=[]
    try:      
        for i in range(2,10):
            lugar=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[{}]/div/div/div[2]/div[1]/span/a/span".format(i)).text
            situacion=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div[{}]/div/div/div[2]/div[2]/div/span/span".format(i)).text
            print(situacion+": "+lugar) 
            sitios.append(situacion+" "+lugar)           
    except:
        pass
     
    return sitios   

def info_contact(driver):
    time.sleep(2)
    driver.get("https://www.facebook.com/"+persona+"/about_contact_and_basic_info")
    print("\n")
    #redes
    try:
        nombre_red=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/ul/li/div/div/div[2]/span/div/div/div/div/span").text
        red=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/ul/li/div/div/div[1]/span/a").text
        print(nombre_red+": "+red)
    except:
        nombre_red=""
        red=""
            
    #genero
    try:
        titulo=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/span/div/div/div/div/span").text      
        genero=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/span").text
        print(titulo+": "+genero)
    except:
        titulo="" 
        genero=""
    
    #cumpleaños
    año=""
    try:
        tit=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/span/div/div/div/div/span").text
        cumpleaños=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[1]/span").text
        print(tit+": "+cumpleaños)
        try:   
            año=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div/div[2]/div[2]/div/div/div/div[1]/span").text
            print("año nacimiento: "+año)
        except:año=""
    except:
        tit=""
        cumpleaños=""
    nombreyred=nombre_red+" "+red
    return nombreyred,genero, cumpleaños,año
    
def login(email, password,url):
    global driver
    global persona
    persona=url
    if True:
        
        print('El dato no está en la base de datos, vamos a buscarlo')
        
        options = Options()
        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument('--headless')
        try:
            #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver = webdriver.Chrome("Selenium drivers\chromedriver.exe")
            print("you logged in. Let's rock")
        except:
            print("you need web driver!")
            exit()
        driver.get("https://facebook.com")
        
        # filling the form
        #driver.find_element(By.CSS_SELECTOR,"._9xo5 ._9xo7").click()
        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]").click()
        driver.find_element(By.XPATH, "//input[@placeholder='Correo electrónico o número de teléfono']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']").send_keys(password)
        # clicking on login button
        #driver.find_element(By.NAME,"login").click()
        time.sleep(1.5)
        driver.minimize_window() 
        driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
        time.sleep(2.5)
        try:
            if(driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/span/div/div[2]/a").text=="¿No eres tú?"):
                return "error"
                driver.close()
                
        except:
            pass
        info=busca_info(driver)
        nombre=info[0]
        trabajo=info[1]
        estudio=info[2]
        vive=info[3]
        nace=info[4]
        pareja=info[5]
        estado_civil=info[6]
        
        we=info_work_education(driver)
        trabajos=we[0]
        universidades=we[1]
        colegios=we[2]
        
        pl=info_places_lived(driver)
        
        con=info_contact(driver)
        red=con[0]
        genero=con[1]
        cumpleaños=con[2]
        año=con[3]
        
        fo=busca_fotos(driver)
        amigos=busca_amigos(driver)
        
        datos_facebook = {
            'Face_id':url,
            'nombre':nombre,
            'trabajo':trabajo,
            'estudio':estudio,
            'vive':vive,
            'nace':nace,
            'pareja':pareja,
            'estado_civil':estado_civil,
            'trabajos':trabajos,
            'universidades':universidades,
            'colegios':colegios,
            'pl':pl,
            'red':red,
            'genero':genero,
            'cumpleaños':cumpleaños,
            'año':año,
            'fo':fo,
            'amigos':amigos
            }
        return datos_facebook
    
    driver.close()
          
    #
    
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

