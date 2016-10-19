class question:
    def __init__(self, question, answer1, answer2, answer3, answer4, difficulty):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.difficulty = difficulty

    def __str__(self):
        return 'Question: {}, A1: {}, A2: {}, A3: {}, A4: {}, Diff: {}'.format(self.question, self.answer1,
                                                                               self.answer2, self.answer3,
                                                                               self.answer4, self.difficulty)



class player:
    def __init__(self, nick, password, points, last):
        self.nick = nick
        self.password = password
        self.points = points

    def __str__(self):
        return 'Nick: {}, Points: {}'.format(self.nick, self.points)

    def get_question():
        pass