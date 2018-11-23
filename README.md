## Хранилище файлов с доступом по http

Демон, который предоставляет HTTP API для загрузки, скачивания и удаления файлов.

* [Upload](#upload)
* [Download](#download)
* [Delete](#delete)

### Upload
* **URL**
  */upload
* **Method:**
  `POST`

#### Download
* **URL**
    */download/\<hash>
* **Method:**
    `GET`
* **URL Params:**
    hash=[str] (required)
    
#### Delete
* **URL**
    */delete/\<hash>
* **Method:**
    `DELETE`
* **URL Params:**
    hash=[str] (required)