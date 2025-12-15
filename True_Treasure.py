import streamlit as st

POINTS = {
    "Wisdom": "知恵",
    "Courage": "勇気",
    "Kindness": "優しさ",
    "Selfishness": "利己的",
}

# ストーリーの各ステージ
STORY_STAGES = {
    # ステージ1: 準備
    1: {
        "text": "You are a seasoned **Treasure Hunter**. The time has come to embark on a grand adventure to find the legendary **True Treasure**! Before setting off, what is the most important thing to prepare?",
        "choices": {
            "A mysterious map said to lead to the treasure's location.": "Wisdom",
            "A reliable team of partners.": "Kindness",
            "Durable equipment, like armor and ropes.": "Courage",
            "Plenty of high-quality food just for you.": "Selfishness",
        },
    },
    # ステージ2: 洞窟への侵入
    2: {
        "text": "Preparation is complete. You start your adventure! Soon, you find a dark, intimidating cave—the rumored entrance. Who should go in first?",
        "choices": {
            "You, the leader, to show no fear.": "Courage",
            "The scout specializing in searching for traps and dangers.": "Wisdom",
            "Everyone together, supporting each other.": "Kindness",
            "One of your less-valued teammates.": "Selfishness",
        },
    },
    # ステージ3: 洞窟内のトラブル
    3: {
        "text": "Inside the cave, many troubles occur: your food supply is running low, one of your partners is injured, and the main flashlight is broken. What do you address first?",
        "choices": {
            "Treating the partner's injury.": "Kindness",
            "Immediately hunting or foraging for food.": "Courage",
            "Finding a way to light the path.": "Wisdom",
            "Encouraging only the strongest teammates to keep going.": "Selfishness",
        },
    },
    # ステージ4: 最終到達
    4: {
        "text": "You overcame countless troubles and finally reached the deepest part of the cave. The air is thick with anticipation. What lies before you is...",
        "choices": {
            "The final choice has been made by your actions.": "Ending", # この選択肢はダミーで、実際には押されない
        },
    },
}

# エンディング
ENDINGS = {
    "Kindness": {
        "title": "The Priceless Companion",
        "text": "Your endless **Kindness** and dedication to your team brought you the True Treasure: the **unbreakable bond of friendship**. Your partners are loyal for life, and together, you embark on even greater adventures. This is a treasure no gold can buy.",
    },
    "Courage": {
        "title": "The Hero's Sword",
        "text": "Your unwavering **Courage** and willingness to face danger led you to the True Treasure: the legendary **Hero's Sword**. With this mighty weapon, you become the most famous and respected adventurer in the land, never fearing any foe.",
    },
    "Wisdom": {
        "title": "The Book of Magic",
        "text": "Your sharp **Wisdom** and careful planning were the True Treasure all along. You found the **Ancient Book of Magic**, filled with forbidden knowledge. You dedicate your life to mastering the arts, becoming the most knowledgeable scholar and wizard the world has ever known.",
    },
    "Selfishness": {
        "title": "The Bad Reputation",
        "text": "Your **Selfishness** caused great damage to your team and reputation. While you might have found some small riches, your partners abandoned you. You are known as a treacherous and unreliable hunter, forever cursed to search for treasure alone, finding only **bad reputation**.",
    },
}

def get_final_ending(scores):
    """スコアに基づいて最終エンディングのキーを決定する"""
    if not scores:
        # スコアがない場合のデフォルト（エラー回避）
        return "Selfishness"

    # スコアが最も高い属性を探す
    # (属性名, スコア) のリストを作成
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    # 最高のスコアを持つ属性が一つだけの場合
    highest_score = sorted_scores[0][1]
    highest_attributes = [attr for attr, score in scores.items() if score == highest_score]

    if len(highest_attributes) == 1:
        return highest_attributes[0]
    else:
        # スコアが同点の場合の優先順位（ゲームバランスのため）:
        # Kindness (協調性) -> Wisdom (知恵) -> Courage (行動力) -> Selfishness (利己的)
        priority = ["Kindness", "Wisdom", "Courage", "Selfishness"]
        for attr in priority:
            if attr in highest_attributes:
                return attr

# スコア表示用の日本語マッピング
SCORE_LABELS_EN = {
    "Kindness": "Kindness (The Team Player)",
    "Courage": "Courage (The Fighter)",
    "Wisdom": "Wisdom (The Planner)",
    "Selfishness": "Selfishness (The Individualist)",
}