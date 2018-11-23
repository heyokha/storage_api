## Хранилище файлов с доступом по http

Демон, который предоставляет HTTP API для загрузки, скачивания и удаления файлов.

* [Upload](#upload)
* [Download](#download)
* [Delete](#delete)

**Upload**
----
Метод для загрузки файлов.

* **URL**

  /upload

* **Method:**
  
  `POST`

* **Data Params**

  **Required:**
  `file=[file]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `a7b4b745d1a4e5e95d7a4e71ca3c7c1d`
 
* **Error Response:**

  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `File already exists`

* **Sample Call:**

```bash
curl --request POST \
  --url http://localhost:5000/upload \
  --header 'Cache-Control: no-cache' \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form file=@/home/user/Pictures/example.jpg
```

**Download**
----
Метод для выгрузки файлов.

* **URL**

  */download/\<hash>

* **Method:**
  
  `GET`

* **Data Params**

  **Required:**
  `hash=[str]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[file]`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `File doesn't exist`

* **Sample Call:**

```bash
curl --request GET \
  --url http://localhos5000/download/samplehash \
```
    
**Delete**
----
Метод для удаления файлов.

* **URL**

  */delete/\<hash>

* **Method:**
  
  `DELETE`

* **Data Params**

  **Required:**
  `hash=[str]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `File deleted`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `File doesn't exist`

* **Sample Call:**

```bash
curl --request DELETE \
  --url http://localhos5000/download/samplehash \
```
