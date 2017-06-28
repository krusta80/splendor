__all__ = ['agent']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'Agent'])
@Js
def PyJs_anonymous_0_(name, this, arguments, var=var):
    var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
    var.registers([u'name'])
    var.get(u"this").put(u'name', var.get(u'name'))
PyJs_anonymous_0_._set_name(u'anonymous')
var.put(u'Agent', PyJs_anonymous_0_)

@Js
def PyJs_anonymous_1_(board, players, playerIndex, moves, this, arguments, var=var):
    var = Scope({u'players':players, u'playerIndex':playerIndex, u'board':board, u'this':this, u'moves':moves, u'arguments':arguments}, var)
    var.registers([u'rand', u'i', u'totalMoves', u'players', u'playerIndex', u'board', u'moves', u'moveLabels', u'moveTypes'])
    if var.get(u'moves').get(u'purchase').get(u'length'):
        PyJs_Object_2_ = Js({u'label':Js(u'PURCHASE'),u'action':var.get(u'moves').get(u'purchase').get(u'0')})
        return PyJs_Object_2_
    var.put(u'moveTypes', Js([var.get(u'moves').get(u'takeChips'), var.get(u'moves').get(u'reserve').get(u'exposed'), var.get(u'moves').get(u'reserve').get(u'covered')]))
    var.put(u'moveLabels', Js([Js(u'TAKE'), Js(u'RESERVE_EXPOSED'), Js(u'RESERVE_COVERED')]))
    @Js
    def PyJs_anonymous_3_(a, b, this, arguments, var=var):
        var = Scope({u'a':a, u'this':this, u'b':b, u'arguments':arguments}, var)
        var.registers([u'a', u'b'])
        return (var.get(u'a')+var.get(u'b').get(u'length'))
    PyJs_anonymous_3_._set_name(u'anonymous')
    var.put(u'totalMoves', var.get(u'moveTypes').callprop(u'reduce', PyJs_anonymous_3_, Js(0.0)))
    var.put(u'rand', (var.get(u'Math').callprop(u'random')*var.get(u'totalMoves')))
    var.put(u'i', (-Js(1.0)))
    while (var.get(u'rand')>Js(0.0)):
        var.put(u'rand', var.get(u'moveTypes').get(var.put(u'i',Js(var.get(u'i').to_number())+Js(1))).get(u'length'), u'-')
    PyJs_Object_4_ = Js({u'label':var.get(u'moveLabels').get(var.get(u'Math').callprop(u'min', var.get(u'i'), Js(2.0))),u'action':var.get(u'moveTypes').get(var.get(u'Math').callprop(u'min', var.get(u'i'), Js(2.0))).get(var.get(u'Math').callprop(u'floor', (var.get(u'Math').callprop(u'random')*var.get(u'moveTypes').get(var.get(u'Math').callprop(u'min', var.get(u'i'), Js(2.0))).get(u'length'))))})
    return PyJs_Object_4_
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'Agent').get(u'prototype').put(u'makeMove', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_5_(nobles, this, arguments, var=var):
    var = Scope({u'this':this, u'nobles':nobles, u'arguments':arguments}, var)
    var.registers([u'nobles'])
    return var.get(u'nobles').get(u'0')
PyJs_anonymous_5_._set_name(u'anonymous')
var.get(u'Agent').get(u'prototype').put(u'takeNoble', PyJs_anonymous_5_)
pass


# Add lib to the module scope
agent = var.to_python()