
# 概要
 - サンプルコードがここにある。環境構築が面倒なのでオンライン環境でやる
 - https://ja.nuxtjs.org/examples

## 疑問
### 環境構築はどうやるのか？

ざっくり以下の手順

```
npm i -g @vue/cli @vue/cli-init
vue init nuxt-community/starter-template
yarn
yarn dev
```

### asyncDataってなんだっけ

https://ja.nuxtjs.org/guide/async-data/

> サーバーサイドでデータを取得し、それをレンダリングしたいことがあるでしょう。Nuxt.js はコンポーネントのデータをセットする前に非同期の処理を行えるようにするために asyncData メソッドを追加しています。

dataのエクステンション。

コンポーネントがインスタンス化される前に呼び出される

contextオブジェクトにアクセスできる

結局何が非同期なのかいまいちよくわかってないが、インスタンスが作られるタイミングとは別にデータを生成するということで、同期的でないということかな

https://ja.nuxtjs.org/api/context

### loadingコンポーネント

Nuxtはデフォルトでローディングコンポーネントを持っている。

画面上部のプログレスバー。

https://ja.nuxtjs.org/guide/configuration/

これをカスタマイズする場合は、 `nuxt.config.js` で設定を変更したり、カスタムコンポーネントを読み込ませる

https://ja.nuxtjs.org/api/configuration-loading

ローディング画面は、asyncDataのメソッドの中で強制的に待ち状態を作る（setTimeoutなどで）ことで実現可能

