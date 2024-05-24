class Puma:
    def __init__(self):
        self.p1_rotation = 0.0
        self.p2_rotation = 90.0
        self.p3_rotation = 90.0
        self.p4_rotation = 0.0
    def p1_spin_left(self):
        if self.p1_rotation == 359.0:
            self.p1_rotation = 0
        else:
            self.p1_rotation = self.p1_rotation + 1
    def p1_spin_right(self):
        if self.p1_rotation == 0.0:
            self.p1_rotation = 359
        else:
            self.p1_rotation = self.p1_rotation - 1
    def p2_spin_forward(self):
        if self.p2_rotation == 180.0:
            print('Nie mozesz')
        else:
            self.p2_rotation = self.p2_rotation + 1
    def p2_spin_backward(self):
        if self.p2_rotation == 0.0:
            print('Nie mozesz')
        else:
            self.p2_rotation = self.p2_rotation - 1
    def p3_spin_forward(self):
        if self.p3_rotation == 180.0:
            print('Nie mozesz')
        else:
            self.p3_rotation = self.p3_rotation + 1
    def p3_spin_backward(self):
        if self.p3_rotation == 0.0:
            print('Nie mozesz')
        else:
            self.p3_rotation = self.p3_rotation - 1
    def p4_catch(self):
        pass
    def p4_release(self):
        pass
    def show_positions(self):
        print(self.p1_rotation,' ',self.p2_rotation,' ',self.p3_rotation,' ',self.p4_rotation)