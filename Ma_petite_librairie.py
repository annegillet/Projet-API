import requests
import json

r = requests.get('https://demo.api-platform.com/books')

"---------------------------------------------------- 1 -------------------------------------------------------------------"
p1 = requests.get('https://demo.api-platform.com/books?order[publicationDate]=desc&page=1')

tenlast = p1.json()

for i in range(10):
    titre = tenlast['hydra:member'][i]['title']
    date = tenlast['hydra:member'][i]['publicationDate']
    print(f"Le livre {titre} a été publié le {date}.")

"---------------------------------------------------- 2 -------------------------------------------------------------------"
#p2 = requests.get('https://demo.api-platform.com/books?order[publicationDate]=desc&author=Dr.%20Kaitlyn%20Ratke&page=1')
#print(p2.json())

searchAuthor = 'Dr. Kaitlyn Ratke'
rAuthor = requests.get('https://demo.api-platform.com/books?author=' + searchAuthor)

if rAuthor.status_code == 200 :
    datAuthor = rAuthor.json()
    for i in range(len(datAuthor['hydra:member'])) :
        titre = datAuthor['hydra:member'][i]['title']
        print(f'Titre de l\'auteur {searchAuthor} est {titre}')
else :
    print('Error')

"---------------------------------------------------- 3 -------------------------------------------------------------------"

searchLivreId = '1d52ba85-97c8-4cc3-b81a-40582f3aff64'
rText = requests.get('https://demo.api-platform.com/books/'+ searchLivreId)

if rText.status_code == 200 :
    dataText = rText.json()
    for i in range(len(dataText['reviews'])) :
        com = dataText['reviews'][i]['body']
        print(f'Commentaire n°{i+1} est {com}')
else :
    print('Error')

"---------------------------------------------------- 4 -------------------------------------------------------------------"
searchPostId = '/books/1b08c9ab-6254-4015-ad14-bac3e5c008df'
comment = {
  "body": "Daaaaaaamn Girl you're nasty",
  "rating": 5,
  "author": "Anne",
  "publicationDate": "2020-01-10T08:23:20.595Z",
  "book": searchPostId
}
rComment = requests.post('https://demo.api-platform.com/reviews', json=comment)

searchLivreId = '1b08c9ab-6254-4015-ad14-bac3e5c008df'
rText = requests.get('https://demo.api-platform.com/books/'+ searchLivreId)

if rText.status_code == 200 :
    dataText = rText.json()
    for i in range(len(dataText['reviews'])) :
        com = dataText['reviews'][i]['body']
        print(f'Commentaire n°{i+1} est {com}')
else :
    print('Error')

"---------------------------------------------------- 5 -------------------------------------------------------------------"
searchPutId = '/books/1b08c9ab-6254-4015-ad14-bac3e5c008df'
comment = {
  "body": "Girl you're nasty",
  "rating": 5,
  "author": "Anne",
  "publicationDate": "2020-01-10T08:23:20.595Z",
  "book": searchPutId
}

putComment = requests.post('https://demo.api-platform.com/reviews', json = comment)
p = putComment.json()

commentupload = {
  "body": "Girl you're pretty",
  "rating": 5,
  "author": "Anne",
  "publicationDate": "2020-01-10T08:23:20.595Z",
  "book": searchPutId
}
rComment = requests.put('https://demo.api-platform.com' + p['@id'], json=commentupload)

searchLivreId = '1b08c9ab-6254-4015-ad14-bac3e5c008df'
rText = requests.get('https://demo.api-platform.com/books/'+ searchLivreId)
