import random
import sys

def restart(point,diler_point,money):
	print('Your points: ',point,"Diler's point:  ",diler_point,'\n')
	if money < 1:
			print('################   GAMEOVER   ################')
			exit()
	restart_choose = input('Want to restart? y/n:  ')
	if (restart_choose == 'y'):
		point = 0
		diler_point = 0
		gaming_cards = list_of_cards[:]
		count_of_card = 0
		bet = 0
		cardstring = ''
		list_of_player_card = []
		list_of_diler_card = []
		game(point,diler_point,choose,count_of_card,bet,money,cardstring,list_of_player_card,list_of_diler_card,gaming_cards)
	else:
		print ('bye');exit()
	return NULL

#hearts tiles - буби clovers - крести pikes
list_of_cards = ['2h','3h','4h','5h','6h','7h','8h','9h','Jh','Qh','Kh','Ah',
				'2t','3t','4t','5t','6t','7t','8t','9t','Jt','Qt','Kt','At',
				'2c','3c','4c','5c','6c','7c','8c','9c','Jc','Qc','Kc','Ac',
				'2p','3p','4p','5p','6p','7p','8p','9p','Jp','Qp','Kp','Ap']

value_of_card = {'2h':2,'3h':3,'4h':4,'5h':5,'6h':6,'7h':7,'8h':8,'9h':9,'Jh':10,'Qh':10,'Kh':10,'Ah':1,
				'2t':2,'3t':3,'4t':4,'5t':5,'6t':6,'7t':7,'8t':8,'9t':9,'Jt':10,'Qt':10,'Kt':10,'At':1,
				'2c':2,'3c':3,'4c':4,'5c':5,'6c':6,'7c':7,'8c':8,'9c':9,'Jc':10,'Qc':10,'Kc':10,'Ac':1,
				'2p':2,'3p':3,'4p':4,'5p':5,'6p':6,'7p':7,'8p':8,'9p':9,'Jp':10,'Qp':10,'Kp':10,'Ap':1}

#money = sys.argv[-1]
#print (sys.argv)
cardstring = ''
choose = ''
point = 0
diler_point = 0
#diler_flag = False
gaming_cards = list_of_cards[:] #copy for game
list_of_player_card = []
list_of_diler_card = []
money = 1000
bet = 0
card = 0 
count_of_card = 0
count_of_diler_card = 0
rand_diler_card = random.randint(0,len(gaming_cards) - 1)#diler
first_diler_card = gaming_cards[rand_diler_card]
list_of_diler_card.append(first_diler_card)
diler_point += value_of_card[first_diler_card]
gaming_cards.pop(rand_diler_card)


def game(point,diler_point,choose,count_of_card,bet,money,cardstring,list_of_player_card,list_of_diler_card,gaming_cards):
	try:
		bet = abs(int(input('Your bet:   ')))
		money -= bet
		print('Money:  ',money)
		while choose !='q':
			choose = input('Show or pick - 1, Pass - 2:  ')
			if (choose == '1') and (count_of_card < 3):
				count_of_card += 1
				rand_card = random.randint(0,len(gaming_cards) - 1)
				card = gaming_cards[rand_card]
				list_of_player_card.append(card)
				cardstring = " ".join(list_of_player_card)
				print('Your card:   ',cardstring.upper())
				gaming_cards.pop(rand_card)
				print("Diler's card:  ",first_diler_card.upper())
				point = point + value_of_card[card]
				if (point < 9) and ((card == 'Ah') or( card == 'At') or (card== 'Ac') or (card == 'Ap')):
					A_choose = input('1 or 11\n')
					if A_choose == '1':
						point = point + value_of_card[card] #+1 from dic
					if A_choose == '11':
						point = point - value_of_card[card]
						point += 11
				if point > 21:
					print('Your points: ',point)
					print('################   YOU LOSE   ################') 
					print('Money:  ',money)
					restart(point,diler_point,money)
				if point == 21:
					print('-' *10, 'BLACKJACK', '-'*10)
					choose = '2'
				print('Points: ',point)

			if (choose == '2') or (count_of_card >=3):
				#  = True
				while True:
					rand_card = random.randint(0,len(gaming_cards) - 1)
					card = gaming_cards[rand_card]
					list_of_diler_card.append(card)
					cardstring = " ".join(list_of_diler_card)
					print("Diler's card:   ",cardstring.upper())
					#print("Diler's card:  ",gaming_cards[rand_card].upper())
					gaming_cards.pop(rand_card)
					diler_point += value_of_card[card]
					if (diler_point < 9) and ((card == 'Ah') or( card == 'At') or (card== 'Ac') or (card == 'Ap')):
						diler_point += 11
						print (diler_point)
					if (diler_point > point) and (diler_point < 21):
						print('################   YOU LOSE   ################')
						print('Money:  ',money)
						restart(point,diler_point,money)
					if (diler_point >= 16) and (diler_point < 21):
						print('Your points: ',point,'\n','Diler point:  ',diler_point,'\n')
						if (diler_point < point) and (point != 21):
							print('################   YOU WIN   ################')
							money += bet + bet
							print('Money:  ',money)
							restart(point,diler_point,money)
						if (diler_point < point) and (point != 21):
							print('################   YOU WIN   ################')
							money = money + bet + 1.5*bet
							print('Money:  ',money)
							restart(point,diler_point,money)
						if (diler_point > point):
							print('################   YOU LOSE   ################')
							print('Money:  ',money)
							restart(point,diler_point,money)
						if diler_point == point:
							print('################ DRAW ################')
							money += bet
							print('Money:  ',money)
							restart(point,diler_point,money)
					if diler_point > 21:
						print('################   YOU WIN   ################')
						money += bet + bet
						print('Money:  ',money)
						restart(point,diler_point,money)
					if (diler_point == 21):
						print('################   DRAW   ################')
						money += bet
						print('Money:  ',money)
						restart(point,diler_point,money)
					if (diler_point == 21) and (point != 21):
						print('################   YOU LOSE   ################')
						print('Money:  ',money)
						restart(point,diler_point,money)
					#print ("Diler's point:  ",diler_point)
	except KeyboardInterrupt:
		exit()
if __name__ == "__main__":
	game(point,diler_point,choose,count_of_card,bet,money,cardstring,list_of_player_card,list_of_diler_card,gaming_cards)
