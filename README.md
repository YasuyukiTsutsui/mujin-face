# mujin 顔認識サーバ
ソフトウェア工学という講義でグループ開発をした際に作成した商品棚での顔認識をするためのサーバです．

# 要件
git  
Docker  

# 使い方
1. このリポジトリをローカルに落とす  
``` .sourceCode .shell
$ git clone https://github.com/white0221/mujin-face.git
```  

2. イメージのビルド
``` .sourceCode .shell
$ docker build -t mujin-face .
```  

3. コンテナ立ち上げ  
``` .sourceCode .shell
$ docker run -it -v $(pwd):/app -p 5001:5000 mujin-face python app.py
```  

4. ローカルホストに接続  
ブラウザから[localhost:5000](http://localhost:5000)に接続する

# 追記
自分がGitアカウントの設定を誤っていたため、Contributorsで自分のコミットのほとんどが集計されていないですが、Commitには自分の名前で表示されています．
