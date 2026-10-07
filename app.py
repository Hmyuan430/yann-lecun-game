import streamlit as st

st.set_page_config(page_title="杨立昆的人生岔路口", page_icon="🤖", layout="centered")

questions = [
    {
        'title': '第1题：1980年代，AI寒冬',
        'scene': '你是年轻的杨立昆，在贝尔实验室研究神经网络。但全世界都说神经网络是骗局，没有经费、没有认可。',
        'options': {
            'A': '转行做当时主流的符号主义AI，更容易发论文、拿经费。',
            'B': '继续死磕神经网络，哪怕被嘲笑“顽固的蠢货”。'
        },
        'correct': 'B',
        'result_A': '你可能成为主流学者，但神经网络这条线就少了一个坚守者。也许就不会有CNN，今天的刷脸支付、自动驾驶可能晚来很多年。',
        'result_B': '你选择了和杨立昆一样的路。他后来做出了LeNet，让机器学会了“看”。'
    },
    {
        'title': '第2题：2013年，扎克伯格邀请',
        'scene': '你在纽约大学当教授，学术安稳。扎克伯格请你创立FAIR，去工业界。',
        'options': {
            'A': '留在大学，稳稳当教授，不冒险。',
            'B': '去Meta，创立FAIR，但可能被公司战略绑架。'
        },
        'correct': 'B',
        'result_A': '你会安稳一生，但可能错过工业界的大规模资源，深度学习的工业落地可能慢一些。',
        'result_B': '你选择了和杨立昆一样的路。他去了Meta，创立FAIR，并放话“你不能指挥像我这样的研究员做什么”。'
    },
    {
        'title': '第3题：2025年，大模型席卷全球',
        'scene': '全世界都在卷大模型，Meta也全力押注。但你认为大模型是死胡同。',
        'options': {
            'A': '跟着公司走，闷声发大财。',
            'B': '公开唱反调，说大模型是死胡同，然后65岁离职创业。'
        },
        'correct': 'B',
        'result_A': '你会成为大模型浪潮的受益者，但可能违背自己的技术判断，继续做一个自己都不相信的方向。',
        'result_B': '你选择了和杨立昆一样的路。他离开Meta，创立AMI Labs，两个月融资10.3亿美元。'
    }
]

if 'step' not in st.session_state:
    st.session_state.step = 'welcome'
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False
if 'choice' not in st.session_state:
    st.session_state.choice = None

if st.session_state.step == 'welcome':
    st.title("🤖 杨立昆的人生岔路口")
    st.write("如果你是他，你会怎么选？")
    if st.button("开始选择"):
        st.session_state.step = 'game'
        st.session_state.q_index = 0
        st.session_state.show_feedback = False
        st.rerun()

elif st.session_state.step == 'game':
    q = questions[st.session_state.q_index]
    st.header(q['title'])
    st.write(q['scene'])
    if not st.session_state.show_feedback:
        choice = st.radio("你的选择：", ['A', 'B'], format_func=lambda x: f"{x}. {q['options'][x]}")
        if st.button("提交选择"):
            st.session_state.choice = choice
            st.session_state.show_feedback = True
            st.rerun()
    else:
        if st.session_state.choice == q['correct']:
            st.success(f"✅ 你和杨立昆选的一样！他选了 {q['correct']}。")
            st.info(q[f'result_{q["correct"]}'])
        else:
            st.warning(f"⚠️ 你选了 {st.session_state.choice}，但杨立昆选了 {q['correct']}。")
            st.info(q[f'result_{st.session_state.choice}'])
            st.write(f"**杨立昆的真实选择**：{q['correct']}。{q[f'result_{q["correct"]}']}")
        if st.button("下一题"):
            if st.session_state.q_index < len(questions) - 1:
                st.session_state.q_index += 1
                st.session_state.show_feedback = False
                st.session_state.choice = None
                st.rerun()
            else:
                st.session_state.step = 'summary'
                st.rerun()

elif st.session_state.step == 'summary':
    st.title("你的人生选择完成！")
    st.write("杨立昆这一生，每一次都选了难走的那条路。")
    st.balloons()