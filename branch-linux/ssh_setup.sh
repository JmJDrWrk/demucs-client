sudo apt-get install openssh-server && 
sudo systemctl enable ssh && 
sudo systemctl start ssh && 
sudo systemctl status ssh && 
sudo ufw allow ssh &&
sudo ufw enable && 
sudo ufw status