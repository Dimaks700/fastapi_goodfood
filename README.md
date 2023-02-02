# fastapi_goodfood

This is a [FastAPI](https://fastapi.tiangolo.com/) project, API with CRUD for recipes with authorization and authentication, with the ability to download a list of ingredients in PDF format

## Setup
```sh
$ git clone git clone https://github.com/Dimaks700/fastapi_goodfood.git
$ cd cd fastapi_goodfood 
$ pip3 install virtualenv
$ python3 -m virtualenv myenv
$ source myenv/bin/activate
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```
And navigate to `http://127.0.0.1:8000/`.
