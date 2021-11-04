import argparse
import utils.retrieval as retri
import os

def main(args):
    if args.database and os.path.exists(args.database):
        retri.retrieve_wiki(args.query, args.database)
    elif args.database and not os.path.exists(args.database):
        raise Exception(f'Database {args.database} does not exist')
    else:
        retri.retrieve_wiki(args.query, 'myjieba.db')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('query', type=str)
    parser.add_argument('-d', '--database', type=str, required=False)
    args = parser.parse_args()
    main(args)