# coding: UTF-8
from __future__ import print_function

import boto3,os
import json,logging,re
import http.client, urllib.parse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Loading function')

def lambda_handler(event, context):
    
    # このサービスが動作するか決定する。動作条件は、「君の名」という単語が含まれているかどうか。
    lineText = event["lineMessage"]["events"][0]["message"]["text"]
    logger.info(lineText)
    if "君の名" not in lineText :
        logger.info("応答すべきメッセージではない")
        return 
    
    # メッセージタイプがUserではない場合は応答しない
    if "user" !=  event["lineMessage"]["events"][0]["source"]["type"] :
        logger.info("メッセージタイプがUserではない")
        return 
        
    # 応答メッセージ組み立て
    repMessage = "私の名はMr.i-lab、通称i-lab君です。あなたと入れ替わったりしないから安心して下さい。あ、今日は彗星見えるかもしれませんね。"
    
    logger.info(repMessage)

    # メッセージを送信したUserのIDを返す
    return {
         "message" : repMessage
    }
    
