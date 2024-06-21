import requests
import re
import json
# 代码有错误，无法进行对json解析

url = 'https://vd6.l.qq.com/proxyhttp'
data = '{"buid":"onlyvinfo","vinfoparam":"charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200syv5tor%2Fm00471y98i3.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200syv5tor%2Fm00471y98i3.html&sphttps=1&encryptVer=9.2&cKey=fZfHd9m17_i11M1Orq2-LnCjnpb8Ocr0cPTcY3jMzEul_f4uOWcoUmJNR8G177I5OlJKj0xWlWraCp7VHCeQghpmp7rG5tiHjLv_PnnatnPaZfOXktuBpd_Ii-ctopCam13s_IMO5sAvFjOj-NmZhE-NjjawCzIdF66cdsFdzz5jk70UOmynTHDptaxqIemxrSlkg-M_BbDaBoWwiX7uSsBkDK_qlv9BvC71Ch6ixh2gniDG5LKtpya6ni_VmBm3gdW2SPCpvJY8ymTr2rFp56lxzzDtPFKhwYCtsQcaQ5txIefj4bzawfqzkqynoc8SM4Zzh-tm4MPVSaSl29Zyy7900ICoeOJZY6b_P75Em4nh9wpcKyMc2-ZSG3IOk0hnCuc2Zr8bNdI90MIn9qwngq39fYDM-5q-9hCJy5AjxN0GmZunIBDR37Gt4j2ntrJWOa_08iyeOslYAFY1slGC-jRM--uI4V9GTo25H9-wZNGMYva2wMzkWJplWGKNS3cQWEihYDfc89A4wCcDkmmyb7JwecT-EWB2V9xwIcqwTwqCo5SjbOqbP4z83N6haK7KskXWake3iMwICAgICAgICB9ZYbQ&clip=4&guid=396588f596fd821e&flowid=c9770e665acb53e4d74daa835283c46f&platform=10201&sdtfrom=v1010&appVer=1.30.3&unid=&auth_from=&auth_ext=&vid=m00471y98i3&defn=shd&fhdswitch=1&dtype=3&spsrt=2&tm=1705489694&lang_code=0&logintoken=&spvvpay=1&spadseg=3&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&hevclv=31&drm=40","lcAdCookie":"o_minduid=8_zo6w5a40uICnZlRB_aQK-F30j00yV8; appuser=8F85C9CEA446260F; full_screen_cid_pause_times=1; full_screen_pause_times=1; LZTturn=960; Lturn=417; LKBturn=416; LPVLturn=226; LZCturn=719; LPSJturn=658; LBSturn=948; LVINturn=394; LPHLSturn=303; LDERturn=581; LPPBturn=297; LPDFturn=923"}'

headers = {
'authority':'vd6.l.qq.com',
'Cookie':'pgv_pvid=8246472714; pac_uid=0_2584eae2c7601; ptcz=e7977afc6d90c391af316513e1c029a354943dc02facafdbddb29856d1d7cef2; qq_domain_video_guid_verify=396588f596fd821e; _qimei_uuid42=181100f2f321004a1923759bb98997363088834ea5; _qimei_q36=; _qimei_h38=2db8277c1923759bb989973602000003118110; appuser=8F85C9CEA446260F; pgv_info=ssid=s3379966856; video_platform=2; lv_play_index=0; vversion_name=8.2.95; video_omgid=396588f596fd821e; _qimei_fingerprint=d3c60c3b650720acc14bcdd8e80ce840; o_minduid=8_zo6w5a40uICnZlRB_aQK-F30j00yV8; full_screen_cid_pause_times=1; full_screen_pause_times=1; LZTturn=960; Lturn=417; LKBturn=416; LPVLturn=226; LZCturn=719; LPSJturn=658; LBSturn=948; LVINturn=394; LPHLSturn=303; LDERturn=581; LPPBturn=297; LPDFturn=923',
'Origin':'https://v.qq.com',
'Referer':'https://v.qq.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'

}


response = requests.post(url=url,json=data,headers=headers)
print(response.json())