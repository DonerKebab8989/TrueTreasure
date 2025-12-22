import streamlit as st
from True_Treasure import STORY_STAGES, ENDINGS, POINTS, SCORE_LABELS_EN, get_final_ending

# --- Streamlitの設定とCSSの読み込み ---

st.set_page_config(
    page_title="True Treasure",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSSの読み込み
# setting.py 内の修正案
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"{file_name} not found. Please check if the file exists.")


# --- ゲームの状態初期化 ---

if 'game_state' not in st.session_state:
    st.session_state.game_state = 'start' # 'start', 'playing', 'ending'
    st.session_state.current_stage = 1
    st.session_state.player_name = ''
    st.session_state.scores = {
        "Wisdom": 0,
        "Courage": 0,
        "Kindness": 0,
        "Selfishness": 0,
    }


# --- 関数定義 ---

def start_game():
    """ゲーム開始時の状態にリセット"""
    st.session_state.game_state = 'playing'
    st.session_state.current_stage = 1
    st.session_state.scores = {
        "Wisdom": 0,
        "Courage": 0,
        "Kindness": 0,
        "Selfishness": 0,
    }

def handle_choice(point_type):
    """選択肢が選ばれた時の処理"""
    if st.session_state.game_state != 'playing':
        return

    # スコアを加算
    st.session_state.scores[point_type] += 1
    
    # 次のステージへ、またはエンディングへ
    if st.session_state.current_stage < len(STORY_STAGES):
        st.session_state.current_stage += 1
    else:
        st.session_state.game_state = 'ending'

# --- UIコンポーネント ---

st.title("🗺️ True Treasure: An Adventure")

# サイドバーにスコアを表示
with st.sidebar:
    st.header("🏆 Your Current Scores")
    if st.session_state.game_state == 'playing' or st.session_state.game_state == 'ending':
        # スコアを降順にソートして表示
        sorted_scores = sorted(st.session_state.scores.items(), key=lambda item: item[1], reverse=True)
        for attribute, score in sorted_scores:
            st.markdown(f"""
                <div class="score-card">
                    **{SCORE_LABELS_EN[attribute]}**: {score} Points
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Start the game to see your scores!")

# --- メインゲームロジック ---

if st.session_state.game_state == 'start':
    # スタート画面
    st.markdown("Welcome, brave soul, to the quest for the **True Treasure**!")
    st.markdown("Your choices will determine your destiny.")
    
    player_name = st.text_input("First, what is your name, Treasure Hunter?", key="name_input")
    
    if st.button("Start Adventure"):
        if player_name:
            st.session_state.player_name = player_name
            start_game()
            st.rerun()
        else:
            st.warning("Please enter your name to start.")

elif st.session_state.game_state == 'playing':
    # ゲームプレイ画面
    stage_key = st.session_state.current_stage
    story = STORY_STAGES.get(stage_key)

    if story:
        st.subheader(f"Stage {stage_key}:")
        # プレイヤー名を挿入してストーリーを表示
        story_text = story["text"].replace("You are", f"{st.session_state.player_name}, you are")
        st.markdown(f"**{story_text}**")
        

        # 選択肢の表示
        for choice_text, point_type in story["choices"].items():
            # point_type（例: "Wisdom"）から日本語ラベル（例: "知恵"）を取得
            point_label = POINTS[point_type] 
            
            # ボタンのラベルにポイントの種類を英語でヒントとして追加
            button_label = f"[{point_type}] {choice_text}"
            
            # ボタンが押されたらhandle_choiceをコールバックとして実行
            if st.button(button_label, key=f"choice_{stage_key}_{point_type}"):
                handle_choice(point_type)
                st.rerun() # 状態が変わったら画面を更新
    else:
        st.error("Error: Story stage not found.")
        st.button("Restart Game", on_click=start_game)


elif st.session_state.game_state == 'ending':
    # エンディング画面
    final_key = get_final_ending(st.session_state.scores)
    ending = ENDINGS[final_key]
    
    st.subheader("🎉 FINAL RESULT 🎉")
    st.markdown(f"**{st.session_state.player_name}**, the adventure has concluded.")
    
    st.header(f"✨ {ending['title']} ✨")
    st.markdown(f"<p style='font-size: 1.2em; text-align: center;'>{ending['text']}</p>", unsafe_allow_html=True)
    

    st.markdown("---")
    st.subheader("Your Journey Score Breakdown:")
    
    # 最終スコアを再度表示
    final_scores = sorted(st.session_state.scores.items(), key=lambda item: item[1], reverse=True)
    for attribute, score in final_scores:
        st.info(f"**{SCORE_LABELS_EN[attribute]}**: {score} Points")

    st.markdown("---")
    if st.button("Play Again?"):
        st.session_state.game_state = 'start'
        st.rerun()