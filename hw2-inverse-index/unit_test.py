from utils import retrieval

if __name__ == "__main__":
    # s = ["今天天氣真好"]
    # mysplitter = splitter.Splitter('D:\\Projects\\NCHU-Information-Retrival\\hw2-inverse-index\\data', cuda=True)
    # print(mysplitter.split(s))
    # index.reverse_index()
    retrieval.retrieve_wiki("人心惶惶", 'myjieba.db')