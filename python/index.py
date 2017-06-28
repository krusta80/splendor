__all__ = ['index']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'stats', u'winner', u'game', u'Agent', u'outcomes', u'numberOfGames', u'Game', u'agents'])
var.put(u'Agent', var.get(u'require')(Js(u'./agent.js')))
var.put(u'Game', var.get(u'require')(Js(u'./game.js')))
if (var.get(u'process').get(u'argv').get(u'length')<Js(4.0)):
    var.get(u'console').callprop(u'log', Js(u'usage:'), var.get(u'process').get(u'argv').get(u'1'), Js(u'<number of games> <player 1 name>...<player n name>'))
    var.get(u'process').callprop(u'exit')
var.put(u'numberOfGames', var.get(u'process').get(u'argv').get(u'2'))
@Js
def PyJs_anonymous_0_(name, this, arguments, var=var):
    var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
    var.registers([u'name'])
    return var.get(u'Agent').create(var.get(u'name'))
PyJs_anonymous_0_._set_name(u'anonymous')
var.put(u'agents', var.get(u'process').get(u'argv').callprop(u'slice', Js(3.0)).callprop(u'map', PyJs_anonymous_0_))
var.put(u'game', var.get(u'Game').create(var.get(u'agents')))
var.put(u'outcomes', Js([]))
PyJs_Object_1_ = Js({})
var.put(u'stats', PyJs_Object_1_)
pass
while (var.put(u'numberOfGames',Js(var.get(u'numberOfGames').to_number())-Js(1))+Js(1)):
    if PyJsStrictEq((var.get(u'numberOfGames')%Js(1000.0)),Js(0.0)):
        var.get(u'console').callprop(u'log', var.get(u'numberOfGames'))
    var.get(u'game').callprop(u'reset')
    var.get(u'outcomes').callprop(u'push', var.get(u'game').callprop(u'playUntilEnd'))
    var.put(u'winner', var.get(u'game').callprop(u'getWinner'))
    if var.get(u'stats').get(var.get(u'winner')).neg():
        var.get(u'stats').put(var.get(u'winner'), Js(0.0))
    (var.get(u'stats').put(var.get(u'winner'),Js(var.get(u'stats').get(var.get(u'winner')).to_number())+Js(1))-Js(1))
var.get(u'console').callprop(u'log', var.get(u'outcomes'))
var.get(u'console').callprop(u'log', var.get(u'stats'))
pass


# Add lib to the module scope
index = var.to_python()