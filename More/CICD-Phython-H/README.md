# GitLab CICD feladat

## 1. Hozz létre egy projektet, ami 1 szöveges fájlt és 3 python scriptet tartalmaz:

**input.txt**

```
3
12
44
1
5
```

**build.py**

- Olvassa be a vele egy mappában található input.txt fájlt, és hozzon létre egy output.txt-t, ami az input.txt számjainak 2-szeresét tartalmazza soronként:

```
6
24
88
2
10
```

**test.py**

- ellenőrizze le, hogy a vele egy mappában lévő output.txt minden sora  az input.txt kétszerese
- ha nem az, akkor lépjen ki 1-es exit code-al (ezáltal akassza meg a pipeline-t)


**deploy.py**

- hozzon létre egy index.html fájlt, ami tartalmazza az output.txt-t. Pl:

```html
<h1>Output numbers:</h1>
6
24
88
2
10
```

- opcionális feladat: a html fájl tartalmazzon html, head, és body tag-eket is.

## 2. Hozz létre egy gitlab pipeline-t!

- 3 stage-e legyen: Build, Test, Deploy
- Olyan image.-ből indulj ki, ami képes python scripteket futtatni.


## 3. Valósítsd meg az alábbi job-okat:

**build_numbers**

- build stage-ben legyen
- futtassa le a build.py scriptet
- csak akkor fusson le, ha létezik az input.txt fájl
- mentse ki artifact-ba az output fájlt

**test_numbers**

- test stage-ben legyen
- futtassa le a test.py scriptet
- csak akkor fusson le, ha lefutott a build_numbers job

**deploy_numbers**

- deploy stage-ben legyen
- futtassa le a deploy.py-t
- mentse ki artifact-ba az index.html-t

**pages**

- deployolja a GitLab Pages-re az index.html-et

## 4. Ellenőrző feladatok

- Változtasd meg az input.txt fájl számait, és nézd meg, hogy megfelelően végig megy-e a pipeline!
- Töröld ki az input.txt fájlt, és ellenőrizd le, hogy mi történik!
