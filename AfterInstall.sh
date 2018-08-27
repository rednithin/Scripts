
sudo pacman -S nodejs npm yarn chromium go rustup gparted fish fisherman yaourt mongodb mongodb-tools opera kodi vim simplescreenrecorder mpv youtube-dl aria2 kipi-plugins plasma5-applets-redshift-control cpanminus texlive-core texlive-bin

yaourt -S teamviewer visual-studio-code-bin spotify ttf-fira-code mongodb-compass postman-bin ttf-ms-fonts --noconfirm --aur

yarn global add nativescript create-react-app create-react-native-app create-next-app vue-cli grommet-cli eslint flow-bin concurrently http-server serve eslint eslint-plugin-vue

sudo pip install ipython numpy scipy matplotlib virtualenv jupyter jupyter_contrib_nbextensions pylint jupyterlab autopep8 beautifulsoup4 scrapy pylint autopep8
jupyter contrib nbextension install --user
jupyter nbextensions_configurator enable --user

chsh

set -U fish_greeting ""
set -U fish_user_paths /home/nithin/.yarn/bin $fish_user_paths
mkdir /home/nithin/.go
set -Ux GOPATH /home/nithin/.go

sudo pacman-mirrors -b stable
sudo pacman -Syy; and sudo pacman -Suu; and sudo pacman -Syu

yarn config set ignore-engines true

sudo cpanm Log::Dispatch::File File::HomeDir Unicode::GCString YAML::Tiny Log::Log4perl

# fisher omf/theme-edan