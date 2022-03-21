"""Solution to HackerRank's pyton coding challenge.
Given a time in 12-hour AM/PM format convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.



@author: Mohammed Salim Dason
@email: salimdason@outlook.com
@twitter: moedason
"""


def timeConversion(s):
    """ Let us begin by splitting the string input into a list using ":" as our seperator. Then we determine
    if it is PM or AM simply by indexing and comparing. If it is PM we simply add 12 to the hour. """
    time = s.split(":")
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0]) + 12)
    else:
        if time[0] == "12":
            time[0] = "00"
    stringtime: str = ':'.join(time)

    # Return the converted time without PM or AM because it is not needed.
    return str(stringtime[:-2])


if __name__ == '__main__':
    s = input("Enter time: ")
    print(timeConversion(s))
