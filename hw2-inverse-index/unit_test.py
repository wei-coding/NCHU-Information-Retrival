from utils import splitter, index
import os

if __name__ == "__main__":
    # s = ["今天天氣真好"]
    # mysplitter = splitter.Splitter('D:\\Projects\\NCHU-Information-Retrival\\hw2-inverse-index\\data', cuda=True)
    # print(mysplitter.split(s))
    # index.reverse_index()
    index.retrieve_wiki("人心惶惶")