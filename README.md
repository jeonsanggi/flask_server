### Flask Server

- Window 10
- python 3.7.3

#### Python Version

- Python 2.7 or python 3.4 이상

#### Create an Environment

```bash
pip install virtualenv
cd flask_server
virtualenv venv
venv\Scripts\activate
```

#### Install Flask

```bash
pip install Flask
pip install Pandas
pip install numpy
conda install -c conda-forge scikit-surprise
```

#### Start

```bash
# 설정(window cmd)
# flask_server\
set FLASK_APP=flaskr

# 실행
flask run
```

- 브라우저에서 http://127.0.0.1:5000/ 접속
