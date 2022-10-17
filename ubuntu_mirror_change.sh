#!/usr/bin/env bash
#카카오 미러가 터져서 생긴..
#forked from https://gist.github.com/lesstif/8185f143ba7b8881e767900b1c8e98ad

SL=/etc/apt/sources.list

PARAM="r:hm:dnak"

KAKAO=mirror.kakao.com
KAIST=ftp.kaist.ac.kr
HARU=ftp.harukasan.org

if [ "$(id -u)" != "0" ]; then
   echo "'$0' must be run as root" 1>&2
   exit 1
fi

function  usage {
    echo "USAGE: $0 [OPTION] ";
    echo -e "\r\n-b : make backup file";
    echo "-r[sources.list] : specify source list file (default ${SL})"
    echo "-m[mirror-url] : speficy mirror site url"
    echo "-k : use kakao mirror (${KAKAO})"
    echo "-n : use kaist mirror (${KAIST})"
    echo "-a : use harukasan mirror (${HARU})"

    exit 0;
}

REPOS=${KAKAO}

while getopts $PARAM opt; do
    case $opt in
        r)
            echo "-r option was supplied. OPTARG: $OPTARG" >&2
            SL=$OPTARG;
            ;;
        m)
            echo "Using mirror repository(${OPTARG})." >&2
            REPOS=${OPTARG}
            ;;
        k)
            echo "Using Kakao repository(${KAKAO})." >&2
            REPOS=${KAKAO}
            ;;
        n)
            echo "Using kaist repository(${KAIST})." >&2
            REPOS=${KAIST}
            ;;
        a)
            echo "Using harukasan repository(${HARU})." >&2
            REPOS=${HARU}
            ;;
        h)
            usage;
             ;;
    esac
done

echo "using repository(${REPOS})"

## change mirror
# sed -i.bak -re "s/([a-z]{2}.)?archive.ubuntu.com|security.ubuntu.com/${REPOS}/g" ${SL}
sed -i.bak -re "s/([a-z]{2}.)?mirror.kakao.com/${REPOS}/g" ${SL}

## check
apt update
