#ベースイメージ設定 slimは軽いバージョンのこと
FROM python:3.10-slim 

#作業ディレクトリ設定
WORKDIR /work

COPY requirementes.txt requirementes.txt
RUN pip install --no-cache-dir -r requirementes.txt

COPY . . 
CMD ["python","test2.py"]