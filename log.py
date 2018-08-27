#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/25 上午12:19
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : log.py
# @Software: PyCharm

from common_import import *
from conf.conf import *


def set_log_conf(log_dir, log_file):
    """配置日志格式的字典
    :param log_dir: str, 日志目录
    :param log_file: str, 日志文件名
    :return:
    """
    log_dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                'format': '%(asctime)s %(name)s [%(module)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
            'standard': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
        },

        "handlers": {
            "console_handler": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },

            "file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": os.path.join(log_dir, log_file),
                'mode': 'w+',
                "maxBytes": 1024*1024*5,  # 5 MB
                "backupCount": 20,
                "encoding": "utf-8"
            }
        },
        # 设置基本的logger
        "root": {
            'handlers': ['file_handler', 'console_handler'],
            'level': "DEBUG",
            'propagate': False
        }
    }
    return log_dict


def init_logging():
    """
    配置日志,初始化设置
    """

    # 创建路径
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)

    # 配置日志
    log_dict = set_log_conf(LOG_PATH, MEDICAL_SORT_NAME)
    logging.config.dictConfig(log_dict)
