import os
from dotenv import load_dotenv
from api.slack import post_text

load_dotenv(verbose=True)

ZOOM_STUDY_WEBHOOK_URL = os.environ.get("ZOOM_STUDY_WEBHOOK_URL")

ZOOM_STUDY_NOTICE = """1. 한 주동안 달성하고자 하는 목표를 적어주세요.
2. 지난 일주일동안의 목표 달성률과 그 이유를 적어주세요

[예시]
😀 이번주 목표
  - 도메인 주도 설계 책 4챕터까지 읽기
🤗 지난주 달성
  - 75/100, 3챕터까지 다 읽고자했지만, 못 읽었다.

😉 목표의 방향은 정해져있지않아요.
🙃 스스로 할 수 있는 목표치를 정해보아요.
😇 매주 목표를 정하고, 점검해보아요
🥰 목표가 많다면 여러개를 적어도 돼요
"""


if __name__ == "__main__":
    ret = post_text(ZOOM_STUDY_WEBHOOK_URL, ZOOM_STUDY_NOTICE)
    print(ret)
