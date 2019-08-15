import argparse
from experiments import elapsed_time


def main():
    parser = argparse.ArgumentParser(description='Find elapsed time from input file or start and end date argument.')
    parser.add_argument('-f',
                        '--file',
                        dest="file_path",
                        type=str,
                        help="pass file path which contains list of experiment dates ex: 02/06/1983 - 22/06/1983\n04/07/1984 - 25/12/1984",
                        default="",
                        )
    parser.add_argument('-ed',
                        '--expdate',
                        dest="exp_date",
                        type=str,
                        help="pass experiement start and end date value ex: 02/06/1983 - 22/06/1983",
                        default="",
                        )
    args_obj = parser.parse_args()
    elapsed_time.process_data(args_obj)
