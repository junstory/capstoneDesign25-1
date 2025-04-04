#!/bin/bash

# rdate 설치 여부 확인
if ! command -v rdate &> /dev/null; then
    echo "rdate가 설치되어 있지 않습니다. 설치를 시도합니다..."
    sudo apt update
    sudo apt install -y rdate
fi

# 시간 동기화
sudo rdate -s time.bora.net

# 동기화 결과 출력
date