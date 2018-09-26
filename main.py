import argparse, os
from ParagraphGenerator import ParagraphGenerator

"""parsing and configuration"""
def parse_args():
    desc = "Paragraph generator"
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--dataset', type=str, help='The name of dataset')
    parser.add_argument('--P', type=int, default=2, help='The length of prefix')
    parser.add_argument('--N', type=int, default=1, help='The number of paragraphs')

    return parser.parse_args()

"""main"""
def main():
    # parse arguments
    args = parse_args()
    if args is None:
        exit()

    generator = ParagraphGenerator(args)
    sentences, prefix_cnt = generator.generate()
    for s in sentences:
        print(s)
    print('number of unique prefix phrases = {}'.format(prefix_cnt))


if __name__ == '__main__':
    main()
