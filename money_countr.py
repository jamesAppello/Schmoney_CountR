class ShmoneyCounter:
    # global hundo_countr, fifT_countr, twenT_countr, ten_countr, five_countr, one_countr
    def __init__(self):
        print('''
         _________           ________          __________      ___________________     ______    ______     ____________  ___       ____
        ^    _.^   \       |          \        /          |    |                   |   |      \  |      |   |    ________|\   \     /   / 
        (   (  )     |     |           \      /           |    |     _________     |   |       \ |      |   |   |          \   \   /   /
        \__)   |    |      |            \    /            |    |    |         |    |   |        \|      |   |   |____       \   \./   /
               |    |      |             \__/             |    |    |         |    |   |         \      |   |    ____|       \       / 
               |____|      |      |\             /|       |    |    |         |    |   |      |\        |   |   |             |     |
                ____       |      | \           / |       |    |    |_________|    |   |      | \       |   |   |_______      |     |     
               |    |      |      |  \         /  |       |    |                   |   |      |  \      |   |___________|     |     |
               |____|      |______|   \_______/   |_______|    |___________________|   |______|   \_____|                     |_____|                    


        ''')
        a_hundos = input("Amount of 100_NOTES::")
        a_fifTies = input("Amount of 50_NOTES::")
        a_twenTies = input("Amount of 20_NOTES::")
        a_tens = input("Amount of 10_NOTES::")
        a_fives = input("Amount of 5_NOTES::")
        a_singles = input("Amount of 1_NOTES::")
        print("calculating.........\n\n")
        print("100s.............", int(self.hundo_countr(a_hundos)))
        print("50s..............", int(self.fifT_countr(a_fifTies)))
        print("20s..............", int(self.twenT_countr(a_twenTies)))
        print("10s..............", int(self.ten_countr(a_tens)))
        print("5s...............", int(self.five_countr(a_fives)))
        print("1s...............", int(self.one_countr(a_singles)))
        print("----------------------------------------------------\n")
        print("TOTAL::", int(self.hundo_countr(a_hundos) + 
        self.fifT_countr(a_fifTies) + 
        self.twenT_countr(a_twenTies) +
        self.ten_countr(a_tens) +
        self.five_countr(a_fives) +
        self.one_countr(a_singles)))

    # amount of 100s
    def hundo_countr(self, h):
        return int(int(h)*100)
    # amount of 50s
    def fifT_countr(self, f):
        return int(int(f)*50)
    # amount of 20s
    def twenT_countr(self, t):
        return int(int(t)*20)
    # amount of 10s
    def ten_countr(self,x):
        return int(int(x)*10)
    # amount of 5s
    def five_countr(self, ph):
        return int(int(ph)*5)
    # amount of 1s
    def one_countr(self,o):
        return int(int(o)*1)

mc1 = ShmoneyCounter()