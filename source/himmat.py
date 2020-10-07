'''
Copyright 2020 Aniket Kumar

Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
 under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 either express or implied. See the License for the specific language
 governing permissions and limitations under the License.

'''

from datetime import date


def to_integer(dt_time):
    return dt_time.day


def primary():
    print()
    print("*** LOSE NOT YOUR HEART ***")
    print()
    print("Refining oneself is the greatest service to humanity")
    print("                - Pandit Shriram Sharma Acharya")
    print()
    f = open("LNYH_head.txt")
    head = f.readlines()
    f.close()
    f = open("LNYH.txt")
    LNYH = f.readlines()
    f.close()
    d = date.today()
    print("Today is: ", d)
    day = d.strftime("%d")
    print("Motivation for Day ", day, ":")
    tday = to_integer(date.today())
    print()
    print("        ", head[tday-1])
    print(LNYH[tday-1])
    print()
    print()
    print("-----------------------------------------")
    print("Developed by Aniket, a student of DSVV.")
    print("My website: https://crypticani.github.io/")
    print()
    hold = input()


if __name__ == "__main__":
    try:
        primary()
    except:
        print("Please put the files LNYH.txt and LNYH_head.txt with this program.")
        hold = input()
