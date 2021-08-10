#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: root.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/8/8 5:41 PM
"""

from fastapi import APIRouter

from app import schemas, worker

router = APIRouter()


@router.post("/submit", response_model=schemas.SimpleResponse)
async def submit(args: schemas.FormArgs):
    return {"msg": args.json()}


@router.get("/test_celery", response_model=schemas.SimpleResponse)
async def test_celery():
    task = worker.test_celery.apply_async(("hello",), queue="main-queue")
    return {"msg": task.get()}
