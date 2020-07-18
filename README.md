## 유사색상 기반 립스틱 추천 웹
- RGB와 4가지(발색력, 지속력, 발림성, 수분감) 특성 기반으로 유사도를 파악해 유사한 립스틱을 추천
- 사용자의 구매 이력을 기반으로 소비 패턴이 유사한 사용자를 찾아 구매 가능성이 높은 립스틱을 추천
- [유사색 기반 립스틱 추천 웹 PDF 보기](https://github.com/jeonsanggi/flask_server/blob/master/%EC%9C%A0%EC%82%AC%EC%83%89%EC%83%81%20%EA%B8%B0%EB%B0%98%20%EB%A6%BD%EC%8A%A4%ED%8B%B1%20%EC%B6%94%EC%B2%9C%20%EC%9B%B9.pdf)

### Skill
- Python
- Flask
- MySQL
- BeautifulSoup
- Selenium
- Pandas
- K-means clustering
- Scikit Learn
- Bootstrap

### Flask Server

- Window 10
- python 3.7.3


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
