import streamlit as st

st.set_page_config(page_title="杨立昆的人生岔路口", page_icon="🤖", layout="centered")

# ========== 题目数据 ==========
questions = [
    {
        'title': '第1关：1980年代，AI寒冬',
        'scene': '你是年轻的杨立昆，在贝尔实验室研究神经网络。但全世界都说神经网络是骗局，没有经费、没有认可。',
        'options': {
            'A': '转行做当时主流的符号主义AI，更容易发论文、拿经费。',
            'B': '继续死磕神经网络，哪怕被嘲笑“顽固的蠢货”。'
        },
        'correct': 'B',
        'result_A': '你可能成为主流学者，但神经网络这条线就少了一个坚守者。也许就不会有CNN，今天的刷脸支付、自动驾驶可能晚来很多年。',
        'result_B': '你选择了和杨立昆一样的路。他后来做出了LeNet，让机器学会了“看”。没有他这次死磕，今天的人脸识别、医学影像、自动驾驶，可能都还是科幻片。'
    },
    {
        'title': '第2关：1990年代，拒绝高盛',
        'scene': '你在贝尔实验室做出LeNet后，华尔街高盛开出天价邀请你去做量化交易。',
        'options': {
            'A': '去高盛，赚大钱。',
            'B': '留在学术界，继续搞神经网络。'
        },
        'correct': 'B',
        'result_A': '你会成为华尔街的量化精英，收入翻几十倍。但CNN这条技术路线可能就此中断，深度学习在工业界的落地会慢很多年。',
        'result_B': '你选择了和杨立昆一样的路。他留在学术界，继续深耕神经网络，后来加入纽约大学，培养了一批深度学习人才。他放弃了短期财富，换来了AI革命的技术基础。'
    },
    {
        'title': '第3关：2013年，扎克伯格邀请',
        'scene': '你在纽约大学当教授，学术安稳。扎克伯格请你创立FAIR，去工业界。',
        'options': {
            'A': '留在大学，稳稳当教授，不冒险。',
            'B': '去Meta，创立FAIR，但可能被公司战略绑架。'
        },
        'correct': 'B',
        'result_A': '你会安稳一生，论文照发、职称照升。但可能错过工业界的大规模算力和数据，深度学习的工业落地可能慢很多年。',
        'result_B': '你选择了和杨立昆一样的路。他去了Meta，创立FAIR，并放话“你不能指挥像我这样的研究员做什么”。他借助工业界资源，推动了深度学习的爆发。'
    },
    {
        'title': '第4关：拒绝麦肯锡',
        'scene': '麦肯锡请你去做商业咨询，年薪极高，工作光鲜。',
        'options': {
            'A': '去麦肯锡，走商业路线。',
            'B': '去Meta，搞基础研究。'
        },
        'correct': 'B',
        'result_A': '你会成为商业精英，西装革履、全球出差。但AI基础研究可能少了一个最重要的推动者。',
        'result_B': '你选择了和杨立昆一样的路。他选择了基础研究，而不是商业咨询。今天Meta的AI实力，很大程度建立在他当年打下的基础上。'
    },
    {
        'title': '第5关：面对同行嘲笑',
        'scene': 'AI寒冬时期，同行嘲笑你是“顽固的蠢货”，说神经网络永远不可能成功。',
        'options': {
            'A': '放弃神经网络，转行。',
            'B': '不理嘲笑，继续死磕。'
        },
        'correct': 'B',
        'result_A': '你会轻松很多，不用再被人嘲笑。但神经网络这条线可能就此断了，深度学习革命可能永远不会发生。',
        'result_B': '你选择了和杨立昆一样的路。他顶住了整个学界的质疑，坚持了十几年。2018年，他拿到了图灵奖。那些曾经嘲笑他的人，后来都在用他的技术。'
    },
    {
        'title': '第6关：2025年，大模型席卷全球',
        'scene': '全世界都在卷大模型，Meta也全力押注。但你认为大模型是死胡同。',
        'options': {
            'A': '跟着公司走，闷声发大财。',
            'B': '公开唱反调，说大模型是死胡同，然后65岁离职创业。'
        },
        'correct': 'B',
        'result_A': '你会成为大模型浪潮的受益者，股票期权拿满。但你可能违背自己的技术判断，继续做一个自己都不相信的方向。',
        'result_B': '你选择了和杨立昆一样的路。他离开Meta，创立AMI Labs，两个月融资10.3亿美元。65岁，用真金白银证明自己。他这一生，都在逆流。'
    }
]

# ========== 状态初始化 ==========
if 'step' not in st.session_state:
    st.session_state.step = 'welcome'
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False
if 'choice' not in st.session_state:
    st.session_state.choice = None
if 'passed' not in st.session_state:
    st.session_state.passed = 0

# ========== 页面路由 ==========
if st.session_state.step == 'welcome':
    st.title("🤖 杨立昆的人生岔路口")
    st.write("如果你是他，你会怎么选？")
    st.write("共6关，选对进入下一关，选错从头再来。")
    if st.button("开始闯关"):
        st.session_state.step = 'game'
        st.session_state.q_index = 0
        st.session_state.show_feedback = False
        st.session_state.choice = None
        st.session_state.passed = 0
        st.rerun()

elif st.session_state.step == 'game':
    q = questions[st.session_state.q_index]
    st.header(q['title'])
    st.progress((st.session_state.q_index) / len(questions))
    st.write(q['scene'])
    
    if not st.session_state.show_feedback:
        # 未提交状态：显示选项
        choice = st.radio("你的选择：", ['A', 'B'], format_func=lambda x: f"{x}. {q['options'][x]}")
        if st.button("提交选择"):
            st.session_state.choice = choice
            st.session_state.show_feedback = True
            st.rerun()
    else:
        # 已提交状态：显示反馈
        if st.session_state.choice == q['correct']:
            # 选对：显示正反馈，进入下一题
            st.success(f"✅ 恭喜通关！你和杨立昆选的一样。")
            st.info(q[f'result_{q["correct"]}'])
            if st.session_state.q_index < len(questions) - 1:
                if st.button("进入下一关"):
                    st.session_state.q_index += 1
                    st.session_state.show_feedback = False
                    st.session_state.choice = None
                    st.rerun()
            else:
                if st.button("查看最终结果"):
                    st.session_state.step = 'win'
                    st.rerun()
        else:
            # 选错：游戏结束，展示两个选项的后果
            st.error(f"❌ 游戏结束！你选了 {st.session_state.choice}，但杨立昆选了 {q['correct']}。")
            st.write("**你的选择意味着什么：**")
            st.warning(q[f'result_{st.session_state.choice}'])
            st.write("**杨立昆的选择意味着什么：**")
            st.success(q[f'result_{q["correct"]}'])
            if st.button("重新开始"):
                st.session_state.step = 'game'
                st.session_state.q_index = 0
                st.session_state.show_feedback = False
                st.session_state.choice = None
                st.session_state.passed = 0
                st.rerun()

elif st.session_state.step == 'win':
    st.balloons()
    st.title("🏆 通关！")
    st.write("你完整走完了杨立昆的逆流之路！")
    st.write("他这一生，每一次都选了难走的那条路。")
    st.write("不是因为他不知道哪条路容易，而是因为他知道，容易的路，通往不了真正的智能。")
    st.write("——杨立昆")
    if st.button("再玩一次"):
        st.session_state.step = 'game'
        st.session_state.q_index = 0
        st.session_state.show_feedback = False
        st.session_state.choice = None
        st.session_state.passed = 0
        st.rerun()
