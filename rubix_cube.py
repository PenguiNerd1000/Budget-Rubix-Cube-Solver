#abbreviation for ease of typing
w, g, r ,b ,o, y = "w", "g", "r", "b", "o", "y"
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

def clockwise(which_face, rubix_cube):
    # define side based on which face
    if which_face == 0:
        top_side, right_side, bottom_side, left_side, front_side = 3, 2, 1, 4, 0
    elif which_face == 1:
        top_side, right_side, bottom_side, left_side, front_side = 0, 2, 5, 4, 1
    elif which_face == 2:
        top_side, right_side, bottom_side, left_side, front_side = 0, 3, 5, 1, 2
    elif which_face == 3: 
        top_side, right_side, bottom_side, left_side, front_side = 0, 4, 5, 2, 3
    elif which_face == 4:
        top_side, right_side, bottom_side, left_side, front_side = 0, 1, 5, 3, 4
    else:
        top_side, right_side, bottom_side, left_side, front_side = 1, 2, 3, 4, 5
    
    # keep track of pieces in its previous state
    top_piece1, top_piece2, top_piece3 = rubix_cube[top_side][2][0], rubix_cube[top_side][2][1], rubix_cube[top_side][2][2]
    right_piece1, right_piece2, right_piece3 = rubix_cube[right_side][0][0], rubix_cube[right_side][1][0],rubix_cube[right_side][2][0]
    bottom_piece1, bottom_piece2, bottom_piece3 = rubix_cube[bottom_side][0][2], rubix_cube[bottom_side][0][1], rubix_cube[bottom_side][0][0]
    left_piece1, left_piece2, left_piece3 = rubix_cube[left_side][2][2], rubix_cube[left_side][1][2], rubix_cube[left_side][0][2]
    
    front_piece1, front_piece2, front_piece3, front_piece4, front_piece5, front_piece6, front_piece7, front_piece8 = rubix_cube[front_side][0][0], rubix_cube[front_side][0][1], rubix_cube[front_side][0][2], rubix_cube[front_side][1][0], rubix_cube[front_side][1][2], rubix_cube[front_side][2][0],rubix_cube[front_side][2][1], rubix_cube[front_side][2][2] 
    
    
    # copy data copied from current state of cube onto new state of cube
    rubix_cube[right_side][0][0], rubix_cube[right_side][1][0], rubix_cube[right_side][2][0] = top_piece1, top_piece2, top_piece3
    rubix_cube[bottom_side][0][2], rubix_cube[bottom_side] [0][1], rubix_cube[bottom_side][0][0] = right_piece1, right_piece2, right_piece3
    rubix_cube[left_side][2][2], rubix_cube[left_side] [1][2], rubix_cube[left_side][0][2] = bottom_piece1, bottom_piece2, bottom_piece3
    rubix_cube[top_side][2][0], rubix_cube[top_side] [2][1], rubix_cube[top_side][2][2] = left_piece1, left_piece2, left_piece3
    
    rubix_cube[front_side][0][0], rubix_cube[front_side][0][1], rubix_cube[front_side][0][2], rubix_cube[front_side][1][0], rubix_cube[front_side][1][2], rubix_cube[front_side][2][0],rubix_cube[front_side][2][1], rubix_cube[front_side][2][2] = front_piece3, front_piece5, front_piece8, front_piece2, front_piece7, front_piece1, front_piece4, front_piece6
    
    
    return rubix_cube

def counter_clockwise(which_face, rubix_cube):
    # define side based on which face
    if which_face == 0:
        top_side, right_side, bottom_side, left_side, front_side = 3, 2, 1, 4, 0
    elif which_face == 1:
        top_side, right_side, bottom_side, left_side, front_side = 0, 2, 5, 4, 1
    elif which_face == 2:
        top_side, right_side, bottom_side, left_side, front_side = 0, 3, 5, 1, 2
    elif which_face == 3: 
        top_side, right_side, bottom_side, left_side, front_side = 0, 4, 5, 2, 3
    elif which_face == 4:
        top_side, right_side, bottom_side, left_side, front_side = 0, 1, 5, 3, 4
    else:
        top_side, right_side, bottom_side, left_side, front_side = 1, 2, 3, 4, 5
    
    # keep track of pieces in its previous state
    top_piece1, top_piece2, top_piece3 = rubix_cube[top_side][2][0], rubix_cube[top_side][2][1], rubix_cube[top_side][2][2]
    right_piece1, right_piece2, right_piece3 = rubix_cube[right_side][0][0], rubix_cube[right_side][1][0],rubix_cube[right_side][2][0]
    bottom_piece1, bottom_piece2, bottom_piece3 = rubix_cube[bottom_side][0][2], rubix_cube[bottom_side][0][1], rubix_cube[bottom_side][0][0]
    left_piece1, left_piece2, left_piece3 = rubix_cube[left_side][2][2], rubix_cube[left_side][1][2], rubix_cube[left_side][0][2]
    
    front_piece1, front_piece2, front_piece3, front_piece4, front_piece5, front_piece6, front_piece7, front_piece8 = rubix_cube[front_side][0][0], rubix_cube[front_side][0][1], rubix_cube[front_side][0][2], rubix_cube[front_side][1][0], rubix_cube[front_side][1][2], rubix_cube[front_side][2][0],rubix_cube[front_side][2][1], rubix_cube[front_side][2][2] 
    
    
    # copy data copied from current state of cube onto new state of cube
    rubix_cube[right_side][0][0], rubix_cube[right_side][1][0], rubix_cube[right_side][2][0] = bottom_piece1, bottom_piece2, bottom_piece3
    rubix_cube[bottom_side][0][2], rubix_cube[bottom_side] [0][1], rubix_cube[bottom_side][0][0] = left_piece1, left_piece2, left_piece3
    rubix_cube[left_side][2][2], rubix_cube[left_side] [1][2], rubix_cube[left_side][0][2] = top_piece1, top_piece2, top_piece3
    rubix_cube[top_side][2][0], rubix_cube[top_side] [2][1], rubix_cube[top_side][2][2] = right_piece1, right_piece2, right_piece3
    
    rubix_cube[front_side][0][0], rubix_cube[front_side][0][1], rubix_cube[front_side][0][2], rubix_cube[front_side][1][0], rubix_cube[front_side][1][2], rubix_cube[front_side][2][0],rubix_cube[front_side][2][1], rubix_cube[front_side][2][2] = front_piece3, front_piece5, front_piece8, front_piece2, front_piece7, front_piece1, front_piece4, front_piece6
    
    
    return rubix_cube