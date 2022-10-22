# Miniapp feladatok  
A feladat leírás mellett találsz egy mini full stack alkamazás. (miniapp)   
Összetétele:  
- A frontend könyvtár tartalmazza a frontendet (FE) (web kiszolgáló szükséges hozzá)  
- A server könyvtár a backendet (BE) (api.js - nodejs) és az adatbázist (DB) (db.json)  
```
./
├───frontend
│       index.html
│       logic.js
│       style.css
│
└───server
        api.js
        db.json
```


## 1. feladat - Dockerfile  
Készítsd el a 2 konténert, dockerfile segítségével  
- FE-hez használj nginx/apache web kiszolgálót
- BE-hez nodejs bázisu imaget, ide másold be a DB-t is.

## 2. feladat - Compose  
Készítsd el a 2 konténert, docker-compose segítségével (.yaml), hasonlóan mint az 1.-es feladatban. 

## 3. feladat - web proxyval  
Készítd el a konténereket, úgy, hogy a frontendhez nginx proxyt használsz
    lásd: [Magas rendelkezésre állás és skálázhatóság](https://e-learning.training360.com/courses/take/architect/lessons/18133297-magas-rendelkezesre-allas-es-skalazhatosag)  

## 4. feladat - Daily deploy  
Készítsd el a konténereket, úgy, hogy a frontend és backend kódbázist egy git repoból frissíted, például minden este 8 órakor.  
Ehhez:  
- Hozz létre egy új repositoryt a **SAJÁT** Github vagy Gitlab fiókodban, a fent látható könyvtárstruktúrával.  
- Írj egy .sh scriptet ami:  
    - Frissíti a repositoryt (Git pull)  
    - Szinkronizálja a konténerekben használt könyvtárakkal 
    - Elkészíti a konténereket  
- Készítsd el hozzá az időzítő (chron) parancsot.  

## 5. feladat - Mindez együtt  
Készítsd el az alkamazás stackjét, úgy, hogy felhasználód az eddigi lehetőségeket.    
 - Az adatbázis változásait őrizze meg *(Kötetkezelés)*  
 - A létrehozandó konténereket docker compose-zal hozd létre szolgáltatásként. *(1/2-es feladat)*   
 - A frontendet kialakítani magas rendelkezésrá állású rendszernek *(3-as feladat)*    
 - A kódbázist git repoból frissítsd időnként. *(4-es feladat)*  
 - A változó paramétereket külső fájlból olvasd fel, használj dockerignore-t ha szükséges. *(lásd [Quickstart: Compose and WordPress](https://docs.docker.com/samples/wordpress/) feladatnál)*  
 - Készíts saját hálózatot hozzá, amely a 192.168.239.0/24-es tartományt használja. 

## Kötetkezelés  
A feladathoz kapott adatbázist: 
1. Másold bele a konténerbe (akár a backendjébe, de kezelheted külön is)  
2. Kezeld a számítógépeden lévő mappában  