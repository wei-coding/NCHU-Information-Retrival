import argparse
import utils.index

def main(args):
    result = utils.index.retrieve_wiki(args.query, args.db)
    for r in result:
        print(*r, end=' ')

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("query", type=str)
    argparser.add_argument("db", type=str, choices=["mydb.db", "myjieba.db"])
    args = argparser.parse_args()
    main(args)