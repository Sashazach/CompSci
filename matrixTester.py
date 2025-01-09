import MaxtrixMaster

ralph = MaxtrixMaster.Matrix(3,1)
ralph.data = [
    [2],
    [4],
    [3],
]

romeo = MaxtrixMaster.Matrix(2,3)
romeo.data = [
    [3, 4, 5],
    [6, 7, 8],
]

mult = romeo.times(ralph)
mult.print_matrix()