import random
import re
import sys

from matplotlib import animation
from matplotlib import pyplot as plt

from algorithms.bubbleSort import bubbleSort
from algorithms.timSort import timSort
from algorithms.mergeSort import mergeSort
from algorithms.insertionSort import insertionSort
from algorithms.quickSort import quickSort
from algorithms.visualizer import Visualizer

stype_dic = {'all': -1,
             'insertion-sort': 0, 'bubble-sort': 1, 'merge-sort': 2,
             'quick-sort': 3}
titles = [r'Insertion Sort ($O(n^2)$)', r'Shell Sort ($O(n \cdot log_2(n)^2)$)', r'Selection Sort ($O(n^2)$)',
          r'Merge Sort ($O(n \cdot log_2(n))$)', r'Quick Sort ($O(n \cdot log_2(n))$)',
          r'Heap Sort ($O(n \cdot log_2(n))$)',
          r'Bubble Sort ($O(n^2)$)', r'Comb Sort ($O(n \cdot log_2(n))$)', r'Monkey Sort ($O(n!)$)']
funs = [insertionSort, bubbleSort, mergeSort,
        quickSort]


def create_original_data(dtype):
    data = []
    if dtype == 'random':
        data = list(range(1, Visualizer.sizeArrays + 1))
        random.shuffle(data)
    return data


def draw_chart(stype, original_data, frame_interval):
    # First set up the figure, the axis, and the plot elements we want to animate.
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Visualizer(d) for d in original_data]
    axs = fig.add_subplot(111)
    axs.set_xticks([])
    axs.set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95, wspace=0.05, hspace=0.15)

    # Get the data of all frames.
    # frames = bubbleSort(data_set)
    frames = funs[stype](data_set)
    # Output the frame count.
    print('%s: %d frames.' % (re.findall(r'\w+ Sort', titles[stype])[0], len(frames)))

    # Animation function. This is called sequentially.
    # Note: fi is framenumber.
    def animate(fi):
        print(fi)
        print(frames[0])
        bars = []
        if len(frames) > fi:
            print("CU")
            print(frames[fi])
            axs.cla()
            axs.set_title(titles[stype])
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(Visualizer.sizeArrays)),  # X
                            [d.value for d in frames[fi]],  # data
                            1,  # width
                            color=[d.color for d in frames[fi]]  # color
                            ).get_children()
        return bars

    # Call the animator.
    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=frame_interval)
    return plt, anim


def draw_all_charts(original_data, frame_interval):
    # First set up the figure, the axis, and the plot elements we want to animate.
    axs = []
    frames = []
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Visualizer(d) for d in original_data]
    for i in range(9):
        axs.append(fig.add_subplot(331 + i))
        axs[-1].set_xticks([])
        axs[-1].set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)

    # Get the data of all frames.
    for i in range(8):
        frames.append(f"{funs[i]}({data_set})")
    # The frame count of monkey sort is 50 more than the maximum one.
    frames.append(funs[8](data_set, max(len(f) for f in frames) + 50))

    # Output the frame counts of all chart.
    names = []
    max_name_length = 0
    frame_counts = []
    max_frame_length = 0
    for i in range(9):
        names.append(re.findall(r'\w+ Sort', titles[i])[0] + ':')
        if len(names[-1]) > max_name_length:
            max_name_length = len(names[-1])
        frame_counts.append(len(frames[i]))
        if len(str(frame_counts[-1])) > max_frame_length:
            max_frame_length = len(str(frame_counts[-1]))
    for i in range(9):
        print('%-*s %*d frames' % (max_name_length, names[i], max_frame_length, frame_counts[i]))

    # Animation function. This is called sequentially.
    # Note: fi is framenumber.
    def animate(fi):
        bars = []
        for i in range(9):
            if len(frames[i]) > fi:
                axs[i].cla()
                axs[i].set_title(titles[i])
                axs[i].set_xticks([])
                axs[i].set_yticks([])
                bars += axs[i].bar(list(range(Visualizer.sizeArrays)),  # X
                                   [d.value for d in frames[i][fi]],  # data
                                   1,  # width
                                   color=[d.color for d in frames[i][fi]]  # color
                                   ).get_children()
        return bars

    # Call the animator.
    anim = animation.FuncAnimation(fig, animate, frames=max(len(f) for f in frames), interval=frame_interval)
    return plt, anim


if __name__ == "__main__":
    try:
        Visualizer.sizeArrays = int(input('Please set array size to be sorted (default = 32): '))
    except:
        Visualizer.sizeArrays = 32

    if len(sys.argv) > 1:
        # Type of sort algorithm.
        stype = -1
        if len(sys.argv) > 2:
            if sys.argv[2] in stype_dic:
                stype = stype_dic[sys.argv[2]]
            else:
                print('Error: Wrong argument!')
                exit()
        stype_str = list(stype_dic.keys())[list(stype_dic.values()).index(stype)]

        # Type of data.
        od = create_original_data('random')
        # Frames
        fi = 100
        # Show animation
        plt, _ = draw_all_charts(od, fi) if stype == -1 else draw_chart(stype, od, fi)
        plt.show()
