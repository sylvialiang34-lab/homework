#!/usr/bin/env python
# -*- coding: utf-8 -*-

#一
#加了“”按字符串比较,实际是比字符串的unicode
#而且是从左往右一位一位的比，例如"134" < "24" => True,是因为1的unicode小于2的

#二
#type ( 3e7 ) => float, 所以是浮点数
#e表示10n次幂,科学计数法

#三
#对于使用“<”“>” 比大小,str只能和str比较,float int and bool 可以互相比较

#IndentationError, 在定义x和y的时候没缩进【x == y 】
#NameError,命名Z的时候错误【x=y=z】
#SyntaxError,在尝试运用if的函数时语法错误【if x=y , print (x) 】

