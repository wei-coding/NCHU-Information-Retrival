import jieba

class Splitter:
    
    def __init__(self, data_path='./model', user_dict='./model'):
        jieba.set_dictionary(data_path+'/dict.txt.big')
        if user_dict:
            self._set_user_dict(user_dict+'/userdict.txt')
        # pass

    def _set_user_dict(self, user_dict):
        jieba.load_userdict(user_dict)

    def split(self, sentences):
        return jieba.cut(sentences)
