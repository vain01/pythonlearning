# gather
def gather(*args):
    print(args)


gather(1, 2, 3)

# scatter
nums_list = [2, 3, 4]
gather(*nums_list)
