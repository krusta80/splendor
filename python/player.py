__all__ = ['player']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'Player', u'common'])
var.put(u'common', var.get(u'require')(Js(u'./common.js')))
@Js
def PyJs_anonymous_0_(id, name, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'id':id, u'name':name}, var)
    var.registers([u'id', u'name'])
    var.get(u"this").put(u'id', var.get(u'id'))
    var.get(u"this").put(u'name', var.get(u'name'))
    var.get(u"this").callprop(u'reset')
PyJs_anonymous_0_._set_name(u'anonymous')
var.put(u'Player', PyJs_anonymous_0_)
var.get(u'module').put(u'exports', var.get(u'Player'))
@Js
def PyJs_anonymous_1_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put(u'purchasedCards', Js([]))
    var.get(u"this").put(u'cardChipValues', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.get(u"this").put(u'reservedCards', Js([]))
    var.get(u"this").put(u'nobles', Js([]))
    var.get(u"this").put(u'points', Js(0.0))
    var.get(u"this").put(u'chips', Js(0.0))
    var.get(u"this").put(u'chipsAndCards', Js(0.0))
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'reset', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(card, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'card':card}, var)
    var.registers([u'card'])
    if var.get(u'card').callprop(u'buy', var.get(u"this").get(u'id'), var.get(u"this").get(u'chipsAndCards')):
        var.get(u"this").callprop(u'payForCard', var.get(u'card'))
        var.get(u"this").get(u'purchasedCards').callprop(u'push', var.get(u'card'))
        var.get(u"this").put(u'points', var.get(u'card').get(u'points'), u'+')
        (var.get(u"this").get(u'cardChipValues').put(var.get(u'common').callprop(u'getColorIndex', var.get(u'card').get(u'color')),Js(var.get(u"this").get(u'cardChipValues').get(var.get(u'common').callprop(u'getColorIndex', var.get(u'card').get(u'color'))).to_number())+Js(1))-Js(1))
        var.get(u"this").callprop(u'updateChipsAndCards', var.get(u"this").get(u'chips'))
    else:
        var.get(u'console').callprop(u'log', Js(u'ERROR:  Cannot buy card ('), var.get(u'card'), Js(u')'))
PyJs_anonymous_2_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'buyCard', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_3_(card, gold, this, arguments, var=var):
    var = Scope({u'this':this, u'gold':gold, u'card':card, u'arguments':arguments}, var)
    var.registers([u'gold', u'card'])
    if (var.get(u"this").get(u'reservedCards').get(u'length')>=Js(3.0)):
        var.get(u'console').callprop(u'log', Js(u"ERROR:  Player's reserves are maxed out!"))
        return Js(False)
    if var.get(u'card').callprop(u'reserve', var.get(u"this").get(u'id')):
        var.get(u"this").put(u'chips', ((var.get(u'gold')&Js(1.0))<<Js(15.0)), u'+')
        var.get(u"this").put(u'chipsAndCards', ((var.get(u'gold')&Js(1.0))<<Js(15.0)), u'+')
        var.get(u"this").get(u'reservedCards').callprop(u'push', var.get(u'card'))
        if (var.get(u'card').get(u'owner')!=var.get(u"this").get(u'id')):
            var.get(u'console').callprop(u'log', Js(u'ERROR:  Owner mismatch!'))
        return var.get(u'true')
PyJs_anonymous_3_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'reserveCard', PyJs_anonymous_3_)
@Js
def PyJs_anonymous_4_(card, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'card':card}, var)
    var.registers([u'reservedCount', u'card'])
    var.put(u'reservedCount', var.get(u"this").get(u'reservedCards').get(u'length'))
    @Js
    def PyJs_anonymous_5_(reservedCard, this, arguments, var=var):
        var = Scope({u'this':this, u'reservedCard':reservedCard, u'arguments':arguments}, var)
        var.registers([u'reservedCard'])
        return (var.get(u'reservedCard').get(u'cost')!=var.get(u'card').get(u'cost'))
    PyJs_anonymous_5_._set_name(u'anonymous')
    var.get(u"this").put(u'reservedCards', var.get(u"this").get(u'reservedCards').callprop(u'filter', PyJs_anonymous_5_))
    if PyJsStrictEq(var.get(u'reservedCount'),var.get(u"this").get(u'reservedCards').get(u'length')):
        var.get(u'console').callprop(u'log', Js(u"ERROR:  Card not found in player's reserved pile!"))
        var.get(u'console').callprop(u'log', var.get(u'card'))
        var.get(u'console').callprop(u'log', var.get(u"this").get(u'reservedCards'))
        return Js(False)
    var.get(u"this").callprop(u'buyCard', var.get(u'card'))
