#abbreviation for ease of typing
w, g, r ,b ,o, y = "white", "green", "red", "blue", "orange", "yellow"

#assigned at starting position
white_face = [
    [w, w, w], 
    [w, w, w] 
    [w, w, w]
]

green_face = [
    [g, g, g],
    [g, g, g],
    [g, g, g],
]

red_face = [
    [r, r, r],
    [r, r, r],
    [r, r, r],
]

blue_face = [
    [b, b, b],
    [b, b, b],
    [b, b, b],
]

orange_face = [
    [o, o, o],
    [o, o, o],
    [o, o, o],
]

yellotow_face = [
    [y, y, y], 
    [y, y, y], 
    [y, y, y], 
]

#assigned at starting position in a 3d array
rubix_cube = [
    #white face = 0
    [
        [w, w, w], 
        [w, w, w],
        [w, w, w]
    ],
    #green face = 1
    [
        [g, g, g],
        [g, g, g],
        [g, g, g],
    ],
    #red face = 2
    [
        [r, r, r],
        [r, r, r],
        [r, r, r],
    ],
    # blue face = 3
    [
        [b, b, b],
        [b, b, b],
        [b, b, b],
    ],
    # orange face = 4
    [
        [o, o, o],
        [o, o, o],
        [o, o, o],
    ],
    # yellow face = 5
    [
        [y, y, y], 
        [y, y, y], 
        [y, y, y], 
    ]
]

def clockwise(which_face, top_face, front_face, right_face, left_face, bottom_face):
    # keep track of pieces in its previous state
    top_piece1, top_piece2, top_piece3 = top_face[2][0], top_face [2][1], top_face[2][2]
    right_piece1, right_piece2, right_piece3 =right_face[0][0],right_face [1][0],right_face[2][0]
    bottom_piece1, bottom_piece2, bottom_piece3 = bottom_face[0][2], bottom_face [0][1], bottom_face[0][0]
    left_piece1, left_piece2, left_piece3 = left_face[2][2], left_face [1][2], left_face[0][2]
    
    front_piece1, front_piece2, front_piece3, front_piece4, front_piece5, front_piece6, front_piece7, front_piece8 = front_face[0][0], front_face[0][1], front_face[0][2], front_face[1][0], front_face[1][2], front_face[2][0],front_face[2][1], front_face[2][2] 
    
    
    # copy data copied from current state of cube onto new state of cube
    right_face[0][0],right_face [1][0],right_face[2][0] = top_piece1, top_piece2, top_piece3
    bottom_face[0][2], bottom_face [0][1], bottom_face[0][0] = right_piece1, right_piece2, right_piece3
    left_face[2][2], left_face [1][2], left_face[0][2] = bottom_piece1, bottom_piece2, bottom_piece3
    top_face[2][0], top_face [2][1], top_face[2][2] = left_piece1, left_piece2, left_piece3
    
    front_face[0][0], front_face[0][1], front_face[0][2], front_face[1][0], front_face[1][2], front_face[2][0],front_face[2][1], front_face[2][2] = front_piece3, front_piece5, front_piece8, front_piece2, front_piece7, front_piece1, front_piece4, front_piece6
    
    
    return top_face, front_face, right_face, left_face, bottom_face