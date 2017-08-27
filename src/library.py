'''
Created on Aug 26, 2017

@author: Mily
'''
def height_ftiins_to_cm(x):
    # print x
    x = x.replace('"', "")
    heights = x.split("'")
    ft_to_cm = float(heights[0]) * 30
    incs_to_cm = float(heights[1]) * 2.5
    return ft_to_cm + incs_to_cm