PyJs_anonymous_4_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'activateCard', PyJs_anonymous_4_)
@Js
def PyJs_anonymous_6_(card, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'card':card}, var)
    var.registers([u'card', u'goldChipsNeeded', u'chipTotal', u'colorBalanceAfterCards', u'colorIndex'])
    var.put(u'chipTotal', var.get(u"this").get(u'chips'))
    var.put(u'goldChipsNeeded', Js(0.0))
    #for JS loop
    var.put(u'colorIndex', Js(0.0))
    while (var.get(u'colorIndex')<Js(5.0)):
        try:
            var.put(u'colorBalanceAfterCards', var.get(u'Math').callprop(u'max', Js(0.0), (((var.get(u'card').get(u'cost')>>(Js(3.0)*var.get(u'colorIndex')))&Js(3.0))-var.get(u"this").get(u'cardChipValues').get(var.get(u'colorIndex')))))
            var.get(u"this").put(u'chips', ((var.get(u"this").get(u'chips')&(((Js(1.0)<<Js(18.0))-Js(1.0))-(Js(7.0)<<(Js(3.0)*var.get(u'colorIndex')))))+(var.get(u'Math').callprop(u'max', Js(0.0), ((var.get(u'chipTotal')&Js(7.0))-var.get(u'colorBalanceAfterCards')))<<(Js(3.0)*var.get(u'colorIndex')))))
            var.put(u'goldChipsNeeded', var.get(u'Math').callprop(u'max', Js(0.0), (var.get(u'colorBalanceAfterCards')-(var.get(u'chipTotal')&Js(7.0)))), u'+')
            var.put(u'chipTotal', (var.get(u'chipTotal')>>Js(3.0)))
        finally:
                (var.put(u'colorIndex',Js(var.get(u'colorIndex').to_number())+Js(1))-Js(1))
    var.get(u"this").put(u'chips', (var.get(u'goldChipsNeeded')<<Js(15.0)), u'-')
PyJs_anonymous_6_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'payForCard', PyJs_anonymous_6_)
@Js
def PyJs_anonymous_7_(chips, this, arguments, var=var):
    var = Scope({u'this':this, u'chips':chips, u'arguments':arguments}, var)
    var.registers([u'chips'])
    var.get(u"this").put(u'chips', var.get(u'chips'), u'+')
    var.get(u"this").callprop(u'updateChipsAndCards', var.get(u"this").get(u'chips'))
PyJs_anonymous_7_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'addChips', PyJs_anonymous_7_)
@Js
def PyJs_anonymous_8_(chips, this, arguments, var=var):
    var = Scope({u'this':this, u'chips':chips, u'arguments':arguments}, var)
    var.registers([u'chips'])
    var.get(u"this").put(u'chips', var.get(u'chips'), u'-')
    var.get(u"this").callprop(u'updateChipsAndCards', var.get(u"this").get(u'chips'))
PyJs_anonymous_8_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'removeChips', PyJs_anonymous_8_)
@Js
def PyJs_anonymous_9_(chips, this, arguments, var=var):
    var = Scope({u'this':this, u'chips':chips, u'arguments':arguments}, var)
    var.registers([u'chips', u'colorIndex'])
    var.get(u"this").put(u'chipsAndCards', Js(0.0))
    #for JS loop
    var.put(u'colorIndex', Js(0.0))
    while (var.get(u'colorIndex')<Js(5.0)):
        try:
            var.get(u"this").put(u'chipsAndCards', (var.get(u'Math').callprop(u'min', Js(7.0), (var.get(u"this").get(u'cardChipValues').get(var.get(u'colorIndex'))+(var.get(u'chips')&Js(7.0))))<<(Js(3.0)*var.get(u'colorIndex'))), u'+')
            var.put(u'chips', (var.get(u'chips')>>Js(3.0)))
        finally:
                (var.put(u'colorIndex',Js(var.get(u'colorIndex').to_number())+Js(1))-Js(1))
    var.get(u"this").put(u'chipsAndCards', (var.get(u'chips')<<Js(15.0)), u'+')
PyJs_anonymous_9_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'updateChipsAndCards', PyJs_anonymous_9_)
@Js
def PyJs_anonymous_10_(noble, this, arguments, var=var):
    var = Scope({u'this':this, u'noble':noble, u'arguments':arguments}, var)
    var.registers([u'noble'])
    var.get(u"this").get(u'nobles').callprop(u'push', var.get(u'noble'))
    var.get(u"this").put(u'points', Js(3.0), u'+')
PyJs_anonymous_10_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'addNoble', PyJs_anonymous_10_)
@Js
def PyJs_anonymous_11_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").get(u'cardChipValues').callprop(u'slice', Js(0.0))
PyJs_anonymous_11_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'getCardChipValues', PyJs_anonymous_11_)
@Js
def PyJs_anonymous_12_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").get(u'reservedCards').callprop(u'slice', Js(0.0))
PyJs_anonymous_12_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'getReservedCards', PyJs_anonymous_12_)
@Js
def PyJs_anonymous_13_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").get(u'nobles').callprop(u'slice', Js(0.0))
PyJs_anonymous_13_._set_name(u'anonymous')
var.get(u'Player').get(u'prototype').put(u'getNobles', PyJs_anonymous_13_)
pass


# Add lib to the module scope
player = var.to_python()