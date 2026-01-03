import game_data
import random

points = 0


def gen_influencer():
    number = random.randint(0, 19)
    influencer = game_data.data[number]
    print(f"{influencer['name']} , {influencer['description']} of {influencer['country']}")
    return influencer['follower_count'], influencer, number


def play(previous_influencer=None, previous_index=None):
    if previous_influencer:
        influencer_a = previous_influencer
        index_a = previous_index
        print(f"{influencer_a['name']} , {influencer_a['description']} of {influencer_a['country']}")
        a = previous_influencer['follower_count']
    else:
        a, influencer_a, index_a = gen_influencer()

    print("vs")
    b, influencer_b, index_b = gen_influencer()

    while index_a == index_b:
        b, influencer_b, index_b = gen_influencer()

    check_answer(a, b, influencer_a, influencer_b, index_a, index_b)


def check_answer(follower_count_a, follower_count_b, influencer_a, influencer_b, index_a, index_b):
    global points
    ans = input("who has more followers A or B ? :").lower()
    if ans == "a":
        if follower_count_a > follower_count_b:
            print("good")
            points += 1
            play(influencer_a, index_a)
        else:
            print(f"game_over! your total points : {points}")
    elif ans == "b":
        if follower_count_b > follower_count_a:
            print("good")
            points += 1
            play(influencer_b, index_b)
        else:
            print(f"game_over! your total points : {points}")


if __name__ == '__main__':
    play()