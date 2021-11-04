from utils import retrieval, index, jiebasplitter

if __name__ == "__main__":
    # s = "今天天氣真好"
    # mysplitter = jiebasplitter.Splitter()
    # print(','.join(mysplitter.split(s)))
    index.reverse_index(db='myjieba.db', jieba=True)
    # retrieval.retrieve_wiki("人心惶惶", 'myjieba.db')