#Python2.7
#Copyright ZhaoShuo,2017.9.23
#ShuoCHN e-mail:zhaoshuo100@foxmail.com
#version:1.1

#version:1.0 2017.9.23
#version:1.1 2017.9.23


# this is a program which can get the problem that others has sloved but you haven't in the qdacm.com
# it could offer you the Problem ID,and you can open them all in the browser if you want
# it hasn't support Chinese characters

# versionV1.1 update:
# you can choose to save the Problems ID into a txt file




import urllib
import webbrowser

print """
Version:1.1
# this is a program which can get the problem ID that others has sloved but you haven't in the qdacm.com
# it could offer you the Problem ID
# and you can open them all in the browser fully-automatic if you want
# it hasn't support Chinese characters

# versionV1.1 update:
# you can choose to save the Problems ID into a txt file

Copyright 2017 ZhaoShuo.  All Rights Reserved.
e_mail:zhaoshuo100@foxmail.com

------------------start now--------------------------

"""



def get_prob_list(usr_name):
    usr_name_in = usr_name
    usr_url="https://qdacm.com/User/"+usr_name_in
    usr1_page= urllib.urlopen(usr_url)
    usr1_html= usr1_page.read()

    start_num=usr1_html.find("label label-primary")
    end_num = usr1_html.find("</div>",start_num)
    useful_part = usr1_html[start_num-25:end_num]
    #print useful_part
    useful_part_long = len(useful_part)
    prob_list=[]

    last=0

    while last<useful_part_long:
        first_index=useful_part.find('">',last)
        prob_num=useful_part[first_index+2:first_index+6]
        prob_list.append(prob_num)
        last=first_index+20

    return prob_list

def usr_name_require(usr_name_re):
    usr_name_in = usr_name_re
    usr_url = "https://qdacm.com/User/" + usr_name_in
    usr1_page = urllib.urlopen(usr_url)
    usr1_html = usr1_page.read()
    if "cannot found user" in usr1_html:
        outp = "cannot found user:"+usr_name_in
        print outp
        return 0
    else:
        return 1

def compare():

    prob_lack=[]
    usr_name_1=raw_input("Please enter your ID: ")
    while usr_name_require(usr_name_1)==0:
        usr_name_1 = raw_input("Please enter your ID: ")
    global user_name_all_1
    user_name_all_1 = usr_name_1


    usr_list_1 = get_prob_list(usr_name_1)

    usr_name_2 = raw_input("Please enter the ID you want to beat: ")
    while usr_name_require(usr_name_2) == 0:
        usr_name_2 = raw_input("Please enter the ID you want to beat: ")
    global user_name_all_2
    user_name_all_2 = usr_name_2


    usr_list_2 = get_prob_list(usr_name_2)


    for num_2 in usr_list_2:
        if num_2 not in usr_list_1:
            prob_lack.append(num_2)

    num_lack = len(prob_lack)
    out = "There are %s(S) problem that %s has done but %s haven't. "%(num_lack,user_name_all_2,user_name_all_1)
    print
    print out
    print
    if num_lack!=0:
        print "The problem ID are:"
    hang = 0
    for i in prob_lack:
        print i,
        hang +=1
        if hang ==10:
            print
            hang =0

    return prob_lack


def openweb(prob_list):
    for pro_num in prob_list:
        url = "https://qdacm.com/P/"+pro_num
        webbrowser.open(url)
    print "finished."


def save_list(prob_list):
    prob_list_in = prob_list
    file_name = user_name_all_1+"_VS_"+user_name_all_2+".txt"
    save_file = open(file_name, 'w+')


    num_list = len(prob_list)
    text = "There are %s(S) problem that %s has done but %s haven't. "%(num_list,user_name_all_2,user_name_all_1)
    text += "\nThe Problems ID are: \n"
    a = 0
    for i in prob_list_in:
        text += i
        text += " "
        a+=1
        if a == 10:
            text += '\n'
            a=0

    save_file.write(text)

    save_file.close()

    print "saved into: "+file_name+" finished."





problem_list = compare()
print
print

usr_save_ans = raw_input("do you want to save the problems ID into a txt file(Press Y to save,Press any other key to cancel): ")
if usr_save_ans =="Y":
    save_list(problem_list)
    print


usr_ans = raw_input("do you want to open these problems in the BROWSER(Press Y to OPEN,Press any other key to quit): ")
if usr_ans == "Y":
    openweb(problem_list)
else:
    print "pratice more!have a good time"



