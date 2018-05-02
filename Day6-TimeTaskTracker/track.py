from datetime import datetime
from collections import namedtuple


def TimeMath(endtime, starttime):
    tspan = endtime - starttime
    hrs = tspan.total_seconds() / 3600
    return hrs

WorkItem = namedtuple('WorkItem', 'starttime endtime billto hrsworked')

print("Welcome to your time tracking app.")

work_items = []
while True:
    print("Commands are 'x' to exit the program, 'c' to complete your current item, and 'l' to list the items.")
    print("Please enter what your working on or a command")
    feedback = input()
    if feedback:
        work_item = WorkItem(starttime=datetime.now(), endtime='', billto=feedback, hrsworked=0.00)
        if feedback == 'x':
            break
        if feedback == 'c':
            for i in range(len(work_items)):
                if work_items[i].endtime == '':
                    work_items[i] = work_items[i]._replace(endtime=datetime.now())
                    wi = work_items[i]
                    hrs = TimeMath(wi.endtime, wi.starttime)

                    work_items[i] = work_items[i]._replace(hrsworked=hrs)
                    print('Marked {} complete. You worked on this task for {} hours'.format(
                                                                                wi.billto,
                                                                                '{0:.2f}'.format(hrs)
                                                                                ))
        if feedback == 'l':
            totalhrs = float()
            for item in work_items:
                if item.endtime == '':
                    print("You are currently working on {} for {} hours. Start Time: {}".format(
                          item.billto, '{0:.2f}'.format(TimeMath(datetime.now(),item.starttime)), item.starttime))
                else:
                    print("You worked on {}  for {} hours. Start Time: {} End Time: {}".format(
                          item.billto, '{0:.2f}'.format(item.hrsworked), item.starttime, item.endtime))

                totalhrs += float(item.hrsworked)
                if item.hrsworked == 0.00:
                    totalhrs += TimeMath(datetime.now(), item.starttime)

            print("Today your total hours put in through all activities was {} hours".format(
                                                                                        '{0:.2f}'.format(totalhrs)))
            print("")
        if not work_items:
            work_items.append(work_item)
            print('OK, working on {0}'.format(feedback))
        else:
            count = 0
            for i in range(len(work_items)):
                if work_items[i].endtime == '':
                    count += 1
            if count > 0:
                print('Your already working on something. Close that first.')
            else:
                if feedback != 'x' and feedback != 'c' and feedback != 'l':
                    work_items.append(work_item)
                    print('OK, working on {0}'.format(feedback))


