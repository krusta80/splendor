__all__ = ['common']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'util'])
var.put(u'util', var.get(u'require')(Js(u'util')))
@Js
def PyJs_anonymous_1_(cost, this, arguments, var=var):
    var = Scope({u'this':this, u'cost':cost, u'arguments':arguments}, var)
    var.registers([u'cost'])
    @Js
    def PyJs_anonymous_2_(convertedCost, stackSize, this, arguments, var=var):
        var = Scope({u'convertedCost':convertedCost, u'this':this, u'stackSize':stackSize, u'arguments':arguments}, var)
        var.registers([u'convertedCost', u'stackSize'])
        return ((var.get(u'convertedCost')<<Js(3.0))+var.get(u'stackSize'))
    PyJs_anonymous_2_._set_name(u'anonymous')
    return var.get(u'cost').callprop(u'reduce', PyJs_anonymous_2_, Js(0.0))
PyJs_anonymous_1_._set_name(u'anonymous')
@Js
def PyJs_anonymous_3_(x, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
    var.registers([u'i', u'x', u'colors', u'inEnglish'])
    var.put(u'inEnglish', Js(u''))
    var.put(u'colors', Js([Js(u'B'), Js(u'G'), Js(u'R'), Js(u'W'), Js(u'b'), Js(u'*')]))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<Js(6.0)):
        try:
            var.put(u'inEnglish', (((var.get(u'colors').get(var.get(u'i'))+Js(u': '))+(var.get(u'x')&Js(7.0)))+Js(u',  ')), u'+')
            var.put(u'x', (var.get(u'x')>>Js(3.0)))
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    return var.get(u'inEnglish')
PyJs_anonymous_3_._set_name(u'anonymous')
@Js
def PyJs_anonymous_4_(color, this, arguments, var=var):
    var = Scope({u'color':color, u'this':this, u'arguments':arguments}, var)
    var.registers([u'color', u'colors'])
    PyJs_Object_5_ = Js({u'B':Js(0.0),u'G':Js(1.0),u'R':Js(2.0),u'W':Js(3.0),u'b':Js(4.0),u'g':Js(5.0)})
    var.put(u'colors', PyJs_Object_5_)
    return var.get(u'colors').get(var.get(u'color'))
PyJs_anonymous_4_._set_name(u'anonymous')
@Js
def PyJs_anonymous_6_(obj, this, arguments, var=var):
    var = Scope({u'this':this, u'obj':obj, u'arguments':arguments}, var)
    var.registers([u'obj'])
    return var.get(u'JSON').callprop(u'stringify', var.get(u'obj'))
PyJs_anonymous_6_._set_name(u'anonymous')
PyJs_Object_0_ = Js({u'convertCost':PyJs_anonymous_1_,u'translateChipCount':PyJs_anonymous_3_,u'getColorIndex':PyJs_anonymous_4_,u'show':PyJs_anonymous_6_})
var.get(u'module').put(u'exports', PyJs_Object_0_)
pass


# Add lib to the module scope
common = var.to_python()