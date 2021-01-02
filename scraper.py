#!/usr/bin/env python3
import requests
import time
from bs4 import BeautifulSoup


def main():
    URL = 'https://www.uoguelph.ca/registrar/calendars/undergraduate/current/c12/c12cis.shtml'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    findPreReqs("CIS*3110", soup, page)

# Description: Finds prereqs for courses
# Input: The course to find prereqs for, the soup instance, the page to parse
def findPreReqs(course, soup, page):
    start = 0

    results = soup.find(summary=course+' course description')
    if results != None:
        # print(results)
        prettyTable = results.prettify()

        # print(prettyTable)

        
        soup = BeautifulSoup(prettyTable, 'html.parser')
        results = soup.find_all("tr", class_="prereqs")
        if len(results) != 0:
            prettyTable = results[0].prettify()

            soup = BeautifulSoup(prettyTable, 'html.parser')
            results = soup.find_all("a", class_="clink")

            for course in results:
                print(course.string.rstrip())
                soup = BeautifulSoup(page.content, 'html.parser')
                findPreReqs(course.string.rstrip().lstrip(), soup, page)

    # prettyTableList = prettyTable.split("\n")

    # for i in range(0, len(prettyTableList), 1):
    #     print(i)
        
    #     # if '<th class="label" scope="row">Prerequisite(s):</th>' in prettyTableList[i]:
    #     #     # Grab the pre reqs on the next line
    #     #     print(i)
    #     # if "<tr class=\"prereqs\">" in prettyTableList[i]:
    #     #     print("i here:" + str(i))
    #     #     start = i
    #     # if prettyTableList[i] in '</tr>' and start != 0:
    #     # #     # Grab the prereqs
    #     #     print(i)
    #     #     print("start" + str(start))
    #     #     for j in range(start, i, 1):
    #     #         print(j)
    #     if "<td class=\"text\"><a class=\"clink\" href=\"" in prettyTableList[i]:
    #         print("Hey!")



    #     #     # Grab those prereqs' preqreqs
    #         break





if __name__ == '__main__':
    main()

