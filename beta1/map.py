class pole:

    def __init__(self):
        self.mas_cr()
        self.print_mas()

    def mas_cr(self):
        self.a = int(input("enter size map"))
        self.mas1 = []

        for i in range(self.a):
            self.mas1.append([])
            for j in range(self.a):
                self.mas1[i].append(' ')

    def print_mas(self):
        mas = ''
        for i in self.mas1:
            for i in i:
                mas += str(i) + '  '
            print(mas)
            mas = ''
