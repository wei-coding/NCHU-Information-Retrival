from utils import splitter
import os

if __name__ == "__main__":
    print(os.getcwd())
    s = ["今天天氣真好"]
    mysplitter = splitter.Splitter(True, 'D:\\Projects\\NCHU-Information-Retrival\\hw2-inverse-index\\data')
    print(mysplitter.split(s))