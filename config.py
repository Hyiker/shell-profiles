from tools.helper import *
import argparse

cc = CommandCollection()

cc.append(AliasCommand('code', 'code-insiders'))
cc.append(AliasCommand('p', 'python'))
cc.append(AliasCommand('p3', 'python3'))
cc.append(AliasCommand('ff', 'ffmpeg'))
cc.append(AliasCommand('youtube-dl', 'yt-dlp'))

cc.append(EVCommand('HTTP_PROXY', 'http://127.0.0.1:7890'))
cc.append(EVCommand('HTTPS_PROXY', 'http://127.0.0.1:7890'))
cc.append(EVCommand('ALL_PROXY', 'http://127.0.0.1:7890'))
cc.append(EVCommand('http_proxy', 'http://127.0.0.1:7890'))
cc.append(EVCommand('https_proxy', 'http://127.0.0.1:7890'))
cc.append(EVCommand('all_proxy', 'http://127.0.0.1:7890'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export profiles crossing platforms')
    parser.add_argument('--ps', type=str, help='export powershell')
    parser.add_argument('--bash', type=str, help='export bash')
    args = parser.parse_args()
    if ps := args.ps:
        with open(ps, 'w') as foo:
            foo.write(cc.compile_ps())
    if bash := args.bash:
        with open(bash, 'w') as foo:
            foo.write(cc.compile_bash())
