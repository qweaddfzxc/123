user1 = int(input("請輸入：剪刀：（0）、石頭（1）、布（2）->"))
import random
computer = random.randint(0,2)
if user1 == computer:
    if user1==0:
        print("你的輸入為：剪刀（0）")
        print("隨機生成數字為：0")
    elif user1==1:
        print("你的輸入為：石頭（1）");
        print("隨機生成數字為：1");
    else:
        print("你的輸入為：布（2）");
        print("隨機生成數字為：2");
    print("啊哈，是平局！");
elif user1 == 0 and computer == 1:
    print("你的輸入為：剪刀（0）");
    print("隨機生成數字為：1");
    print(("哈哈，你輸了"));
elif user1 == 0 and computer == 2:
    print("你的輸入為：剪刀（0）");
    print("隨機生成數字為：2");
    print(("恭喜你贏啦！"));
elif user1 == 1 and computer == 0:
    print("你的輸入為：石頭（1）");
    print("隨機生成數字為：0");
    print(("恭喜你贏啦！"));
elif user1 == 1 and computer == 2:
    print("你的輸入為：石頭（1）");
    print("隨機生成數字為：2");
    print(("哈哈，你輸了"));
elif user1 == 2 and computer == 0:
    print("你的輸入為：布（2）");
    print("隨機生成數字為：0");
    print(("哈哈，你輸了"));
elif user1 == 2 and computer == 1:
    print("你的輸入為：布（2）");
    print("隨機生成數字為：1");
    print(("恭喜你贏啦"));
