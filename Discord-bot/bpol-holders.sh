echo '```'Holders: $(curl https://bscscan.com/token/0x8a9c889e60ee674f0d55075fa0d60fb05e1a7aee -s | sed -n 's/.* holders \([^ ]*\).*/\1/p' | sed -n '1p')'```'
