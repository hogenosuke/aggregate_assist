
# 情報収集・更新通知ツール

このリポジトリは各Webサイトなどから情報を収集しまとめ、Markdown形式とそれぞれ登録したSlack Webhook URLなどに更新情報をまとめて投稿するツールを開発しているところです。

## 主な機能

- 各Webサイトからの情報収集
- 収集した情報のMarkdown形式での出力
- Slack Webhook URLを使用した更新情報の通知

## インストール

以下の手順でツールをインストールしてください。

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
npm install
```

## 使用方法
config.json ファイルに収集対象のWebサイトとSlack Webhook URLを設定します。
以下のコマンドを実行して情報収集と通知を行います。

```
npm start
```

## 貢献
貢献を歓迎します。プルリクエストを送る前に、まずIssueを立ててください。

1. リポジトリをフォークします。
2. フィーチャーブランチを作成します (git checkout -b feature/AmazingFeature)。
3. 変更をコミットします (git commit -m 'Add some AmazingFeature')。
4. ブランチにプッシュします (git push origin feature/AmazingFeature)。
5. プルリクエストを作成します。

# ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細については LICENSE ファイルを参照してください。
