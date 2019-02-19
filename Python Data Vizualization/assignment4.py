import matplotlib.pyplot as plt
import csv
import numpy as np
from random import randint



import sys
import operator

file = open(sys.argv[1], newline='')
reader = csv.reader(file)
""" FUNCTIONS """


def retrieveData(filename, alist):
    votes = []
    for candidate in alist:
        candidate_order.append(candidate)
        for a in range(1, len(csv_list)):
            votes.append(csv_list[a][csv_list[0].index(candidate)])
    return votes


def to_matrix(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def DispBarPlot():
    temp_dictionary = {}
    two_candidates = []
    for v in vote_list:
        total = 0
        for i in v:
            total += int(i)
        totalVotes.append(total)
    for can, tvote in zip(candidate_order, totalVotes):
        temp_dictionary[can] = tvote
    candidate_one = (max(temp_dictionary, key=lambda key: temp_dictionary[key]))
    del temp_dictionary[candidate_one]
    candidate_two = (max(temp_dictionary, key=lambda key: temp_dictionary[key]))
    two_candidates.append(candidate_one)
    two_candidates.append(candidate_two)
    candidate_one_y = []
    candidate_two_y = []
    states = []
    for i, k in enumerate(csv_list):
        if i >= 1:
            states.append(k[0])
    for z, x in enumerate(csv_list):
        if z >= 1:
            candidate_one_y.append(int(x[csv_list[0].index(candidate_one)]))
            candidate_two_y.append(int(x[csv_list[0].index(candidate_two)]))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ind = np.arange(51)  # the x locations for the groups
    width = 0.15  # the width of the bars

    rects1 = ax.bar(ind, candidate_two_y, width, color='red')
    rects2 = ax.bar(ind + width, candidate_one_y, width, color='blue')

    ax.set_xlim(-width, len(ind) + width)
    ax.set_ylabel('Vote Count')
    ax.set_xlabel('States')

    xTickMarks = states
    ax.set_xticks(ind + width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=90, fontsize=10)

    ax.legend((rects1[0], rects2[0]), (candidate_two, candidate_one))
    plt.savefig('ComparativeVotes.pdf', bbox_inches='tight')
    plt.show()


def CompareVoteonBar():
    total_vote = 0
    for x in vote_list:
        for i in x:
            total_vote += int(i)
    can_dictionary = {}
    for can, tvote in zip(candidate_order, totalVotes):
        can_dictionary[can] = tvote
    for key, value in can_dictionary.items():
        value = '{:.3f}'.format((value / total_vote) * 100)
        can_dictionary[key] = value
    percentages = []
    for name in candidate_order:
        for key, value in can_dictionary.items():
            if name == key:
                percentages.append(float(value))
    N = len(percentages)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    if len(percentages) == 2:
        rects1 = ax.bar(ind, percentages, width, color=['r', 'b'])
    elif len(percentages) == 3:
        rects1 = ax.bar(ind, percentages, width, color=['r', 'b', 'y'])
    elif len(percentages) == 4:
        rects1 = ax.bar(ind, percentages, width, color=['r', 'b', 'y', 'c'])
    else:
        rects1 = ax.bar(ind, percentages, width, color=['r', 'b', 'y', 'c'])
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Vote Percentages')
    ax.set_xlabel('Nominees')
    ax.set_xticks(ind + width)
    ax.set_xticklabels([str(i) + ' %' for i in percentages])
    ax.legend((rects1[0], rects1[1], rects1[2], rects1[3]), (candidate_order))
    plt.savefig('CompVotePercs.pdf', bbox_inches='tight')
    plt.show()


def obtainHistogram(a_list):
    new_vote_list = []
    frequency = []
    for item in a_list:
        item = str(item)
        if len(item) == 1:
            new_vote_list.append('0' + item)
        else:
            new_vote_list.append(item[len(item) - 2:])
    for i in range(10):
        count = 0
        i = str(i)
        for s in new_vote_list:
            s = str(s)
            if s[0] == i:
                count += 1
            if s[1] == i:
                count += 1
        value = (count / (len(new_vote_list) * 2))
        frequency.append(value)
    return frequency


def plotHistogram():
    frequency_list = obtainHistogram(oneD_vote_list)
    f_list_2 = []
    for i in frequency_list:
        temp_i = '{:.3f}'.format(i)
        f_list_2.append(temp_i)
    x_line = [i for i in range(10)]
    mean = 0
    sum = 0
    for i in f_list_2:
        i = float(i)
        sum += i
    mean = sum / len(f_list_2)
    mean_list = []
    for i in range(len(f_list_2)):
        mean_list.append(mean)
    plt.plot(x_line, mean_list, ls='--', color='green', label='Mean')
    plt.plot(x_line, f_list_2, ls='-', color='red', label='Digit Dist.')
    plt.xlabel('Digits')
    plt.ylabel('Distribution')
    plt.legend()
    plt.savefig('Histogram.pdf', bbox_inches='tight')
    plt.show()


def plotHistogramWithSample():
    xline = [i for i in range(10)]
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    for i in range(10):
        x1 = randint(0, 100)
        y1.append(x1)
    for i in range(50):
        x2 = randint(0, 100)
        y2.append(x2)
    for i in range(100):
        x3 = randint(0, 100)
        y3.append(x3)
    for i in range(1000):
        x4 = randint(0, 100)
        y4.append(x4)
    for i in range(10000):
        x5 = randint(0, 100)
        y5.append(x5)
    y1_hist = obtainHistogram(y1)
    y2_hist = obtainHistogram(y2)
    y3_hist = obtainHistogram(y3)
    y4_hist = obtainHistogram(y4)
    y5_hist = obtainHistogram(y5)
    mean_list_1 = [mean(y1_hist) for i in range(10)]
    mean_list_2 = [mean(y2_hist) for i in range(10)]
    mean_list_3 = [mean(y3_hist) for i in range(10)]
    mean_list_4 = [mean(y4_hist) for i in range(10)]
    mean_list_5 = [mean(y5_hist) for i in range(10)]
    # plotting graphs
    plotGraph(xline, mean_list_1, y1_hist, 1)
    plotGraph(xline, mean_list_2, y2_hist, 2)
    plotGraph(xline, mean_list_3, y3_hist, 3)
    plotGraph(xline, mean_list_4, y4_hist, 4)
    plotGraph(xline, mean_list_5, y5_hist, 5)


def plotGraph(x_lin, mean_list, f_list, n):
    plt.plot(x_lin, mean_list, ls='--', color='green', label='Mean')
    plt.plot(x_lin, f_list, ls='-', color='red', label='Digit Dist.')
    plt.xlabel('Digits')
    plt.ylabel('Distribution')
    plt.legend()
    plt.savefig('HistogramofSample' + str(n) + '.pdf', bbox_inches='tight')
    plt.show()


def mean(o_list):
    total = 0
    for i in o_list:
        total += float(i)
    return total / len(o_list)


def calculateMSE(list1, list2):
    mse = 0
    for i, j in zip(list1, list2):
        mse += (i - j) ** 2
    return mse


def US_MSE(list_f):
    listone = obtainHistogram(list_f)
    listtwo = [0.1 for i in range(10)]
    answer = calculateMSE(listone, listtwo)
    return answer


def compareMSEs(number):
    result_list = []
    templist = []
    smaller = 0
    greater = 0
    for i in range(10000):
        for j in range(len(oneD_vote_list)):
            num = randint(0, 100)
            templist.append(num)
        histogram = US_MSE(templist)
        if histogram > number:
            greater += 1
        elif histogram < number:
            smaller += 1
    result_list.append(smaller)
    result_list.append(greater)
    return result_list


#######################################################
# MAIN CODE#
#######################################################
csv_list = []
totalVotes = []
candidate_order = []
for line in reader:
    temp_line = line
    csv_list.append(temp_line)
vote_list = to_matrix(retrieveData(sys.argv[1], sys.argv[2]), 51)
DispBarPlot()
CompareVoteonBar()
oneD_vote_list = retrieveData(sys.argv[1], sys.argv[2])
plotHistogram()
plotHistogramWithSample()
result = US_MSE(oneD_vote_list)
print(compareMSEs(result))

