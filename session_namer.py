"""日本語セッション名ジェネレーター

セッションの内容に基づいて、日本語の名前を自動生成します。
"""

import random
from datetime import datetime

# 季節の言葉
SEASONS = {
    (3, 4, 5): ["春風", "桜", "若葉", "花見", "霞"],
    (6, 7, 8): ["夏空", "風鈴", "蛍", "向日葵", "涼風"],
    (9, 10, 11): ["紅葉", "秋風", "月見", "実り", "夕暮"],
    (12, 1, 2): ["雪", "冬空", "初日", "氷柱", "静寂"],
}

# トピック別の語彙
TOPIC_WORDS = {
    "bug": ["修復", "解決", "調整"],
    "fix": ["修復", "解決", "調整"],
    "feature": ["新機能", "拡張", "追加"],
    "refactor": ["整理", "改善", "刷新"],
    "test": ["検証", "試験", "確認"],
    "docs": ["文書", "記録", "説明"],
    "style": ["装飾", "美化", "整形"],
    "api": ["接続", "連携", "通信"],
    "database": ["蓄積", "保管", "記憶"],
    "ui": ["画面", "表示", "設計"],
    "deploy": ["配備", "公開", "展開"],
    "security": ["防御", "保護", "安全"],
    "performance": ["高速化", "最適化", "効率化"],
}

# 汎用的な動詞・修飾語
ACTIONS = ["の道", "の旅", "の探求", "の工房", "の作業", "の時間"]
ADJECTIVES = ["静かな", "力強い", "丁寧な", "軽やかな", "確かな", "新しい"]


def get_seasonal_word() -> str:
    """現在の季節に応じた言葉を返す"""
    month = datetime.now().month
    for months, words in SEASONS.items():
        if month in months:
            return random.choice(words)
    return "風"


def generate_session_name(topic: str = "", keywords: list[str] | None = None) -> str:
    """セッションの内容に基づいて日本語の名前を生成する

    Args:
        topic: セッションのトピック（例: "bug fix", "new feature"）
        keywords: セッション内容に関連するキーワードのリスト

    Returns:
        日本語のセッション名
    """
    parts = []

    # トピックからマッチする語彙を探す
    topic_word = None
    if topic:
        topic_lower = topic.lower()
        for key, words in TOPIC_WORDS.items():
            if key in topic_lower:
                topic_word = random.choice(words)
                break

    if keywords:
        for kw in keywords:
            kw_lower = kw.lower()
            for key, words in TOPIC_WORDS.items():
                if key in kw_lower:
                    topic_word = random.choice(words)
                    break
            if topic_word:
                break

    # 名前の組み立て
    seasonal = get_seasonal_word()
    adj = random.choice(ADJECTIVES)

    if topic_word:
        # トピックが見つかった場合: 「季節語 + トピック語 + アクション」
        action = random.choice(ACTIONS)
        parts = [seasonal, "・", topic_word, action]
    else:
        # 汎用: 「形容詞 + 季節語 + アクション」
        action = random.choice(ACTIONS)
        parts = [adj, seasonal, action]

    return "".join(parts)


def generate_batch(count: int = 5, topic: str = "") -> list[str]:
    """複数のセッション名候補を生成する"""
    names = set()
    while len(names) < count:
        names.add(generate_session_name(topic=topic))
    return sorted(names)


if __name__ == "__main__":
    print("=== 日本語セッション名ジェネレーター ===\n")

    print("■ 汎用セッション名:")
    for name in generate_batch(5):
        print(f"  {name}")

    print()

    topics = ["bug fix", "new feature", "refactoring", "API integration", "deploy"]
    for t in topics:
        print(f"■ トピック「{t}」:")
        for name in generate_batch(3, topic=t):
            print(f"  {name}")
        print()
