import os
import random

# @Time    : 2018-12-02
# @Author  : auhtor

"""
    In this program, the problem list is read from the data file, 
    and then one of them is randomly selected for questioning, 
    and 80% of the questions will be extracted for questioning.
    
    The problem in the data file, the answer is defined as follows:
    The prompt for the question is one line, the question and the answer are on one line, and the question and answer are separated by ",".
    If there are multiple answers, they are also separated by ",".
"""


def ask_question(correct_num, asked_num):
    """
    Ask questions to users
    :param correct_num:Answer the correct number of questions
    :param asked_num: Number of questions answered
    :return:
    """
    while (asked_num <= int((len(questionList) - 1) * 0.8)):
        q = get_question()
        print(q['prompt'] + '\n')
        input_s = input(q['title'] + '\n')
        asked_num = asked_num + 1
        if q['multiple_answers']:
            if (i in q['answer'] for i in input_s.split(',')):
                correct_num = correct_num + 1
                print('Correct!\n')
            else:
                print('Incorrect! The answer is ' + ','.join(q['answer']) + '\n')
        elif input_s == q['answer']:
            correct_num = correct_num + 1
            print('Correct!\n')
        else:
            print('Incorrect! The answer is ' + q['answer'] + '\n')
    accuracy = (float(correct_num) / float(asked_num)) * 100
    print('You got %d answers correct out of %d,which is %d' % (correct_num, asked_num, accuracy) + '%\n')


def read_dataFile(fileName):
    """
    Read the question bank from the selected data file
    :param fileName: data file
    :return:the question bank
    """
    try:
        questionList = []
        prompt = None
        with open(fileName, 'r') as f:
            for i in f.readlines():
                i = i.strip('\n')
                question = {}
                if len(i.split(',')) == 1:
                    if i != prompt:
                        prompt = i
                else:
                    question['prompt'] = prompt
                    question['flag'] = False  # Has the question been answered?
                    question['title'] = i.split(',')[0]
                    if len(i.split(',')) > 2:
                        question['answer'] = list(i.split(',')[1:])
                        question['multiple_answers'] = True  # There are multiple answers to the question.
                    else:
                        question['answer'] = i.split(',')[1]
                        question['multiple_answers'] = False
                if question:
                    questionList.append(question)
        return questionList
    except Exception:
        print('Error reading data file')


def get_question():
    """
    Obtaining a Random Problem from Problem Base
    :return:A Random question
    """
    flag = True
    q = None
    while (flag):
        q = random.choice(questionList)
        flag = q['flag']
        index = questionList.index(q)
        questionList[index]['flag'] = True
    return q


def get_fileName(path):
    """
    Allow users to select data files themselves
    :param path:Paths entered by users themselves
    :return: Data files selected by users themselves
    """
    fileName = input('Select data file from ' + ','.join(os.listdir(path)) + ' ')
    return fileName


if __name__ == '__main__':
    path = input('The directory where the input data file is located: ')
    fileName = get_fileName(path)
    questionList = read_dataFile(fileName)
    ask_question(0, 0)
