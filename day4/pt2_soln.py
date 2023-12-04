f = open("day4/input.txt", "r")

card_data = {}

card_occ = {}

i = 1

for line in f:
    parts = line.split('|')
    win_nums = [int(num) for num in parts[0].split(':')[1].strip().split(' ') if num]
    card_nums = [int(num) for num in parts[1].strip().split(' ') if num]
    card_data[i] = (win_nums, card_nums)
    card_occ[i] = 1
    i+=1
        

for card in sorted(card_data.keys()):
    wins, cards = card_data[card]
    matches = len([val for val in wins if val in cards])
    for next_card in range(card+1, card+1+matches):
        if next_card in card_data:
            card_occ[next_card] += card_occ[card]

print(sum(card_occ.values()))