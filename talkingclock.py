"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make
a Talking Clock? I need a script that takes an input 24-hour time
(00:00 - 23:59) and translates it into words. Please format the input
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string

            #TODO: Write code below to return a string with the solution to the prompt.
            res = "It's "
            hour = input_time[0]+input_time[1]
            first = int(hour)%12
            if first == 0:
                first = 12

            dic = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve"}
            hour = dic[first]
            res += hour
            min = input_time[3]
            sec = int(min)
            if sec == 0:
                res+="oh "
            elif sec == 1:
                res += ""
            elif sec == 2:
                res+= "twenty "
            elif sec == 3:
                res += "thirty "
            elif sec == 4:
                res += "fourty "
            elif sec == 5:
                res += "fifty "

            if int(input_time[4]) == 0:
                if(sec == 0):
                    res += "clock "
            else:
                res+= dic[int(input_time[4])]
            if int(input_time[0]) < 2:
                res += "am"
            else:
                res += "pm"
            print(input_time)
            print(res)
            return res

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)

if __name__ == '__main__':
    main()
