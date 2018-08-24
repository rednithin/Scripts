#!/bin/bash
sudo sed -i 's/\(Exec=\)/\1env GTK_THEME=Breeze /' /usr/share/applications/firefox.desktop
sudo sed -i '$ s/\(firefox \)/\1-p private /' /usr/share/applications/firefox.desktop
