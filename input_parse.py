# -*- coding: utf-8 -*-
# @Time : 2020/4/20 14:48
# @Author : zls
# @File : input_parse.py
# @Software: PyCharm
import argparse


def main():
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('-n', '--name', default=' Li ')
    parser.add_argument('-y', '--year', default='20')
    args = parser.parse_args()
    # print(args)
    name = args.name
    year = args.year
    print('Hello {}  {}'.format(name, year))
    # python input_parse.py -n zls -y 25
    # Hello zls  25


if __name__ == '__main__':
    main()
