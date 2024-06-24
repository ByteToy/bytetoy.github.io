# 荆州光睿高级中学-信息技术课程-教师：张鸿雁
# 第四单元第三小节课程演示代码
# 为了便于讲解，步骤分的比较细，定义方法较多

import pandas as pd
from prettytable import PrettyTable
import os


class Sudoku:
    def __init__(self, file_path):
        self.data = None
        self.blank = None
        self.file_path = file_path

    def load(self):
        dataframe = pd.read_csv(self.file_path, sep=',', header=None)
        dataframe.fillna(0, inplace=True)
        for i in range(9):
            dataframe[i] = dataframe[i].astype(int)
        self.data = dataframe.values

    def show_table(self):
        # os.system("cls")
        tb = PrettyTable(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        for i in range(9):
            tb.add_row(self.data[i])
        print(tb)

    def search_blank(self):
        blank_list = []
        for r in range(9):
            for c in range(9):
                if self.data[r][c] == 0:
                    blank_list.append([r, c])
        self.blank = blank_list
        return blank_list

    # pos是一个list，定义了表格的row和col
    # 验证一个数num在对应的区块中是否符合规则
    def block_valid(self, num, pos):
        row_start = (pos[0] // 3) * 3
        col_start = (pos[1] // 3) * 3
        row_end = row_start + 2
        col_end = col_start + 2
        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                # print(r, c, self.data[r][c])
                if num == self.data[r][c]:
                    return False
        return True

    def row_valid(self, num, pos):
        for c in range(9):
            # print(pos[0], c, self.data[pos[0]][c])
            if num == self.data[pos[0]][c]:
                return False
        return True

    def col_valid(self, num, pos):
        for r in range(9):
            # print(r, pos[1], self.data[r][pos[1]])
            if num == self.data[r][pos[1]]:
                return False
        return True

    # 使用回溯算法解数独
    def backtrace(self):
        if len(self.blank) == 0:
            self.show_table()
            return True
        else:
            for num in range(1, 10, 1):
                pos = self.blank[-1]
                if self.block_valid(num, pos) and self.row_valid(num, pos) and self.col_valid(num, pos):
                    self.data[pos[0]][pos[1]] = num
                    # self.show_table()
                    self.blank.pop()
                    if self.backtrace():
                        return True
                    self.data[pos[0]][pos[1]] = 0
                    self.blank.append(pos)
        return False


if __name__ == "__main__":
    sudoku = Sudoku("s2.csv")
    # 1.读取文件
    data = sudoku.load()

    # 2.显示数独表格
    sudoku.show_table()

    # 3. 搜索数独表格中为空（即为0）的列表下标，并计算空格的数量
    sudoku.search_blank()
    # print(sudoku.search_blank())
    # print(len(sudoku.search_blank()))

    # 4.验证块的九宫格是否成立
    # print(sudoku.block_valid(7,[0,1]))

    # 5.验证行是是否成立
    # print(sudoku.row_valid(3,[8,0]))

    # 6.验证列是否成立
    # print(sudoku.col_valid(9,[1,1]))

    # 7.解数独
    sudoku.backtrace()
