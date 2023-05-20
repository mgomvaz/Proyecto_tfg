'''
Created on 6 mar 2023

@author: zorro
'''
import snscrape.modules.twitter as sntwitter
from datetime import datetime
import nltk
from nltk.corpus import stopwords
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pymongo import MongoClient
url = 'mongodb://localhost:27017'

sent_analyzer = SentimentIntensityAnalyzer()

now = datetime.now()
stopwords_es = set(stopwords.words('spanish'))
stopwords_es.add("http")
stopwords_es.add("https")
rango=50

def nube_palabras(user):
    query = "(from:"+user+") until:"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" since:2010-01-01"
    limit=rango
    #tweets=[]
    expresion_regular = re.compile(r'[^\w\s]')
    mapa= dict()
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if(limit!=0):
            palabras_tweet = nltk.word_tokenize(tweet.rawContent)
            palabras_limpias = []
            for palabra in palabras_tweet:
                palabra_limpia = expresion_regular.sub('', palabra)
                if palabra_limpia != '':
                    palabras_limpias.append(palabra_limpia)            
            #aprovecho para contar las palabras            
            for p in palabras_limpias:
                if p not in stopwords_es:
                        if p not in mapa:
                                mapa[p.lower()]=1
                        else:
                            #mapa[p.lower()]=+1
                            mapa.update({p.lower():mapa.get(p.lower())+1})
                # Unir las palabras limpias para crear el texto del tweet final
                #texto_limpiar = ' '.join(palabras_limpias)
                #tweets.append(texto_limpiar)
            limit=limit-1
        else:
            break
     
    print(sorted(mapa.items(), key=lambda item:item[1], reverse=True))
    return sorted(mapa.items(), key=lambda item:item[1], reverse=True)
           
def opinion_tema(user,tema):
    res=""
    cont=1
    media=0
    query = "(from:"+user+") until:"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" since:2010-01-01"
    if cont!=rango:
        tope=0
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():

               if tema in nltk.tokenize.word_tokenize(tweet.rawContent.lower()):
                print(tweet.rawContent)
                print("\n")
                print(sent_analyzer.polarity_scores(tweet.rawContent))
                media=(media+sent_analyzer.polarity_scores(tweet.rawContent)['compound'])/(cont+1)
                print("\n")
                print("--------------------------------------------------------")
                print("\n")
                cont=cont+1
                if cont==rango:
                    break 
            
    print(media)
    if(media>0.03):
        print("Cuando habla de "+tema+" habla de forma positiva")
        res="Cuando habla de "+tema+" habla de forma positiva"
    if(media<-0.03):
        print("Cuando habla de "+tema+" habla de forma negativa ")
        res="Cuando habla de "+tema+" habla de forma negativa"
    else:
        print("Cuando habla de "+tema+" habla de forma neutra")
        res="Cuando habla de "+tema+" habla de forma neutra"     
    return (user,res,media)

def main():
    cuenta="2010MisterChip"
    dbName = 'TFG'
    collectionName = 'twitter'
    client = MongoClient(url)
    db = client[dbName]
    collection = db[collectionName]
    resultado = collection.find_one({"twitter_id": cuenta})

    if resultado:
        print('El dato está en la base de datos')
        print(resultado)
    else:
        print('El dato no está en la base de datos, vamos a buscarlo')
        
        nube=nube_palabras(cuenta)
        datos_twitter = {
            'twitter_id':cuenta,
            'nube':nube
            }
        
        resultado = collection.insert_one(datos_twitter)
#opinion_tema("2010MisterChip","proton")