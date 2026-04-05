"""日本語セッション名ジェネレーター

英語のセッション名と同じルールで、日本語の名前を生成します。
例: "Fix login bug" → "ログインバグの修正"
"""


def translate_session_name(english_name: str) -> str:
    """英語のセッション名を日本語に変換する

    標準的なセッション名パターン（動詞 + 対象）を日本語に翻訳します。

    Args:
        english_name: 英語のセッション名（例: "Fix login bug"）

    Returns:
        日本語のセッション名
    """
    # 動詞の翻訳マップ
    verbs = {
        "fix": "修正",
        "add": "追加",
        "update": "更新",
        "remove": "削除",
        "refactor": "リファクタリング",
        "implement": "実装",
        "create": "作成",
        "delete": "削除",
        "improve": "改善",
        "optimize": "最適化",
        "debug": "デバッグ",
        "test": "テスト",
        "configure": "設定",
        "setup": "セットアップ",
        "migrate": "移行",
        "deploy": "デプロイ",
        "review": "レビュー",
        "analyze": "分析",
        "design": "設計",
        "document": "ドキュメント作成",
        "rename": "リネーム",
        "move": "移動",
        "merge": "マージ",
        "revert": "リバート",
        "upgrade": "アップグレード",
        "downgrade": "ダウングレード",
        "enable": "有効化",
        "disable": "無効化",
        "integrate": "統合",
        "extract": "抽出",
        "replace": "置換",
        "convert": "変換",
        "validate": "バリデーション",
        "handle": "ハンドリング",
        "support": "サポート",
        "build": "ビルド",
        "clean": "クリーンアップ",
        "clean up": "クリーンアップ",
        "explore": "調査",
        "investigate": "調査",
        "research": "調査",
    }

    # よく使われる名詞の翻訳マップ
    nouns = {
        "bug": "バグ",
        "error": "エラー",
        "issue": "問題",
        "feature": "機能",
        "function": "関数",
        "method": "メソッド",
        "class": "クラス",
        "component": "コンポーネント",
        "module": "モジュール",
        "test": "テスト",
        "tests": "テスト",
        "config": "設定",
        "configuration": "設定",
        "database": "データベース",
        "api": "API",
        "ui": "UI",
        "style": "スタイル",
        "layout": "レイアウト",
        "page": "ページ",
        "route": "ルート",
        "endpoint": "エンドポイント",
        "auth": "認証",
        "authentication": "認証",
        "authorization": "認可",
        "login": "ログイン",
        "logout": "ログアウト",
        "user": "ユーザー",
        "password": "パスワード",
        "email": "メール",
        "notification": "通知",
        "message": "メッセージ",
        "file": "ファイル",
        "image": "画像",
        "button": "ボタン",
        "form": "フォーム",
        "input": "入力",
        "output": "出力",
        "response": "レスポンス",
        "request": "リクエスト",
        "header": "ヘッダー",
        "footer": "フッター",
        "sidebar": "サイドバー",
        "navbar": "ナビバー",
        "menu": "メニュー",
        "modal": "モーダル",
        "dialog": "ダイアログ",
        "table": "テーブル",
        "list": "リスト",
        "item": "アイテム",
        "data": "データ",
        "cache": "キャッシュ",
        "log": "ログ",
        "logging": "ロギング",
        "performance": "パフォーマンス",
        "security": "セキュリティ",
        "dependency": "依存関係",
        "dependencies": "依存関係",
        "package": "パッケージ",
        "library": "ライブラリ",
        "framework": "フレームワーク",
        "server": "サーバー",
        "client": "クライアント",
        "middleware": "ミドルウェア",
        "handler": "ハンドラー",
        "controller": "コントローラー",
        "service": "サービス",
        "model": "モデル",
        "view": "ビュー",
        "template": "テンプレート",
        "schema": "スキーマ",
        "migration": "マイグレーション",
        "query": "クエリ",
        "session": "セッション",
        "token": "トークン",
        "type": "型",
        "types": "型定義",
        "interface": "インターフェース",
        "documentation": "ドキュメント",
        "docs": "ドキュメント",
        "readme": "README",
        "workflow": "ワークフロー",
        "pipeline": "パイプライン",
        "ci": "CI",
        "cd": "CD",
        "docker": "Docker",
        "container": "コンテナ",
        "environment": "環境",
        "variable": "変数",
        "constant": "定数",
        "hook": "フック",
        "callback": "コールバック",
        "event": "イベント",
        "listener": "リスナー",
        "validator": "バリデーター",
        "formatter": "フォーマッター",
        "parser": "パーサー",
        "util": "ユーティリティ",
        "utility": "ユーティリティ",
        "helper": "ヘルパー",
        "wrapper": "ラッパー",
        "plugin": "プラグイン",
        "extension": "拡張機能",
        "script": "スクリプト",
        "command": "コマンド",
    }

    words = english_name.strip().split()
    if not words:
        return english_name

    # 先頭の動詞を検出
    first = words[0].lower()
    verb_ja = verbs.get(first)

    if verb_ja and len(words) > 1:
        # 残りの単語を名詞として翻訳
        rest = words[1:]
        translated_rest = []
        for w in rest:
            lower = w.lower()
            if lower in nouns:
                translated_rest.append(nouns[lower])
            else:
                # 翻訳できない固有名詞はそのまま残す
                translated_rest.append(w)

        subject = "".join(translated_rest)
        return f"{subject}の{verb_ja}"

    # 動詞が見つからない場合は単語ごとに翻訳を試みる
    translated = []
    for w in words:
        lower = w.lower()
        if lower in nouns:
            translated.append(nouns[lower])
        elif lower in verbs:
            translated.append(verbs[lower])
        else:
            translated.append(w)

    return "".join(translated)


if __name__ == "__main__":
    examples = [
        "Fix login bug",
        "Add user authentication",
        "Update API endpoint",
        "Remove unused dependencies",
        "Refactor database queries",
        "Implement notification service",
        "Optimize cache performance",
        "Debug session handler",
        "Create Docker workflow",
        "Migrate database schema",
        "Review security config",
        "Explore React component",
    ]

    print("=== セッション名の日本語変換 ===\n")
    for name in examples:
        ja = translate_session_name(name)
        print(f"  {name:<40} → {ja}")
