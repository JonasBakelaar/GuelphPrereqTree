# GuelphPrereqTree
Gives you a list of prereqs for courses at Guelph

# TODO List
    - Put courses into a tree with different levels for each prereq
    - Parse every course list page
    - Be able to grab course prereqs from another page's list of courses
        - This seems to be a common issue...

# Libraries
The following libraries are used in this project
    - requests
    - beautifulsoup4

# Things to factor in
There's some stuff that needs to be thought about here:
    - Courses that have a credit requirement OR prereq list
    - Optional prereqs (this course OR this course)
    - Probably more that I'm missing
    