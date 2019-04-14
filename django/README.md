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

### SHELL

```
>>> from polls.models import Choice, Question

# modelに足した__str__() が働くことを確認
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# [filter]`Django は キーワード引数から database lookup API を使える
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# [get]今年公開された質問を検索
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# 見つからなかったら例外
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# 主キーはpkと言うIFが与えられている
>>> Question.objects.get(pk=1)
<Question: What's up?>

# 自作メソッドが使えることを確認
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# ここからは新しい選択肢を作ってQに紐づけていきます。
>>> q = Question.objects.get(pk=1)

# 選択肢を確認
>>> q.choice_set.all()
<QuerySet []>

# 選択肢を3つ作る
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice は 紐づいた Question へのアクセスが可能
>>> c.question
<Question: What's up?>

# QからCへのアクセスも可能
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# アンダーバー二つで区切ってフィルターかける
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# 選択肢を削除することもできる
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```


## フロントエンドのテストについてメモ

TODO

## テンプレートや静的ファイルのパスをカスタマイズするならどうするか

TODO
