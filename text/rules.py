#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Rule:

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)

class HeadingRule(Rule):
    type = 'heading'

    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)