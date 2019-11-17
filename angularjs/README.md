# AngularJS

 - AngularとAngularJsがある
   - AngularJSはAngular1.0という古いバージョンで今はAngular
 - https://angular.io/
 - directiveを使う点は、Vueと似ている
 
## Your First App
 - https://angular.io/start
 - EventEmitterが出てきた
 - 開発環境なしで開発むりでは
 - ローカルで開発しようとしたら300MBくらいのサンプルをダウンロードすることに
 - エコシステムに慣れない
 - コンパイル必須
 
## アーキテクチャ
 - https://angular.io/guide/architecture
 - TypeScript
 - モジュール(NgModule)
 - コンポーネント（UIを持つ） <-> サービス（UIを持たない）
   - コンポーネントはサービスにユースケースを移譲する（通信、バリデーション、ログ出力）
   - サービスは複数のコンポーネントで再利用される
 - サービスもクラスとして定義するのはなんかJavaっぽい
 - サービスも状態を持つようなので、DDDのサービスとは違うものっぽい
 - ライブラリについてはHTTPクライアントやCSSアニメーションのラッパなどを自前で持ってるらしい
 
## 結局なんの開発環境で開発すればいいのか？
 - CodeSandbox
    - https://codesandbox.io/
    - ReactやVueの開発もできる
 - StackBlitz 
    - https://stackblitz.com/angular/mjrapnbjydj
    - Angularのサンプルで使われているオンラインエディタ
    - GitHub連携もできるらしい？

## とりあえずStackBlitzでアプリを作り始める
 - 無料版ではedit内容をプライベートにできず、GitHubのプライベートリポジトリに紐づけることもできない
 - なので、VSCodeでプラグインを入れて開発するか、Cloud9を調べてみる
 - あんまりな感じだったら1ヶ月だけStackBlitzの有料版を契約してみる


### Cloud9
 - なんかパッケージインストールが必要そう
    - アプリのリアルタイム表示もできないかな？

## デプロイまで
### StackBlitzの場合
もし任意の場所でホスティングしたい場合は以下のようなことをする必要あり

```
npm install -g @angular/cli
ng new my-project-name
ng build --prod
```

### VSCode
https://qiita.com/henjiganai/items/930a299afa53a968d310

```
ng new my-project-name
ng serve --open
```

## HTTP Request
 - https://angular.jp/guide/http
 - RxJSにも対応しているのでリトライ制御とかできる
