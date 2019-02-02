sudo pacman -Syyuu &&
sudo pacman-mirrors -f 0 &&


sudo pacman -S trizen yay &&
yay --noconfirm -S - < packages.txt &&

yarn global add concurrently create-react-app create-react-native-app eslint eslint-plugin-vue express-generator http-server nodemon prisma vue-cli &&

# jupyter contrib nbextension install --user
# jupyter nbextensions_configurator enable --user

exec $SHELL -l &&

sudo sed -i 's/\(Exec=\)/\1env GTK_THEME=Breeze /' /usr/share/applications/firefox.desktop &&
sudo sed -i '$ s/\(firefox \)/\1-p private /' /usr/share/applications/firefox.desktop &&

sudo vim /usr/share/plasma/plasmoids/org.kde.plasma.kickoff/contents/ui/FullRepresentation.qml &&

fish
set -U fish_greeting "" &&
set -U fish_user_paths $HOME/.yarn/bin $fish_user_paths &&
set -U fish_user_paths /opt/miniconda3/bin/ $fish_user_paths &&
echo "source /opt/miniconda3/etc/fish/conf.d/conda.fish" >> .config/fish/config.fish &&

mkdir $HOME/.go &&
set -Ux GOPATH $HOME/.go &&
exit

git config --global user.name "rednithin" &&
git config --global user.email "reddy.nithinpg@live.com" &&

git clone https://github.com/rednithin/Zsh $HOME &&
ln -s $HOME/Zsh/zshrc.zsh $HOME/.zshrc &&

# sudo cp /usr/share/icons/breeze/status/16/media-playback-* /usr/share/icons/breath/status/16/ &&
# sudo cp /usr/share/icons/breeze/status/22/media-playback-* /usr/share/icons/breath/status/22/ &&
# sudo cp /usr/share/icons/breeze/status/24/media-playback-* /usr/share/icons/breath/status/24/ &&

yarn config set ignore-engines true &&

# sudo cpanm Log::Dispatch::File File::HomeDir Unicode::GCString YAML::Tiny Log::Log4perl &&

mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql &&
sudo systemctl start mariadb &&
sudo systemctl enable mariadb &&
mysql_secure_installation

rustup toolchain install stable &&
rustup default stable