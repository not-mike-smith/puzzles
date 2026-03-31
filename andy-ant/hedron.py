from __future__ import annotations
from face import Face


def coin() -> Face:
    [heads, tails] = [Face(name) for name in ['heads', 'tails']]
    heads.touch(tails)
    return heads


def ribbon3() -> Face:
    [home, left, right] = [Face(name) for name in ['home', 'left', 'right']]
    home.touch(left)
    home.touch(right)
    left.touch(right)
    return home


def ribbon4() -> Face:
    [home, left, right, opposite] = [Face(name) for name in ['home', 'left', 'right', 'opposite']]
    home.touch(left)
    home.touch(right)
    opposite.touch(left)
    opposite.touch(right)
    return home


def ribbon5() -> Face:
    [home, left1, left2, right1, right2] = [Face(name) for name in ['home', 'left1', 'left2', 'right1', 'right2']]
    home.touch(left1)
    left1.touch(left2)
    left2.touch(right2)
    right2.touch(right1)
    right1.touch(home)
    return home


def ribbon6() -> Face:
    names = ['home', 'left1', 'left2', 'opposite', 'right2', 'right1']
    [home, left1, left2, opposite, right2, right1] = [Face(name) for name in names]
    home.touch(left1)
    left1.touch(left2)
    left2.touch(opposite)
    opposite.touch(right2)
    right2.touch(right1)
    right1.touch(home)
    return home


def tetrahedron() -> Face:
    [home, side1, side2, side3] = [Face(name) for name in ['home', 'side1', 'side2', 'side3']]
    home.touch(side1)
    home.touch(side2)
    home.touch(side3)
    side1.touch(side2)
    side2.touch(side3)
    side3.touch(side1)
    return home


def cube() -> Face:
    names = ['h', 's1', 's2', 's3', 's4', 'op']
    [home, side1, side2, side3, side4, opposite] = [Face(name) for name in names]
    home.touch(side1).touch(opposite)
    home.touch(side2).touch(opposite)
    home.touch(side3).touch(opposite)
    home.touch(side4).touch(opposite)
    side1.touch(side2).touch(side3).touch(side4).touch(side1)
    return home


def tri_prism() -> Face:
    names = ['h', 's1', 's2', 's3', 'op']
    [home, side1, side2, side3, opposite] = [Face(name) for name in names]
    home.touch(side1).touch(opposite)
    home.touch(side2).touch(opposite)
    home.touch(side3).touch(opposite)
    side1.touch(side2).touch(side3).touch(side1)
    return home


def penta_prism() -> Face:
    names = ['h', 's1', 's2', 's3', 's4', 's5', 'op']
    [home, side1, side2, side3, side4, side5, opposite] = [Face(name) for name in names]
    home.touch(side1).touch(opposite)
    home.touch(side2).touch(opposite)
    home.touch(side3).touch(opposite)
    home.touch(side4).touch(opposite)
    home.touch(side5).touch(opposite)
    side1.touch(side2).touch(side3).touch(side4).touch(side5).touch(side1)
    return home


def octohedron() -> Face:
    names = ['h', 's11', 's12', 's13', 's21', 's22', 's23', 'op']
    [home, s11, s12, s13, s21, s22, s23, op] = [Face(name) for name in names]
    home.touch(s11).touch(s22).touch(op)
    home.touch(s12).touch(s23).touch(op)
    home.touch(s13).touch(s21).touch(op)
    s11.touch(s23)
    s12.touch(s21)
    s13.touch(s22)
    return home


def soccer_ball() -> Face:
    names = [
        'h',
        'hex11', 'hex12', 'hex13', 'hex14', 'hex15',
        'hex21', 'hex22', 'hex23', 'hex24', 'hex25',
        'pen21', 'pen22', 'pen23', 'pen24', 'pen25',
        'hex31', 'hex32', 'hex33', 'hex34', 'hex35',
        'pen31', 'pen32', 'pen33', 'pen34', 'pen35',
        'hex41', 'hex42', 'hex43', 'hex44', 'hex45',
        'pen5'
    ]

    [
        home,
        hex11, hex12, hex13, hex14, hex15,
        hex21, hex22, hex23, hex24, hex25,
        pen21, pen22, pen23, pen24, pen25,
        hex31, hex32, hex33, hex34, hex35,
        pen31, pen32, pen33, pen34, pen35,
        hex41, hex42, hex43, hex44, hex45,
        pen5
    ] = [Face(name) for name in names]

    home.touch(hex11).touch(hex21).touch(pen31)
    home.touch(hex12).touch(hex22).touch(pen32)
    home.touch(hex13).touch(hex23).touch(pen33)
    home.touch(hex14).touch(hex24).touch(pen34)
    home.touch(hex15).touch(hex25).touch(pen35)

    pen5.touch(hex41).touch(hex31).touch(pen21)
    pen5.touch(hex42).touch(hex32).touch(pen22)
    pen5.touch(hex43).touch(hex33).touch(pen23)
    pen5.touch(hex44).touch(hex34).touch(pen24)
    pen5.touch(hex45).touch(hex35).touch(pen25)

    hex11.touch(hex12).touch(hex13).touch(hex14).touch(hex15).touch(hex11)
    hex41.touch(hex42).touch(hex43).touch(hex44).touch(hex45).touch(hex41)
    hex21.touch(pen21).touch(hex22).touch(pen22).touch(hex23).touch(pen23).touch(hex24).touch(pen24).touch(hex25).touch(pen25).touch(hex21)
    hex31.touch(pen31).touch(hex32).touch(pen32).touch(hex33).touch(pen33).touch(hex34).touch(pen34).touch(hex35).touch(pen35).touch(hex31)

    hex11.touch(pen21).touch(hex12).touch(pen22).touch(hex13).touch(pen23).touch(hex14).touch(pen24).touch(hex15).touch(pen25).touch(hex11)
    hex45.touch(pen31).touch(hex41).touch(pen32).touch(hex42).touch(pen33).touch(hex43).touch(pen34).touch(hex44).touch(pen35).touch(hex45)

    hex35.touch(hex21).touch(hex31).touch(hex22).touch(hex32).touch(hex23).touch(hex33).touch(hex24).touch(hex34).touch(hex25).touch(hex35)
    return home
