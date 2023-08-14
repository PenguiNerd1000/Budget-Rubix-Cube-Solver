w, g, r ,b ,o, y = "w", "g", "r", "b", "o", "y"

rubix_cube = [
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
def clockwise(turning_side, rubix_cube): 
    if turning_side == 0:
        top_side, right_side, bottom_side, left_side,  = 2, 1, 4, 3
    elif turning_side == 1:
        top_side, right_side, bottom_side, left_side,  = 5, 4, 0, 2
    elif turning_side == 2:
        top_side, right_side, bottom_side, left_side,  = 5, 1, 0, 3
    elif turning_side == 3: 
        top_side, right_side, bottom_side, left_side,  = 5, 2, 0, 4
    elif turning_side == 4:
        top_side, right_side, bottom_side, left_side,  = 5, 3, 0, 1
    else:
        top_side, right_side, bottom_side, left_side,  = 4, 1, 2, 3
    
    top_piece1, top_piece2, top_piece3 = rubix_cube[top_side][2][0], rubix_cube[top_side][2][1], rubix_cube[top_side][2][2]
    right_piece1, right_piece2, right_piece3 = rubix_cube[right_side][2][0], rubix_cube[right_side][2][1],rubix_cube[right_side][2][2]
    bottom_piece1, bottom_piece2, bottom_piece3 = rubix_cube[bottom_side][2][0], rubix_cube[bottom_side][2][1], rubix_cube[bottom_side][2][2]
    left_piece1, left_piece2, left_piece3 = rubix_cube[left_side][2][2], rubix_cube[left_side][1][2], rubix_cube[left_side][0][2]
    turning_face1, turning_face2, turning_face3, turning_face4, turning_face5, turning_face6, turning_face7, turning_face8 = rubix_cube[turning_side][0][0], rubix_cube[turning_side][0][1], rubix_cube[turning_side][0][2], rubix_cube[turning_side][1][0], rubix_cube[turning_side][1][2], rubix_cube[turning_side][2][0],rubix_cube[turning_side][2][1], rubix_cube[turning_side][2][2]
     
    rubix_cube[left_side][2][2], rubix_cube[left_side][2][1],rubix_cube[left_side][2][0] = bottom_piece1, bottom_piece2, bottom_piece3
    rubix_cube[top_side][2][0], rubix_cube[top_side][2][1], rubix_cube[top_side][2][2] = left_piece1, left_piece2, left_piece3
    rubix_cube[right_side][2][0], rubix_cube[right_side][2][1], rubix_cube[right_side][2][2] = top_piece1, top_piece2, top_piece3
    rubix_cube[bottom_side][2][2], rubix_cube[bottom_side][2][1], rubix_cube[bottom_side][2][0] = right_piece1, right_piece2, right_piece3
    #fix this, turning faces arent proper
    rubix_cube[turning_side][0][0], rubix_cube[turning_side][0][1], rubix_cube[turning_side][0][2], rubix_cube[turning_side][1][0], rubix_cube[turning_side][1][2], rubix_cube[turning_side][2][0],rubix_cube[turning_side][2][1], rubix_cube[turning_side][2][2] = turning_face6, turning_face4, turning_face1, turning_face7, turning_face2, turning_face8, turning_face5, turning_face3
    return rubix_cube


def counter_clockwise(turning_side, rubix_cube):
    if turning_side == 0:
        top_side, right_side, bottom_side, left_side,  = 2, 1, 4, 3
    elif turning_side == 1:
        top_side, right_side, bottom_side, left_side,  = 5, 4, 0, 2
    elif turning_side == 2:
        top_side, right_side, bottom_side, left_side,  = 5, 1, 0, 3
    elif turning_side == 3: 
        top_side, right_side, bottom_side, left_side,  = 5, 2, 0, 4
    elif turning_side == 4:
        top_side, right_side, bottom_side, left_side,  = 5, 3, 0, 1
    else:
        top_side, right_side, bottom_side, left_side,  = 4, 1, 2, 3

    top_piece1, top_piece2, top_piece3 = rubix_cube[top_side][2][0], rubix_cube[top_side][2][1], rubix_cube[top_side][2][2]
    right_piece1, right_piece2, right_piece3 = rubix_cube[right_side][2][0], rubix_cube[right_side][2][1],rubix_cube[right_side][2][2]
    bottom_piece1, bottom_piece2, bottom_piece3 = rubix_cube[bottom_side][2][0], rubix_cube[bottom_side][2][1], rubix_cube[bottom_side][2][2]
    left_piece1, left_piece2, left_piece3 = rubix_cube[left_side][2][2], rubix_cube[left_side][1][2], rubix_cube[left_side][0][2]
    turning_face1, turning_face2, turning_face3, turning_face4, turning_face5, turning_face6, turning_face7, turning_face8 = rubix_cube[turning_side][0][0], rubix_cube[turning_side][0][1], rubix_cube[turning_side][0][2], rubix_cube[turning_side][1][0], rubix_cube[turning_side][1][2], rubix_cube[turning_side][2][0],rubix_cube[turning_side][2][1], rubix_cube[turning_side][2][2]
     
    rubix_cube[left_side][2][2], rubix_cube[left_side][2][1], rubix_cube[left_side][2][0] = top_piece1, top_piece2, top_piece3
    rubix_cube[top_side][2][0], rubix_cube[top_side][2][1], rubix_cube[top_side][2][2] = right_piece1, right_piece2, right_piece3
    rubix_cube[right_side][2][0], rubix_cube[right_side][2][1], rubix_cube[right_side][2][2] = bottom_piece1, bottom_piece2, bottom_piece3
    rubix_cube[bottom_side][2][2], rubix_cube[bottom_side][2][1], rubix_cube[bottom_side][2][0] = left_piece1, left_piece2, left_piece3
    rubix_cube[turning_side][0][0], rubix_cube[turning_side][0][1], rubix_cube[turning_side][0][2], rubix_cube[turning_side][1][0], rubix_cube[turning_side][1][2], rubix_cube[turning_side][2][0],rubix_cube[turning_side][2][1], rubix_cube[turning_side][2][2] = turning_face3, turning_face5, turning_face8, turning_face2, turning_face7, turning_face1, turning_face4, turning_face6
    return rubix_cube


