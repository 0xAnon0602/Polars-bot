echo '```'Holders: $(curl https://etherscan.io/token/0xc17fbe1d709ddf6c0b6665dd0591046815ac7554 -s | sed -n 's/.* holders \([^ ]*\).*/\1/p' | sed -n '1p')'```'
