#!/usr/bin/env python3
import argparse
import os
import re
import pathlib


def valid_target_dir(path_attr):
    path = pathlib.Path(path_attr)
    try:
        if path.is_dir():
            return path_attr
    except OSError:
        raise argparse.ArgumentTypeError('%s is not a valid directory' % (path,))


def valid_result_dir(path_attr):
    path = pathlib.Path(path_attr)
    try:
        if path.is_dir():
            return path_attr
        else:
            try:
                os.mkdir(path)
                return path_attr
            except OSError:
                raise argparse.ArgumentTypeError('%s cant create directory' % (path,))
    except OSError:
        raise argparse.ArgumentTypeError('%s is not a valid directory' % (path,))


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--withMonth', choices={"y", "n", "Y", "N"}, default="y")
    parser.add_argument('-t', '--targetPath', type=valid_target_dir, help='folder to sort', default='.')
    parser.add_argument('-r', '--resultPath', type=valid_result_dir, help='folder to save', default='./test')
    return parser.parse_args()
    # print(parser.parse_args())


def gerenerate_file_mask(fileName: str):
    # FileTypes = ('.jpg', '.mp4')
    if re.search(r'^\d{8}_\d{6}', fileName):
        return True


def generate_list_of_edit_files(directory: pathlib.Path):
    file_list = []  # A list for storing files existing in directories
    for x in directory.iterdir():
        if x.is_file() and gerenerate_file_mask(x.name):
            file_list.append(str(x))
        # else:
        # file_list.append(searching_all_files(directory / x))
    return file_list


def checkYearDir_orCreate(fileName):
    dirYearName = fileName[:4]
    valid_result_dir(args.resultPath + '/' + dirYearName)
    return dirYearName


def checkMothDir_orCreate(fileName):
    dirYearName = fileName[:4]
    dirMonthName = fileName[4:6]
    valid_result_dir(args.resultPath + '/' + dirYearName + '/' + dirMonthName)
    return dirMonthName


if __name__ == '__main__':
    args = init_args()
    file_list = generate_list_of_edit_files(pathlib.Path(args.targetPath))
    for fileName in file_list:
        dist_dir = args.resultPath + '/' + checkYearDir_orCreate(pathlib.Path(fileName).name)
        if args.withMonth in ('Yy'):
            dist_dir += '/' + checkMothDir_orCreate(pathlib.Path(fileName).name) + '/'
        pathlib.Path(args.targetPath + '/' + fileName).rename(dist_dir + pathlib.Path(fileName).name)
