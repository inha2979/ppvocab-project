from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

# 동사 단어 목록
verb_pool = ['be', 'have', 'do', 'say', 'go', 'get', 'make', 'know', 'think', 'take',
    'see', 'come', 'want', 'look', 'use', 'find', 'give', 'tell', 'work', 'call',
    'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let',
    'begin', 'seem', 'help', 'talk', 'turn', 'start', 'show', 'hear', 'play', 'run',
    'move', 'like', 'live', 'believe', 'hold', 'bring', 'happen', 'write', 'sit', 'stand',
    'lose', 'pay', 'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead', 'understand',
    'watch', 'follow', 'stop', 'create', 'build', 'read', 'remember', 'buy', 'send', 'hope',
    'win', 'sell', 'jump', 'dance', 'sing', 'walk', 'climb', 'fly', 'swim', 'cook',
    'drink', 'eat', 'open', 'close', 'push', 'pull', 'throw', 'catch', 'cut', 'grow',
    'fall', 'break', 'wake', 'finish', 'speak', 'touch', 'sleep', 'dream', 'wait', 'listen'
   
]

# 다른 단어 목록 (명사, 형용사 등)
other_word_pool = ['airport', 'airplane', 'passport', 'visa', 'luggage', 'backpack', 'map', 'compass', 'hotel', 'motel',
    'hostel', 'resort', 'train', 'bus', 'taxi', 'car', 'cruise', 'boat', 'ship', 'beach',
    'mountain', 'desert', 'forest', 'ocean', 'river', 'lake', 'island', 'city', 'country', 'continent',
    'tour', 'trip', 'journey', 'adventure', 'vacation', 'holiday', 'souvenir', 'camera', 'photo', 'museum',
    'gallery', 'palace', 'castle', 'temple', 'church', 'monument', 'landmark', 'pyramid', 'statue', 'bridge',
    'man', 'woman', 'child', 'boy', 'girl', 'dog', 'cat', 'house', 'road', 'window',
    'light', 'water', 'food', 'sun', 'moon', 'star', 'fire', 'ice', 'money', 'time',
    'day', 'night', 'friend', 'family', 'school', 'music', 'story', 'dream', 'hope', 'life',
    'big', 'small', 'good', 'bad', 'happy', 'sad', 'fast', 'slow', 'tall', 'short',
    'strong', 'weak', 'beautiful', 'ugly', 'young', 'brave', 'kind', 'clever', 'warm', 'cold'

]

# 웹사이트의 메인 페이지를 보여주는 함수
@app.route('/')
def index():
    return render_template('index.html')

# 단어 뽑기 요청을 처리하는 함수
@app.route('/draw', methods=['POST'])
def draw_words():
    try:
        num_total_words = int(request.form['num_players'])
        num_verbs = 8
        num_others = num_total_words - num_verbs

        if num_others < 0:
            result = "팀원 수는 최소 5명이어야 합니다."
        else:
            selected_verbs = random.sample(verb_pool, num_verbs)
            selected_others = random.sample(other_word_pool, num_others)

            final_word_list = selected_verbs + selected_others
            random.shuffle(final_word_list)
            
            result = f"선택된 단어 ({num_total_words}개): {', '.join(final_word_list)}"
            
    except ValueError:
        result = "15"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


