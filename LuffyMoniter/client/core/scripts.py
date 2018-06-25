#!/usr/bin/env python
# -*- coding:utf-8 -*-
from src.client import AutoSSH


def client():
    cli = AutoSSH()
    cli.process()