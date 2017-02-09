#!/usr/bin/python
# Maze solver menggunakan algoritma backtracking
# Mohammad Irsyad Fauzan
# 09 Feb 2017

import sys

class MazeSolver:
    def __init__(self, nama_file):
        self.labirin = []
        self.lebar = 0
        self.panjang = 0
        self.solusi = []
        self.dilewati =[]
        self.start = []
        self.finish = []

        self.baca_maze(nama_file)
        self.solve()

    def baca_maze(self, nama_file):
        f = open(nama_file, 'r')
        for baris in f:
            lst = []
            for kolom in baris:
                if kolom == '#':
                    lst.append(0)
                elif kolom == ' ':
                    lst.append(1)
            self.labirin.append(lst)

        self.panjang = len(self.labirin)
        self.lebar = len(self.labirin[0])
        self.cari_start()
        self.cari_finish()

    def cari_start(self):
        i = 0
        ketemu = False
        # Cari Di Sumbu X
        for x in self.labirin[0]:
            if x == 1:
                ketemu = True
                self.start = [0, i]
                break
            i += 1

        # Cari di Sumbu Y
        i = 0
        for y in range(0, len(self.labirin)):
            if self.labirin[y][0] == 1:
                self.start =  [i, 0]
                break
            i += 1

    def cari_finish(self):
        i = 0
        ketemu = False
        # Cari Di Sumbu X
        for x in self.labirin[-1]:
            if x == 1:
                ketemu = True
                self.finish = [len(self.labirin) - 1, i]
                break
            i += 1

        # Cari di Sumbu Y
        i = 0
        for y in range(0, len(self.labirin)):
            if self.labirin[y][len(self.labirin[y]) - 1] == 1:
                self.finish = [y, len(self.labirin[y]) - 1]
                break
            i += 1

    def cari_jalan(self, x, y):
        if [y, x] == self.finish:
            self.solusi.append([y, x])
            self.tampil_solusi()
        else:
            if (y - 1 > 0) and (([y - 1, x] not in self.dilewati) and (self.labirin[y - 1][x] > 0)): # Ke Atas
                self.solusi.append([y, x])
                self.dilewati.append([y - 1, x])
                self.cari_jalan(x, y - 1)

            elif (y + 1 < self.panjang) and (([y + 1, x] not in self.dilewati) and (self.labirin[y + 1][x] > 0)): # Ke Bawah
                self.solusi.append([y, x])
                self.dilewati.append([y + 1, x])
                self.cari_jalan(x, y + 1)

            elif (x + 1 < self.lebar) and (([y, x + 1] not in self.dilewati) and (self.labirin[y][x + 1] > 0)): # Ke Kanan
                self.solusi.append([y, x])
                self.dilewati.append([y, x + 1])
                self.cari_jalan(x + 1, y)

            elif (x - 1 > 0) and (([y, x - 1] not in self.dilewati) and (self.labirin[y][x - 1] > 0)): # Ke Kiri
                self.solusi.append([y, x])
                self.dilewati.append([y, x - 1])
                self.cari_jalan(x - 1, y)

            else:
                if len(self.solusi) > 0:
                    sebelum = self.solusi.pop()
                    self.cari_jalan(sebelum[1], sebelum[0]) # Backtrack
                else:
                    print "Solusi Tidak Ditemukan"

    def solve(self):
        start = self.start
        self.cari_jalan(start[1], start[0])

    def tampil_solusi(self):
        for br in range(0, self.panjang):
            for kl in range(0, self.lebar):
                if [br, kl] in self.solusi:
                    sys.stdout.write(".")
                else:
                    if self.labirin[br][kl] == 0:
                        sys.stdout.write("#")
                    elif self.labirin[br][kl] == 1:
                        sys.stdout.write(" ")
            sys.stdout.write("\n")

s = MazeSolver('maze.txt')