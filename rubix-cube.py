#abbreviation for ease of typing
w, g, r ,b ,o, y = "white", "green", "red", "blue", "orange", "yellow"

#assigned at starting position
whiteface = [
    [w, w, w], 
    [w, w, w] 
    [w, w, w]
]

greenface = [
    [g, g, g],
    [g, g, g],
    [g, g, g],
]

redface = [
    [r, r, r],
    [r, r, r],
    [r, r, r],
]

blueface = [
    [b, b, b],
    [b, b, b],
    [b, b, b],
]

orangeface = [
    [o, o, o],
    [o, o, o],
    [o, o, o],
]

yellowface = [
    [y, y, y], 
    [y, y, y], 
    [y, y, y], 
]

def clockwise(which_face, wface, gface, rface, oface, yface):
    # keep track of pieces in its previous state
    # change to front, left, etc
    wpiece1, wpiece2, wpiece3 = wface[2][0], wface [2][1], wface[2][2]
    rpiece1, rpiece2, rpiece3 = rface[0][0], rface [1][0], rface[2][0]
    ypiece1, ypiece2, ypiece3 = yface[0][2], yface [0][1], yface[0][0]
    opiece1, opiece2, opiece3 = oface[2][2], oface [1][2], oface[0][2]
    
    #keep track of all green face pieces
    gpiece1, gpiece2, gpiece3, gpiece4, gpiece5, gpiece6, gpiece7, gpiece8 = gface[0][0], #etc
    
    #copy data copied from current state of cube onto new state of cube
    rface[0][0], rface [1][0], rface[2][0] = wpiece1, wpiece2, wpiece3
    yface[0][2], yface [0][1], yface[0][0] = rpiece1, rpiece2, rpiece3
    oface[2][2], oface [1][2], oface[0][2] = ypiece1, ypiece2, ypiece3
    wface[2][0], wface [2][1], wface[2][2] = opiece1, opiece2, opiece3
    return wface, gface, rface, oface, yface