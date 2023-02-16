# function for line generation
def bresenham(x1, y1, x2, y2):
    dy = (y2 - y1)
    dx = (x2 - x1)
    dy = 2*(y2 - y1)
    slope_error_new = dy - dx
    y = y1
    for x in range(x1, x2+1):

        print("(",x,",",y,")\n")
        slope_error_new = slope_error_new + dy
        if (slope_error_new >= 0):
            y = y+1
            slope_error_new = slope_error_new - (2 * dx)

if __name__ == '__main__':
    x1 = 1
    y1 = 1
    x2 = 8
    y2 = 5
    bresenham(x1, y1, x2, y2)
