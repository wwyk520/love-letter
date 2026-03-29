import streamlit as st
import time

#初始化
if"step"not in st.session_state:
    st.session_state["step"]=0

# —————————————— 页面设置 ——————————————
st.set_page_config(
    page_title="给你的一封信",
    page_icon="✉️",
    layout="centered"
)

# —————————————— 样式美化 ——————————————
st.markdown("""
<style>
body {
    background-color: #fdf6f8;
    font-family: "Microsoft YaHei";
}
.title {
    font-size: 35px;
    text-align: center;
    color: #c75c7f;
    font-weight: bold;
}
.letter {
    font-size: 20px;
    line-height: 1.8;
    color: #555;
    padding: 20px;
    background: #fff8f9;
    border-radius: 15px;
}
.heart {
    font-size: 50px;
    text-align: center;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# —————————————— 初始化状态 ——————————————
if "step" not in st.session_state:
    st.session_state.step = 0  # 0=封面 1=输入指令 2=书信 3=小心脏 4=提问 5=结果
if "no_count" not in st.session_state:
    st.session_state.no_count = 0

# —————————————— 步骤0：封面 ——————————————
if st.session_state.step == 0:
    st.markdown('<div class="title">✉️ 一封给你的信 ✉️</div>', unsafe_allow_html=True)
    st.write("\n")
    if st.button("点击打开信封", use_container_width=True):
        st.session_state.step = 1
        st.rerun()

# —————————————— 步骤1：输入指令 ——————————————
elif st.session_state.step == 1:
    st.subheader("请输入指令才能打开信件")
    st.info("提示：指令是【打开看看】")
    cmd = st.text_input("输入指令：")

    if cmd == "打开看看":
        st.success("验证成功！正在为你打开信件...")
        time.sleep(1)
        st.session_state.step = 2
        st.rerun()
    elif cmd != "":
        st.error("指令不对哦～再试试！")

# —————————————— 步骤2：书信内容 ——————————————
elif st.session_state.step == 2:
    st.markdown('<div class="title">💌 我的心里话 💌</div>', unsafe_allow_html=True)
    st.write("\n")

    # ———— 这里写你自己的书信内容 ————
    st.markdown("""
<div class="letter">
武莹莹：<br><br>
其实我有很多话想对你说，却不知道从哪里开始。不知道你这周回去了吗？写这份信的时候我才发现，原来我们没联系也才两周，但我总觉得过了很久，像是两个月了，其实我有很多次想你，但倔强的我，总是一次又一次忍住了。还记得你那次说，我对你不是喜欢，只是不甘，我说，给我一些时间，在这些时间里，我常常问自己何为喜欢，我想，我想看见你笑的酒窝，我想和你牵着手去看花，我也想抱着你，在月光下相吻，而且这个人我希望的是你，这些都是我内心给我的答案，我开始觉得可能都是假的，但每次想你时，我又坚信这些都是真的，也许我还是不知道喜欢是什么，但想你都是真的，想见你也是真的。<br>
要是坦白说，第一次见面时，我的心里充斥着紧张和小心翼翼，其实那天我更想去你家里静静的陪你工作，但我连看你都不敢，更别提我敢说出那句陪你工作了。那天回去后，我开心的以为，我终于可以有个陪我的女朋友了。第二次见面，哇，好好看，但我依旧不知道怎么和你聊天，只能刻意的找话题，有一搭没一搭的聊。吃饭时，应该坐对面的，想坐她旁边，哎，算了算了，也许坐对面会让他反感呢？散步时，想牵她的手，但她手一直架着，好像不太给牵呢，算了算了，得礼貌，好想搂着她一点啊，但这么突然，她会不会反感推开啊，那以后岂不是面都见不了，算了算了。到楼下了，我想送她到门口，但她和我说拜拜了，应该不想让我送吧，好吧，算了算了。第三次见面，她扎了头发好好看啊，以后是我女朋友，我该好幸福啊，竟然真带了相机，待会看有没有好看的地方，想给她拍一张，走路时，好像这样也挺好的，牵手就慢慢来吧，应该会自然而然的碰上吧，吃饭时，我想坐她旁边，哎，但她放了衣服，好像又不太行，她好像一直在玩手机，是不是和我在一起很没意思，好像没看上我，更不敢碰她了。在地铁站口，哎，果然没看上我，想要抱抱时，我有点忐忑，我没抱过人。也没被抱过，姿势应该是什么样的，抱了，好像姿势不对吧，她会不会难受，她真的好可爱，想哭，哎，想找个地方？是我想的那个吗，还是我会想多，她只想找个地方和我多抱一会，我要是往那块想，但她不是这个意思，会不会好尴尬。亲我后，我就开始觉得一切都是梦，直到我晚上回到酒店后，才后知后觉，但我不知道为什么，那个时候我还会控制自己的生理反应，好像说的好听点是礼貌或绅士，但我知道就是我的胆小和怯懦，明明喜欢你，却不敢表达，总是畏头畏尾。<br>
内心的声音一直告诉我，让我再勇敢的尝试一次，这不是一时的兴起，而是无数次的心声让我这么做，我想你能否再给我一次机会，一次重新了解彼此的机会，我想晚上和你打视频，听你说话，也想见你，握紧你的手，与你拥抱，感受你舌尖的温度，也许你会觉得这些都在浪费时间，但哪怕这样只有一年甚至半年，我也愿意我的生命中，曾出现过你，在我这空白无奇的人生中画上浓妆艳抹的一笔，无论未来怎样，都会成为我一生最好的回忆，后果我也都愿意承担。<br><br>
我想随着春天的花一同开放，哪怕最后也躲不掉凋零！武莹莹这几天的答案是：我盛文凯心里一直有你，从未改变，我可以重新加回你的微信聊天权吗？<br>
</div>
""", unsafe_allow_html=True)

    st.write("\n")
    st.write("\n")

    # 小心脏按钮
    if st.button("看完后，点击一下吧！<span class='heart'>❤️</span>", use_container_width=True):
        st.session_state.step = 3
        st.rerun()

# —————————————— 步骤3：问题弹窗 ——————————————
elif st.session_state.step == 3:
    st.subheader("你是否愿意给我一次机会？")

    col1, col2 = st.columns(2)
    with col1:
        yes = st.button("愿意 ✅", use_container_width=True)
    with col2:
        no = st.button("不愿意 ❌", use_container_width=True)

    # 选择 是
    if yes:
        st.session_state.step = 5
        st.rerun()

    # 选择 否
    if no:
        st.session_state.no_count += 1
        if st.session_state.no_count == 1:
            st.warning("再想想呗～🥺")
        elif st.session_state.no_count >= 2:
            st.session_state.step = 6
            st.rerun()

# —————————————— 步骤5：选择是 → 花束礼炮 ——————————————
elif st.session_state.step == 5:
    st.balloons()  # 礼炮特效
    st.success("🎉 谢谢你愿意给我机会！我会好好珍惜！")
    st.image("https://pic.icons8.com/wp-content/uploads/202001/flowers-3.png")  # 花束
    st.stop()

# —————————————— 步骤6：第二次否 → 失望表情包 ——————————————
elif st.session_state.step == 6:
    st.image("https://pic.icons8.com/wp-content/uploads/201907/sad-1024x1024.png")
    st.subheader("好吧，我很想你。")
    st.stop()