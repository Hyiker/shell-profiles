from tools import ExportableCollection, TargetPlat
import argparse

cc = ExportableCollection()

cc.add_alias('code', 'code-insiders')
cc.add_alias('p', 'python')
cc.add_alias('p3', 'python3')
cc.add_alias('ff', 'ffmpeg')
cc.add_alias('youtube-dl', 'yt-dlp')
cc.add_alias('vim', 'nvim')
cc.add_alias('vi', 'nvim')
cc.add_alias('which', 'get-command', plats=[TargetPlat.POWERSHELL])
cc.add_alias('open', 'explorer', plats=[TargetPlat.POWERSHELL])

cc.add_ev('HTTP_PROXY', 'http://127.0.0.1:7890')
cc.add_ev('HTTPS_PROXY', 'http://127.0.0.1:7890')
cc.add_ev('ALL_PROXY', 'http://127.0.0.1:7890')
cc.add_ev('http_proxy', 'http://127.0.0.1:7890')
cc.add_ev('https_proxy', 'http://127.0.0.1:7890')
cc.add_ev('all_proxy', 'http://127.0.0.1:7890')

# powershell add environment variable
cc.build_custom_shell_func().add_ps_func_from_file('custom/env.ps1').build()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Export profiles crossing platforms')
    parser.add_argument('--ps', type=str, help='export powershell', default='profile.ps1')
    parser.add_argument('--bash', type=str, help='export bash', default='.profile')
    args = parser.parse_args()
    if ps := args.ps:
        with open(ps, 'w') as foo:
            foo.write(cc.compile_ps())
    if bash := args.bash:
        with open(bash, 'w') as foo:
            foo.write(cc.compile_bash())
