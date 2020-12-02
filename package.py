#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program determines whether a given package will be accepted


def main():
    # This function determines whether a package will be accepted
    # through the inputs of this function

    print("This program tells the user whether their"
          "package will be accepted or not.")
    print("Please input the following values in kgs and cms:")
    print("")
    weight_Str = input("weight: ")
    weight = int(weight_Str)
    print("")
    length = int(input("length: "))
    print("")
    width = int(input("width: "))
    print("")
    height = int(input("height: "))
    volume_Str = str(height*width*length)
    volume = int(volume_Str)
    print("The weight is " + weight_Str + "kg and the volume is "
          + volume_Str + "cm³.")

    if weight >= 27:
        print("Package Denied. Too Heavy")

    if volume >= 10000:
        print("Package Denied. Too Large")

    else:
        print("Package Accepted")


if __name__ == "__main__":
    main()
