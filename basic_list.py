def make_list():
 z = []
 def get_input():
        for x in range(3):
           z.append(str(input("Enter your string:")))
        return z
 get_input()
if __name__ == '__main__':
     make_list()
