import math, sys
from konlpy.tag import Okt

class BayesianFilter:
    # 베이시안 필터
    def __init__(self):
        self.words = set() # 출현한 단어의 기록
        self.word_dict = {} # 카테고리마다의 출현 횟수 기록
        self.category_dict = {} # 카테고리 출현 횟수 기록

    # 형태소 분석하기
    def split(Self, text):
        results = []
        okt = Okt()
        # 단어의 기본형 사용
        malist = okt.pos(text, norm=True, stem=True)
        for word in malist:
            if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                results.append(word[0])
        return results

    # 단어의 카테고리의 출현 횟수 세기
    def inc_word(self, word, category):
        #  카테고리 추가하기
        if not category in self.word_dict:
            self.word_dict[category] = {}
        # 카테고리에 단어 추가하기
        if not word in self.word_dict[category]:
            self.word_dict[category][word] = 0
        self.word_dict[category][word] += 1
        self.words.add(word)

    def inc_category(self, category):
        # 카테고리 계산하기
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    # 텍스트 학습하기
    def fit(self, text, category):
        word_list = self.split(text)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(category)

    # 단어 리스트에 점수 매기기
    def score(self, words, category):
        score = math.log(self.category_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    # 예측하기
    def predict(self, text):
        best_category = None
        max_score = -sys.maxsize
        words = self.split(text)
        score_list = []
        for category in self.category_dict.keys():