# import television
from Television import TV
# def main function
def main():
    # create tv1 
    tv1 = TV(30, 3, False)
    print(f"\ntv1's channel is {tv1.channel} and volume level is {tv1.volume_level}")
    # create tv2
    tv2 = TV(3, 2, True)
    print(f"\ntv2's channel is {tv2.channel} and volume level is {tv2.volume_level}\n")
# call main function
main()