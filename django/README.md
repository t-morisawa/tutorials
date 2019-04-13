# Django チュートリアル

https://docs.djangoproject.com/en/2.2/intro/tutorial01/

## ORMの使い方をメモっていく

2章をやってみたものの理解できず、このあとのチュートリアルの理解度に影響を及ぼしているので復習する。

https://docs.djangoproject.com/en/2.2/intro/tutorial02/

### 使用するDBの設置場所

`mysite/settings.py` を以下のような感じでかく

```
databases = {
    'default': {
        'engine': 'django.db.backends.sqlite3',
        'name': os.path.join(base_dir, 'db.sqlite3'),
    }
}
```

2行目のnameはSQLite3の場合はDBファイルの置き場所となる。

MySQLなどを利用する場合は、ここにUSER, PASSWORDなどの設定が必要。


### 事前準備

マイグレーションを行う。

INSTALLED_APPSを調べて必要なデータベーステーブルを作成する

```
python manage.py migrate
```

### モデルを作る

こんな感じ

```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
```

モデルがあると、migrateしたときにテーブルを作ってそれにアクセスするためのAPIができるらしい

### マイグレーションの確認

以下のコマンドを実行すると `polls/migration/0001_initial.py` と言うのができる。

```
python manage.py makemigrations polls
```

これはマイグレーションの内容を確認するようなものである。

これを直接編集してマイグレーションの内容を変更することもできるらしい？

### 実行されるSQLの確認

```
python manage.py sqlmigrate polls 0001
```

 - PK(id)は自動的に追加される

### 実行

```
python manage.py migrate
```

